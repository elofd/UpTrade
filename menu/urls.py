from django.urls import path
from .views import menu_redirect_view


app_name = 'menu'


urlpatterns = [
    path('int:item_id/', menu_redirect_view, name='menu_redirect')
]