from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Order


def students_list(request):
    template = 'school/students_list.html'
    ordering = Student.object.order_by('group')
    context = {'ordering': ordering}

    return render(request, template, context)