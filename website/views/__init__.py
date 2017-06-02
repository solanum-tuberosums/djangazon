"""
These modules represent the views for our bangazon website.
"""

from website.views.index_view import index
from website.views.list_products_view import list_products
from website.views.login_user_view import login_user
from website.views.register_view import register
from website.views.sell_product_view import sell_product
from website.views.user_logout_view import user_logout
from website.views.list_product_categories_view import list_product_categories
from website.views.payment_type_view import add_payment_type, delete_payment_type, edit_payment_type
from website.views.product_detail_view import product_detail
from website.views.order_detail_view import order_detail, delete_product_from_order
from website.views.no_order_view import no_order
from website.views.my_account_view import my_account
from website.views.edit_my_account_view import edit_my_account
from website.views.list_my_products_view import list_my_products
from website.views.product_category_detail_view import product_category_detail
from website.views.complete_order_view import complete_order
from website.views.delete_order_view import delete_order
from website.views.order_history_view import order_history
from website.views.search_product_view import search_products
from website.views.search_location_view import search_locations
from website.views.recommend_product_view import recommend_product
from website.views.recommendations_view import recommendations