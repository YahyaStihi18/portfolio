from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Work,Offer,Comment,Info,Certificate,Qualitie,Skill
from taggit.models import Tag




def index(request):
    info = Info.objects.last()
    offers = Offer.objects.all()
    comments = Comment.objects.all()
    certificates = Certificate.objects.all()
    qualities = Qualitie.objects.all()
    skills = Skill.objects.all()
    context = {
        'offers':offers,
        'comments':comments,
        'info':info,
        'certificates':certificates,
        'qualities':qualities,
        'skills':skills,
        }
    return render(request,"core/index.html",context)


def services(request):
    info = Info.objects.last()
    comments = Comment.objects.all()
    offers = Offer.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'offers':offers,
        'comments':comments,
        'certificates':certificates,
        'info':info,
        }
    return render (request,"core/services.html",context)


def work(request):
    info = Info.objects.last()
    works = Work.objects.all()
    context = {'works':works,'info':info,}
    return render (request,"core/work.html",context)


def contact(request):
    info = Info.objects.last()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for contacting me, I will reply to you as soon as possible.')
            return redirect('contact')
    context = {'form':form,'info':info,}
    return render (request,"core/contact.html",context)

