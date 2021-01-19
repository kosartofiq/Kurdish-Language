from django.urls import path
from . import views


urlpatterns = [
    path('', views.LanguageListView.as_view(), name='language-list'),
    path('new/', views.LanguageCreateView.as_view(), name='language-add'),
    path('<int:pk>/', views.LanguageDetailView.as_view(), name='language-detail'),
    # path('<int:pk>/update', views.LanguageUpdateView.as_view(), name='language-update'),


    # path('<int:pk>/dialect/', views.dialectListView, name='dialect'),
    # path('<int:pk1>/dialect/<int:pk2>/detail', views.dialectDetailView, name='dialect-detail'),
    # path('<int:pk1>/dialect/<int:pk2>/update', views.dialectUpdateView, name='dialect-update'),
    # path('<int:pk1>/dialect/<int:pk2>/new/', views.dialectCreateView, name='dialect-create'),

]