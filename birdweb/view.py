# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from gan import gan

import json
import random
import os,sys

texts = ["the bird is small with a pointed bill, has black eyes, and a yellow crown.",
		"this particular bird has a gray belly breast and sides and a greenish yellow strip on its back",
		"this bird has wings that are grey and has a yellow body"]

def index(request):
	context = {}
	return render(request, 'base.html', context)

@csrf_exempt
def describe_text(request):
	text = request.POST['description']
	return_code = gan(text)
	if return_code==0:
		response = JsonResponse({"error": "The description cannot be empty."})
		response.status_code = 403 # To announce that the user isn't allowed to publish
		return response

	return_json = {'img0':'/static/results/gan_0.png', 'img1':'/static/results/gan_1.png',
					'img2':'/static/results/gan_2.png', 'img3':'/static/results/gan_3.png',
					'img4':'/static/results/gan_4.png', 'img5':'/static/results/gan_5.png'}
	return HttpResponse(json.dumps(return_json), content_type='application/json')

@csrf_exempt
def random_text(request):
	text = request.POST['description']
	texts1 = list(texts)
	if text in texts1:
		texts1.remove(text)
	return_json = {'text':random.choice(texts1)}
	return HttpResponse(json.dumps(return_json), content_type='application/json')