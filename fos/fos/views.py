from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from posts.models import Post

# Create your views here

def home(request):
	queryset_list = Post.objects.all()
	context = {"object_list":queryset_list,}
	return render(request,"index.html",context)

def about(request):
	context = {}
	return render(request,"about.html",context)
