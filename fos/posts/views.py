from urllib import quote_plus
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect,Http404
from .forms import PostForm
from django.contrib import messages

from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.

def post_home(request):
	return HttpResponse("<h1>delete</h1>")

def post_list(request):
	queryset_list = Post.objects.all()
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
    # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {"object_list":queryset,}
	return render(request,"post_list.html",context)

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		context = {}
		return render(request,"sorry2.html",context)

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = { "form": form,}
	return render(request,"post_form.html",context)


def post_detail(request,slug=None):
	# instance = Post.objects.get(id=3)
	instance = get_object_or_404(Post,slug=slug)
	share_string = quote_plus(instance.content)
	context={"title":"Detail","instance":instance,"share_string":share_string,}

	return render(request,"post_detail.html",context)

def post_delete(request,slug=None):
	if not request.user.is_superuser:
		context = {}
		return render(request,"sorry.html",context)

	instance = get_object_or_404(Post,slug=slug)
	messages.success(request,"deleted")
	instance.delete()
	return redirect("list")

def post_update(request, slug):
	if not request.user.is_superuser:
		context = {}
		return render(request,"sorry1.html",context)
	instance = get_object_or_404(Post,slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"saved", extra_tags='some-tag')
		return HttpResponseRedirect(instance.get_absolute_url())
	context={"title":"Detail",
	"instance":instance,"form":form,}
	return render(request,"post_form.html",context)