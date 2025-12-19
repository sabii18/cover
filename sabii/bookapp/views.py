from django.shortcuts import render
def bookapp(request):
    return render(request,'book.html')