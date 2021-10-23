from django.urls import path
from clothingCoordination import views

app_name = 'clothing'
urlpatterns = [
  path('test/', views.test, name='test'),
  path('signup/', views.SignUp.as_view(), name='signup'),
]