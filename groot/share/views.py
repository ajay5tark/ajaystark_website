from django.shortcuts import render
from django.views import generic
# Create your views here.

class sharepage(generic.View):
	template='share.html'
	def get(self,request):
		return render(request,self.template)
