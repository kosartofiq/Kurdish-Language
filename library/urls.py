from django.urls import path
from . import views

urlpatterns = [
    # library
    path('', views.library, name='library'),
    #path('book/new/', views.BookCreateView.as_view(), name='book-create'),

    # genre
    path('genre/', views.GenreListView.as_view(), name='genre-list'),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genre/<int:pk>/histories/', views.genre_histories, name='genre-histories'),
    path('genre/new/', views.GenreCreateView.as_view(), name='genre-create'),
    path('genre/<int:pk>/update', views.GenreUpdateView.as_view(), name='genre-update'),

    # job
    path('job/', views.JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    path('job/<int:pk>/histories/', views.job_histories, name='job-histories'),
    path('job/new/', views.JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/update', views.JobUpdateView.as_view(), name='job-update'),

    # location
    path('location/', views.LocationListView.as_view(), name='location-list'),
    path('location/<int:pk>/', views.LocationDetailView.as_view(), name='location-detail'),
    path('location/<int:pk>/histories/', views.location_histories, name='location-histories'),
    path('location/new/', views.LocationCreateView.as_view(), name='location-create'),
    path('location/<int:pk>/update', views.LocationUpdateView.as_view(), name='location-update'),


    #path('publisher/', views.PublisherListView.as_view(), name='publisher'),
    #path('publisher/<int:pk>/', views.PublisherDetailView.as_view(), name='publisher-detail'),
    #path('publisher/<int:pk>/update', views.PublisherUpdateView.as_view(), name='publisher-update'),
    #path('publisher/new/', views.PublisherCreateView.as_view(), name='publisher-create'),

    #path('writer/', views.WriterListView.as_view(), name='writer'),
    #path('writer/<int:pk>/', views.WriterDetailView.as_view(), name='writer-detail'),
    #path('writer/<int:pk>/update', views.WriterUpdateView.as_view(), name='writer-update'),
    #path('writer/new/', views.WriterCreateView.as_view(), name='writer-create'),

]