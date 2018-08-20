from django.shortcuts import render

# Create your views here.

#template_test
def template_test(request):
    return render(request,'register.html')
