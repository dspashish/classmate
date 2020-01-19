from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from .models import ShowSubClass
# Create your views here.
def select(request):
    return render(request, template_name="select.html")

def home(request):
   
    user = get_object_or_404(User, username=request.user)
    data = ShowSubClass.objects.filter(author=user)
    context = {"data": data}
    return render(request, template_name="home.html", context=context)

def Create(request):
    if request.method == "POST":
        std = request.POST["std"]
        sub = request.POST["sub"]
        user = request.user
        c = ShowSubClass(std=std, Subject=sub, author=user)
        c.save()
        return redirect('home')

    else:    

        return render(request, template_name="create.html")
        