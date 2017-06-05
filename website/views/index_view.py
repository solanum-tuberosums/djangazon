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


    if request.user.is_authenticated():
        all_products = Product.objects.all()
        user_liked_products = request.user.likes.all()
        user_disliked_products = request.user.dislikes.all()
        possible_products = all_products.difference(user_liked_products, 
            user_disliked_products)
        
        possible_recommendations = []
        sum_user_similarity_indices_of_likes = 0
        sum_user_similarity_indices_of_dislikes = 0
        for product in possible_products:
            users_who_have_liked = product.likes.all()
            users_who_have_disliked = product.dislikes.all()
            product_interaction_count = product.likes.all().count() +\
                product.dislikes.all().count()
            for user in users_who_have_liked:
                sum_user_similarity_indices_of_likes += get_similarity_index(request.user, user)
            for user in users_who_have_disliked:
                sum_user_similarity_indices_of_dislikes += get_similarity_index(request.user, user)
            try:
                product_possibility_coefficient_index = (sum_user_similarity_indices_of_likes - sum_user_similarity_indices_of_dislikes) / product_interaction_count
            except ZeroDivisionError:
                product_possibility_coefficient_index = 0
                pass
            if product_possibility_coefficient_index > .25:
                possible_recommendations.append(product)

    if my_product_list:
        return render(request, template_name, 
            {'product_dict_list': my_product_list})
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

    divisor = len(user_one_likes.union(user_two_likes, user_one_dislikes, user_two_dislikes))
    print('divisor', divisor)
    dividend =  users_likes_intersection + users_dislikes_intersection - user_one_like_user_two_dislike_intersection - user_two_likes_user_one_dislikes_intersection
    print('dividend', dividend)
    user_similarity_index = dividend/divisor
    print('user_similarity_index', user_similarity_index)
    print('user_one', user_one)
    print('user_two', user_two)
    return user_similarity_index













