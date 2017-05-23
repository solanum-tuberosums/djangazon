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
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product_detail, name="product_detail"),
    url(r'^product-categories/(?P<category_id>[0-9]+)/$', views.product_category_detail, name="product_category_detail"),
    url(r'^product-categories$', views.list_product_categories, name='list_product_categories'),
    url(r'^completeorder$', views.complete_order, name='complete_order'),
    url(r'^order/(?P<order_id>[0-9]+)/$', views.order_detail, name="order_detail"), 
    url(r'^order/$', views.no_order, name='no_order')


]