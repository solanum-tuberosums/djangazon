from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^product-categories$', views.list_product_categories, name='list_product_categories'),
    url(r'^products/(?P<question_id>[0-9]+)/$', views.product_detail, name="product_detail")
]