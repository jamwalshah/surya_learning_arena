from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from courseApp.models import Course
from django.urls import reverse_lazy, reverse

# Create your views here.
class CourseListView(ListView):
    """ListView definition for view to list out the courses from Course Model.\
    This view retrieves and displays a list of Course Model objects, using a response rendered \
    by the default template

    Attributes:
        model (Course): The Model associated with this view, representing the Course objects to be listed
        template_name (str): The name of the template to be used for rendering the list. \
            Defaults to 'courseApp/templates/courseApp/course_list.html'
        context_object_name (str): The context variable name for the list of Course Objects. \
            Defaults to 'course_list'
    
    Inherits from:
        ListView: A base class to render some list of objects.
    """
    model = Course
    # template_name = "course_list.html"
    # context_object_name = 'course_list'

class CourseDetailView(DetailView):
    """DetailView definition for view to display details for Course Model object. \
    This view retrieves and presents the details of a specific Course Model object. \
    The response is rendered using the default template

    Attributes:
        model (Course): The model associated with this view, representing the Course Model \
            object to be displayed
        template_name (str): The name of the template used to render the Detail view. \
            Defaults to 'courseApp/templates/courseApp/course_detail.html'
        context_object_name (str): THe context variable name for the Course object. \
            Defaults to 'course'
    
    Inherits from:
        DetailView (class): A base class view for rendering a "detail" view of a Model Object.
    """
    model = Course
    # template_name = "course_detail.html"
    # context_object_name = 'course'

class CourseCreateView(CreateView):
    """CreateView definition for view to create a Course Model object.\
    This view handles the creation of a new Course object, with a response rendered \
    by the default template

    Attributes:
        model (Course): The Model associated with this view, representing the Course \
            object to be created
        fields (list): The fields of the course Model to be displayed in the Create Form.
        template_name (str): The name of template to be used for rendering the Create form.\
            Defaults to 'courseApp/templates/courseApp/course_form.html'
        context_object_name (str): The context variable name for the form. \
            Defaults to 'form'
    
    Inherits from:
        CreateView: A base class view for creating a new object, with a response rendered by \
            a template.
    
    Methods:
        get_context_data(self, **kwargs) -> dict: Returns the context data for the template, \
            overriding the base class function to add 'display_view_name' besides the other\
            context data, for displaying the Create operation at title and body.
        get_success_url(self) -> str: Overrides the default behavior of `CreateView` to return a \
            dynamic URL based on the primary key `pk` of the newly created Course instance.
    """
    model = Course
    fields = ('name', 'description', 'instructor', 'rating')
    # template_name = "course_form.html"
    # context_object_name = 'form'
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["display_view_name"] = 'Create'
        return context
    
    def get_success_url(self):
        return reverse(viewname='course_detail', kwargs={'pk': self.object.pk})

class CourseUpdateView(UpdateView):
    """UpdateView definition for view to update the Course Details from Course Model object. \
    This view handles the updating of a course object. Upon successful update, it redirects \
    to a specified success URL.

    Attributes:
        model (Course): The model associated with this view, representing the Course \
            object to be updated
        fields (list): The fields of the course Model to be displayed in the Update Form. \
            Defaults to '__all__' literal indicating all of the fields in Model.
        template_name (str): The name of the template to be used for rendering the Update form. \
            Defaults to 'courseApp/templates/courseApp/course_form.html'
        context_object_name (str): The context variable name for the form. \
            Defaults to 'form'.
    
    Inherits from:
        UpdateView: A base class view for updating an object, with a response rendered by \
            a template
    
    Methods:
        get_context_data(self, **kwargs) -> dict: Returns the context data for the template, \
            overriding the base class function to add 'display_view_name' besides the other \
            context data, for displaying the Update operation at title and body.
        get_success_url(self) -> str: Overrides the default behavior of `UpdateView` to return a \
            dynamic URL based on the primary key `pk` of the updated Course instance.
    """
    model = Course
    fields = '__all__'
    # template_name = "course_form.html"
    # context_object_name = 'form'
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["display_view_name"] = 'Update'
        return context
    
    def get_success_url(self):
        return reverse(viewname='course_detail', kwargs={'pk': self.object.pk})

class CourseDeleteView(DeleteView):
    """DeleteView definition for view to delete from Course Model. \
    This view handles the deletion of the Course object. Upon successful deletion, \
    it redirects to a specified success URL.

    Attributes:
        model (Course): The model associated with this view, representing the Course \
            object to be deleted
        success_url (str): The URL to redirect to after successful deletion. Recommended to \
            use `reverse_lazy(viewname)` to ensure proper URL resolution.
        template_name (str): The name of the template to be used to confirm deletion. \
            Defaults to 'courseApp/templates/courseApp/course_confirm_delete.html'
        context_object_name (str): The context variable name for the Model object to be deleted. \
            Defaults to 'course'
    
    Inherits from:
        DeleteView: A base class view for deleting a Course Model object, with a response \
            rendered by a template
    """
    model = Course
    success_url = reverse_lazy(viewname='course_list')
    # template_name = "course_confirm_delete.html"
    # context_object_name = 'course'
    