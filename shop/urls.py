from django.urls import path 
from .views import *
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
path('products/' , ProductView.as_view()),
path('favorit/' , FavoritView.as_view()), 
path('category/' , CategoryView.as_view()),
path('login/' , obtain_auth_token ),
path('register/' , RegisterView.as_view() ),
path('users/<int:id>/' , UserView.as_view() ),
path('user-profile/' , UserProfileView.as_view() ),
path('allorder/' , GetAllOrderView.as_view() ),
path('ordercreate/' , OrderCreateView.as_view() ),
path('orderbyuser/' , GetOrderByUserView.as_view() ),
path('review/' , ReviewView.as_view() ),
path('review-create/' , ReviewCreate.as_view() ),
]
