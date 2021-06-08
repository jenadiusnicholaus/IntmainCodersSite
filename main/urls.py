from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('course', views.course, name='course'),
    path('course-details/<int:pk>/', views.CourseDetails.as_view(), name='course_details'),
    path('events', views.events, name='events'),
    path('trainers', views.trainers, name='trainers'),
    path('pricing', views.pricing, name='pricing'),
    path('bookforclass/', views.boolForClass, name='bookforclass'),

]
