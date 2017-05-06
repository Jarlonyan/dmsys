#coding:utf-8

from django.shortcuts import render,render_to_response
import django.template #.context import RequestContext
from myapp import models

# Create your views here.
'''----------------------------------主页------------------------------------------'''
def index(request):
	# model_param={}
	# model_param['webname']="company公司网站"
	# return render_to_response('index.html')


	return render(request, 'index.html')   #
