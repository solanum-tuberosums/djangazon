from django.shortcuts import render
from website.models.order_model import Order
from website.models.product_model import Product


def index(request):
    """
    This function is invoked to show the index page.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders complete_index.html

        ---Context---
        --if there are products available to purchase--
            product_dict_list: a list of products available to purchase
        --if there are no products available to purchase--
            error: "No products are available."

    Author: Jeremy Bakker and Blaise Roberts
    """

    template_name = 'index.html'
    my_product_list = Product.objects.filter(current_inventory__gt=0, 
        is_active=1).order_by('-id')[:20]
    try:
        order_id = request.user.profile.get_user_order()
    except: 
        order_id = ''
    active_order_products = []
    if order_id != '':
        active_order = Order.objects.get(pk=order_id)
        active_order_products = active_order.products.distinct()
    possible_recommendations = []
    possible_list = []

    if request.user.is_authenticated():
        all_products = Product.objects.all()
        user_liked_products = request.user.likes.all()
        user_disliked_products = request.user.dislikes.all()
        possible_products = all_products.difference(user_liked_products, 
            user_disliked_products)
        
        for product in possible_products:
            possibility_coefficient = 0
            likes_sum = 0
            dislikes_sum = 0
            print("possible product--",product.title)
            users_who_have_liked = product.likes.all()
            users_who_have_disliked = product.dislikes.all()
            product_interaction_count = product.likes.all().count() +\
                product.dislikes.all().count()
            print("product interaction count--",product_interaction_count)
            if product_interaction_count == 0:
                pass
            else:
                for user in users_who_have_liked:
                    likes_sum += get_similarity_index(request.user, user)
                    print("new sum of Likes indices--", likes_sum)
                for user in users_who_have_disliked:
                    dislikes_sum += get_similarity_index(request.user, user)
                    print("new sum of DISlikes indices--", dislikes_sum)
                
                possibility_coefficient = (likes_sum - dislikes_sum) / product_interaction_count
                print("possibility coefficient--", possibility_coefficient)
                
                if possibility_coefficient > .25:
                    product_tuple = (product, possibility_coefficient)
                    possible_list.append(product_tuple)

        if possible_list:
            for product_tuple in possible_list:
                print("possible products unsorted--\n", product_tuple[0].title, product_tuple[1])    
            possible_list.sort(key=lambda tup: tup[1], reverse=True)
            for product_tuple in possible_list:
                print("possible products sorted--\n", product_tuple[0].title)
                possible_recommendations.append(product_tuple[0]) 
        print("possible recommendation list of products", possible_recommendations)

    if my_product_list:
        return render(request, template_name, 
            {'product_dict_list': my_product_list, 'product_recommendations':possible_recommendations, 'order_products':active_order_products})
    else:
        return render(request, template_name, {'product_dict_list': [], 
            "error": "No products are available."})


def get_similarity_index(user_one, user_two):
    user_one_likes = user_one.likes.all()
    user_one_dislikes = user_one.dislikes.all()

    user_two_likes = user_two.likes.all()
    user_two_dislikes = user_two.dislikes.all()

    users_likes_intersection = len(user_one_likes.intersection(
        user_two_likes))
    users_dislikes_intersection = len(user_one_dislikes.intersection(
        user_two_dislikes))

    user_one_like_user_two_dislike_intersection = \
        len(user_one_likes.intersection(user_two_dislikes))
    user_two_likes_user_one_dislikes_intersection = \
        len(user_two_likes.intersection(user_one_dislikes))

    print('user_one', user_one)
    print('user_two', user_two)
    divisor = len(user_one_likes.union(user_two_likes, user_one_dislikes, user_two_dislikes))
    print('divisor', divisor)
    dividend =  users_likes_intersection + users_dislikes_intersection - user_one_like_user_two_dislike_intersection - user_two_likes_user_one_dislikes_intersection
    print('dividend', dividend)
    user_similarity_index = dividend/divisor
    print('user_similarity_index', user_similarity_index)
    return user_similarity_index













