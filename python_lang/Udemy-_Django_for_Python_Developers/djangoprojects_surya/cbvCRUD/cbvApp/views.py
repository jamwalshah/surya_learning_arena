from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from cbvApp.models import Student

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
    model = Student
    fields = ('firstName', 'lastName', 'testScore')
    # template_name = 'student_form.html'
    # default template_name is student_form.html
    # context_object_name = 'form'
    # default context_object_name is form
