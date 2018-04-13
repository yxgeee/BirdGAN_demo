# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
import random

texts = ["this small bird has a yellow crown and a white belly.",
		"this bird has a speckled belly and breast with a short pointy bill."]

def index(request):
	context = {}
	return render(request, 'base.html', context)

@csrf_exempt
def describe_text(request):
	text = request.POST.get('description')
	return_json = {'img0':'/static/results/0.png', 'img1':'/static/results/1.png',
					'img2':'/static/results/2.png', 'img3':'/static/results/3.png',
					'img4':'/static/results/4.png', 'img5':'/static/results/5.png'}
	return HttpResponse(json.dumps(return_json), content_type='application/json')

def random_text(request):
	return_json = {'text':random.choice(texts)}
	return HttpResponse(json.dumps(return_json), content_type='application/json')