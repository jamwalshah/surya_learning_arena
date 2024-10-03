from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
