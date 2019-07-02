from django.shortcuts import render
from django.views import generic
# Create your views here.

class homepage(generic.View):
	template='/templates/index.html'
	def get(self,request):
		return render(request,self.template)
