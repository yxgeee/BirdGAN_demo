# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


# from blog.models import Post


# def hello(request):
# 	return HttpResponse("Helldcdo world ! ")

def index(request):
	context = {}
	return render(request, 'base.html', context)
	# posts = Post.objects.all()
    # return render_to_response("blog/index.html", {"posts": posts}, context_instance=RequestContext(request))

@csrf_exempt
def describe_text(request):
	text = request.POST.get('description')
	return_json = {'img0':'/static/results/0.png', 'img1':'/static/results/1.png',
					'img2':'/static/results/2.png', 'img3':'/static/results/3.png',
					'img4':'/static/results/4.png', 'img5':'/static/results/5.png'}
	return HttpResponse(json.dumps(return_json), content_type='application/json')

# def ajax_list(request):
#     a = range(100)
#     return JsonResponse(a, safe=False)
 
# def ajax_dict(request):
#     name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
#     return JsonResponse(name_dict)
