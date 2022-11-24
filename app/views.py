from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':3000,'b':5432,'c'=4567}
    return render(request,'condition.html',context=d)
