from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm, RawPersonaForm
# Create your views here.
def personaTestView(request):
    obj=Persona.objects.get(id=1)
    context={
        "objeto":obj
    }
    return render(request, "personas/descripcion.html", context)

def personaCreateView(request):
    initialValues={
        "nombres":"Sin nombre",
        "donador":True
    }
    form=PersonaForm(request.POST or None, initial=initialValues)
    if form.is_valid():
        form.save()
        form=PersonaForm()
    context={
        "form":form
        }
    return render(request, "personas/personaCreate.html", context)

def searchForHelp(request):
    return render(request, "personas/search.html",{}) 

def personasShowObject(request, myID):
    obj=Persona.objects.get(id=myID)
    context={
        "objeto":obj,
    }  
    return render(request, "personas/descripcion.html", context)

def personasAnotherCreateView(request):
    form=RawPersonaForm()#get
    if request.method=="POST":
        form=RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context={
        "form":form,
    }
    return render(request, "personas/personaCreate.html",context)
def personasListView(request):
    queryset= Persona.objects.all()
    context={
        "objectList":queryset,
    }
    return render(request, "personas/personasLista.html", context)