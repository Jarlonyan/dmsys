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

	import random
	import django
	import datetime
	import matplotlib.pyplot as plt

	plt.figure(1)
	x=[]
	y=[]
	now=datetime.datetime.now()
	delta=datetime.timedelta(days=1)
	for i in range(10):
		x.append(now)
		now+=delta
		y.append(random.randint(0, 1000))
	plt.plot(x, y, '-')
	plt.savefig('static/media/test.png')
	plt.clf()
	plt.close()

	return render(request, 'index.html', {'image': "/static/media/test.png"})   #
