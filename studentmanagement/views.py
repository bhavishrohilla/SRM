from django.shortcuts import render
from studentmanagement.models import Student
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# def Home(request):
#     return render(request,'Student/dashboard.html')

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'Student/dashboard.html'

