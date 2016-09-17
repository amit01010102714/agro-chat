from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostForm
from django.contrib import messages

def contact(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = { "form": form,}
	return render(request,"contact.html",context)
