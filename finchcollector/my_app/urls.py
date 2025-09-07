from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_index, name='finch_index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='finch_detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch-update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch-delete'),
]
