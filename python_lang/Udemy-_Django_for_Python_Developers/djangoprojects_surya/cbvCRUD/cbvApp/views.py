from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentListView(ListView):
    """ListView definition for view to list data from Student Model"""
    model = Student
    # template_name = 'student_list.html'
    # default template_name is student_list.html
    # context_object_name = 'student_list'
    # default context_object_name is student_list


class StudentDetailView(DetailView):
    """DetailView definition for view to display detail data from Student Model"""
    model = Student
    # template_name = 'student_detail.html'
    # default template_name is student_detail.html
    # context_object_name = 'student'
    # default context_object_name is student


class StudentCreateView(CreateView):
    """CreateView definition for view to create student from Student Model"""
    model = Student
    fields = ('firstName', 'lastName', 'testScore')
    # template_name = 'student_form.html'
    # default template_name is student_form.html
    # context_object_name = 'form'
    # default context_object_name is form

class StudentUpdateView(UpdateView):
    """UpdateView definition for view to update testScore from Student Model"""
    model = Student
    fields = ('testScore', )
    # template_name = ".html"
    # context_object_name = 'form'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy(viewname='students')
    # template_name = ".html"
    # context_object_name = 'student'
