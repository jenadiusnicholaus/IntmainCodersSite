from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('course-details/<int:pk>/', views.CourseDetails.as_view(), name='course_details'),
    path('dayclasslist/', views.dayClassList, name='dayclasslist'),
    path('make_booking/', views.boolForClass, name='make_booking'),
    path('news/', views.news, name='news'),
    path('news_details/', views.news_details, name='news_details'),
    path('test_ajax/', views.test_ajax, name='test_ajax'),


]
