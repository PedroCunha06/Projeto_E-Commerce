from django.urls import path
from request import views

app_name = 'request'

# as.view(), quando se usa Class
urlpatterns = [
    path('pay/', views.Pay.as_view(), name='pay'),
    path('closeorder/', views.CloseOrder.as_view(), name='close_order' ),
    path('detail/<int:request_id>', views.Detail.as_view(), name='detail'),
    
]