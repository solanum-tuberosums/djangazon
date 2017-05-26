from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^paymenttype$', views.payment_type_view.add_payment_type, name='payment_type'),
    url(r'^paymenttype/delete/(?P<payment_type_id>[0-9]+)/$', views.delete_payment_type, name="delete_payment_type"),

    url(r'^products$', views.list_products, name='list_products'),
    url(r'^my-account/(?P<user_id>[0-9]+)/$', views.my_account, name='my_account'),
    url(r'^my-products/(?P<user_id>[0-9]+)/$', views.list_my_products, name='my_products'),    
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product_detail, name="product_detail"),
    url(r'^product-categories/(?P<category_id>[0-9]+)/$', views.product_category_detail, name="product_category_detail"),
    url(r'^product-categories$', views.list_product_categories, name='list_product_categories'),
    url(r'^completeorder$', views.complete_order, name='complete_order'),
    url(r'^order/(?P<order_id>[0-9]+)/$', views.order_detail, name="order_detail"), 
    url(r'^order/deleteproduct/(?P<product_id>[0-9]+)/(?P<order_id>[0-9]+)$', views.order_detail_view.delete_product_from_order, name="delete_product_from_order"), 
    url(r'^order/$', views.no_order, name='no_order'),
    url(r'^deleteorder/$', views.delete_order, name='delete_order')
    
]