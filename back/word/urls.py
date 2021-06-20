from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:foreign>/<int:txtlen>/', views.user_input),
    path('ai/<int:foreign>/<int:txtlen>/', views.ai_input),
    path('reset/', views.reset),
]
