from django.shortcuts import render

# Create your views here.
def video(request):
    d={'name':'zoom'}
    return render(request,'video.html',context=d)
