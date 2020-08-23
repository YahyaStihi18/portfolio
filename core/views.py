from django.shortcuts import render,redirect
from .forms import ContactForm

def index(request):
    return render(request,"core/index.html")

def services(request):
    return render (request,"core/services.html")

def work(request):
    return render (request,"core/work.html")

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form,}
    return render (request,"core/contact.html",context)