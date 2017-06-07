from django.shortcuts import render
from website.models.order_model import Order
from website.models.product_model import Product


def index(request):
    """
    This function is invoked to show the index page, which includes a list of 
    the 20 most recently added products and a list of recommendations for the 
    current user based on the Jaccard Similarity Index.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders index.html

        ---Context---
        --if there are products available to purchase--
            product_dict_list: a list of products available to purchase
        --if there are no products available to purchase--
            error: "No products are available."
        --if there are recommended products--
            product_recommendations: a list of recommended products
        --if there are no recommended products--
            notice: "Like or Dislike more products to get recommendations"

    Author: Jeremy Bakker and Blaise Roberts
    """

    template_name = 'index.html'
    my_product_list = Product.objects.filter(current_inventory__gt=0, 
        is_active=1).order_by('-id')[:20]
    ## Getting info for shopping cart
    try:
        order_id = request.user.profile.get_user_order()
    except: 
        order_id = ''
    active_order_products = []
    if order_id != '':
        active_order = Order.objects.get(pk=order_id)
        active_order_products = active_order.products.distinct()

    ## Getting product recommendations
    possible_recommendations = []
    possible_list = []
    # Get all users' liked and dislked products
    if request.user.is_authenticated():
        all_products = Product.objects.all()
        user_liked_products = request.user.likes.all()
        user_disliked_products = request.user.dislikes.all()
        # Get products that user has not liked or disliked (not interacted with)
        possible_products = all_products.difference(user_liked_products, 
            user_disliked_products)
        
        for product in possible_products:
            # Reset product's possibility_coefficient to 0
            possibility_coefficient = 0
            likes_sum = 0
            dislikes_sum = 0
            # Get list of users who have liked/disliked product
            users_who_have_liked = product.likes.all()
            users_who_have_disliked = product.dislikes.all()
            # Count "interaction" (likes and dislikes) for product
            product_interaction_count = product.likes.all().count() +\
                product.dislikes.all().count()
            # If user has no interaction with a product, ignore
            if product_interaction_count == 0:
                pass
            else:
                # Add similarity_index (calculated from get_similarity_index
                # function below) to likes_sum tally for each user who has 
                # liked a particular product
                for user in users_who_have_liked:
                    likes_sum += get_similarity_index(request.user, user)
                # Add similarity_index to dislikes_sum tally for each user who 
                # has disliked a particular product    
                for user in users_who_have_disliked:
                    dislikes_sum += get_similarity_index(request.user, user)
                # Possibility coefficient is the likelihood that the current 
                # user will be recommended a product they have not yet 
                # interacted with relative to other users who have interacted 
                # with it.  This should be higher for a product that similar
                # users have liked or for a product that dissimilar users have 
                # disliked.
                possibility_coefficient = (likes_sum - dislikes_sum) / product_interaction_count
                
                if possibility_coefficient > .25:
                    product_tuple = (product, possibility_coefficient)
                    possible_list.append(product_tuple)

        #sorts the possible_list to show highest possibility at the top
        if possible_list:
            possible_list.sort(key=lambda tup: tup[1], reverse=True)
            for product_tuple in possible_list:
                possible_recommendations.append(product_tuple[0])
    if my_product_list:
        return render(request, template_name, 
            {'product_dict_list': my_product_list, 'product_recommendations':possible_recommendations, 'order_products':active_order_products})
    else:
        return render(request, template_name, {'product_dict_list': [], 
            "error": "No products are available."})


def get_similarity_index(user_one, user_two):
    """
    This function calculates the Jaccard Similarity Coefficient, which 
    represents similarity in product preferences between two users based on 
    product likes and dislikes. It is called in the index() function above in 
    order to display products recommended to the current user. 

    ---Arguments---
    user_one: current user
    user_two: any other user who has interacted with the product for which we 
    are calculating the possibility coefficient.

    Author: Jeremy Bakker, Blaise Roberts, Will Sims, Jessica Younker
    """
    # All liked and disliked products for current user
    user_one_likes = user_one.likes.all()
    user_one_dislikes = user_one.dislikes.all()

    # All liked and disliked products for another user
    user_two_likes = user_two.likes.all()
    user_two_dislikes = user_two.dislikes.all()

    # Number of matching liked products between the 2 users
    users_likes_intersection = len(user_one_likes.intersection(
        user_two_likes))
    # Number of matching disliked products between the 2 users
    users_dislikes_intersection = len(user_one_dislikes.intersection(
        user_two_dislikes))

    # Number of products liked by user 1 but dislked by user 2
    user_one_like_user_two_dislike_intersection = \
        len(user_one_likes.intersection(user_two_dislikes))
    # Number of products liked by user 2 but dislked by user 1
    user_two_likes_user_one_dislikes_intersection = \
        len(user_two_likes.intersection(user_one_dislikes))

    # Total number of likes and dislikes in common between the two users (the 
    # actual divisor in the equation for this piece of the Jaccard Index)    
    divisor = len(user_one_likes.union(user_two_likes, user_one_dislikes, user_two_dislikes))
    # Total number of likes and dislikes in common between the two users minus
    # the total number of opposite ratings between them (the actual dividend
    # in the equation for this piece of the Jaccard Index)
    dividend =  users_likes_intersection + users_dislikes_intersection - user_one_like_user_two_dislike_intersection - user_two_likes_user_one_dislikes_intersection
    # The Jaccard Index:
    user_similarity_index = dividend/divisor
    return user_similarity_index













