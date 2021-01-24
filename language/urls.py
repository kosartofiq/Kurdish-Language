from django.urls import path
from . import views


urlpatterns = [
    # language
    path('', views.LanguageListView.as_view(), name='language-list'),
    path('new/', views.LanguageCreateView.as_view(), name='language-create'),
    path('<int:pk>/', views.LanguageDetailView.as_view(), name='language-detail'),
    path('<int:pk>/histories/', views.language_histories, name='language-histories'),
    path('<int:pk>/update', views.LanguageUpdateView.as_view(), name='language-update'),

    # dialect
    path('<int:language_pk>/dialects/', views.dialect_list_view, name='dialect-list'),
    path('<int:language_pk>/dialect/<int:dialect_pk>/new/', views.dialect_create_view, name='dialect-create'),
    path('<int:language_pk>/dialect/<int:dialect_pk>/detail', views.dialect_detail_view, name='dialect-detail'),
    path('dialect/<int:dialect_pk>/histories/', views.dialect_histories, name='dialect-histories'),
    path('<int:language_pk>/dialect/<int:dialect_pk>/update', views.dialect_update_view, name='dialect-update'),

]