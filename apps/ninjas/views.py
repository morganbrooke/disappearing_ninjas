from django.http import HttpResponse, Http404
from django.shortcuts import render
def index(request):
	return render(request, 'ninjas/index.html')
def show(request, color):
	if color.lower() == 'ninja':
		context = {'imgsrc': 'tmnt.png',}
	if color.lower() == 'red':
		context = {'imgsrc': 'raphael.jpg',}
	if color.lower() == 'blue':
		context = {'imgsrc': 'leonardo.jpg',}
	if color.lower() == 'orange':
		context = {'imgsrc': 'michaelangelo.jpg',}
	if color.lower() == 'purple':
		context = {'imgsrc': 'donatello.jpg',}
	else:
		context = {'imgsrc': 'meganfox.jpg',}
	return render(request, 'ninjas/ninja.html', context)
# Create your views here.
