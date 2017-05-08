#coding:utf-8

from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import forms
from myapp import models

# Create your views here.
'''----------------------------------主页------------------------------------------'''

class IndexUploadFileForm(forms.Form):
	title=forms.CharField()
	file=forms.FileField()

def handle_upload_file(f):
	with open("uploaddata/test.png","wb") as dest:
		for chunk in f.chunks():
			dest.write(chunk)

def read_file():
	return 0

def index(request):
	if request.method=="POST":
		form=IndexUploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			print (request.FILES['title'],">>>>>")
			#print (">>>>>>>>>>> 文件 ", request.FILES['filename'].name , " 上传成功!!")
			handle_upload_file(request.FILES['file'])
			return HttpResponseRedirect('/success/url/')
		else:
			form=IndexUploadFileForm()
			return render(request,'index.html',{'uf':form})
	else:
		form=IndexUploadFileForm()

	return render(request,'index.html',{'uf':form})   #


def classification(request):
	return render(request, 'classification.html')