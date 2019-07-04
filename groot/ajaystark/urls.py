from django.urls import path
from ajaystark.views import homepage
urlpatterns = [
	path('',homepage.as_view(),name='home')
]