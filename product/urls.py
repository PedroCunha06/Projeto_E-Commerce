from django.urls import path
from product import views

app_name = 'product'

# as.view(), quando se usa Class
urlpatterns = [
    path('', views.ListProduct.as_view(), name='list'),
    path('<slug>/', views.DetailsProduct.as_view(), name='detail' ),
    path('addtocart/', views.AddToCart.as_view(), name='add_cart'),
    path('removetocart/', views.RemoveToCart.as_view(), name='remove_cart'),
    path('finish', views.Finish.as_view(), name='finish'),
    
]
