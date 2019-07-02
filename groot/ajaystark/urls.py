from django.urls import path
from ajaystark import views
urlpatterns = [
	path('',views.homepage.as_view(),name='home')
]