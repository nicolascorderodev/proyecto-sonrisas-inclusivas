from django.shortcuts import render, redirect
from .forms import ContactoForm
#API
from rest_framework import generics
from .models import Contacto
from .serializers import ContactoSerializer

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = ContactoForm()
    return render(request, 'contacto/contacto.html', {'form': form})

def gracias_view(request):
    return render(request, 'contacto/gracias.html')

# API
class ContactoListCreate(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class ContactoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
