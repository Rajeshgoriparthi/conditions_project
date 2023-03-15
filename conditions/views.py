from django.shortcuts import render

# Create your views here.
def conditions(request):
    dic={'x':20}
    return render (request,'conditions.html',context=dic)

def if_else(request):
    dict={'a':100,'b': 150}
    return render(request,'if_else.html',dict)

def if_elif(request):
    d={'A':200,'B':300,'C': 400}
    return render (request,'if_elif.html',d)