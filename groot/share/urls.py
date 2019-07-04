from django.urls import path
from share.views import sharepage
urlpatterns = [
	path('',sharepage.as_view(),name='sharepage')
]