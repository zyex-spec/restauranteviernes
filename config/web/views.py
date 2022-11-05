from django.shortcuts import render

# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def Platos(request):
    return render(request,'platos.html')