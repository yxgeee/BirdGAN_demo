# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render

# from blog.models import Post


# def hello(request):
# 	return HttpResponse("Helldcdo world ! ")

def index(request):
	context = {}
	return render(request, 'base.html', context)
	# posts = Post.objects.all()
    # return render_to_response("blog/index.html", {"posts": posts}, context_instance=RequestContext(request))

