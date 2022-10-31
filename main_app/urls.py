from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/', views.games_index, name='games_index'),
    path('games/<int:game_id>/', views.games_detail, name='games_detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
]
