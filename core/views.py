from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Work,Offer,Comment,Info,Certificate,Qualitie






def index(request):
    info = Info.objects.last()
    offers = Offer.objects.all()
    comments = Comment.objects.all()
    certificates = Certificate.objects.all()
    qualities = Qualitie.objects.all()
    context = {
        'offers':offers,
        'comments':comments,
        'info':info,
        'certificates':certificates,
        'qualities':qualities,
        }
    return render(request,"core/index.html",context)


def services(request):
    comments = Comment.objects.all()
    offers = Offer.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'offers':offers,
        'comments':comments,
        'certificates':certificates,
        }
    return render (request,"core/services.html",context)


def work(request):
    works = Work.objects.all()
    context = {'works':works,}
    return render (request,"core/work.html",context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for contacting me, I will reply to you as soon as possible.')
            return redirect('contact')
    context = {'form':form,}
    return render (request,"core/contact.html",context)

