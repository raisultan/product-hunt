from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.create_product, name="create_product"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('<int:product_id>/upvote/', views.upvote_product, name="upvote_product"),
]