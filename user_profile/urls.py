from django.urls import path
from user_profile import views

app_name = 'user_profile'

# as.view(), quando se usa Class
urlpatterns = [
    path('', views.Create.as_view(), name='register'),
    path('update/', views.Update.as_view(), name='user_update' ),
    path('addtocart/', views.Login.as_view(), name='login'),
    path('removetocart/', views.Logout.as_view(), name='logout'),

    
]