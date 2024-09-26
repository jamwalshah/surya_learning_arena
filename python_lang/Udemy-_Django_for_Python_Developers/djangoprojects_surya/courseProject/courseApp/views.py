from django.shortcuts import render, redirect
from courseApp.models import Course
from courseApp.forms import CourseForm

# Create your views here.
def getCourseView(request):
    """**Read** view for the courses to display on the template
    Args:
        request (HttpRequest): the Http Request generated when index page template is loaded
    Returns:
        HttpResponse: to render view on the template using the request received and data in Model object
    """
    courses = Course.objects.all()
    return render(request=request, template_name='courseApp/index.html', context={'courses': courses})

def createCourseView(request):
    """**Create** view for the courses, covers logic to add a new course
    Args:
        request (HttpRequest): the Http Request generated when Create Course form is loaded
    Returns:
        HttpResponse: to render view on the template using the request received and data from ModelForm object
    """
    createForm = CourseForm()
    if request.method == 'POST':
        dataCreateForm = CourseForm(data=request.POST)
        if dataCreateForm.is_valid():
            dataCreateForm.save()
            return redirect(to='/')
    return render(request=request, template_name='courseApp/create.html', context={'createForm':createForm})

def updateCourseView(request, id):
    """**Update** view for the courses, covers logic to update a course,\
        first obtains a Model instance based on id,\
        then obtains a ModelForm object with that Model instance,\
        then renders the update form with data from Model object,\
        if form data is found valid, data is committed\
        and redirected to homepage '/'
    Args:
        request (HttpRequest): the Http Request generated when Update Course form is loaded
        id (int): the id of the record later used to obtain the Model object to be updated
    Returns:
        HttpResponse: to render view on the template using the request received\
        and data from ModelForm object having data from Model object based on id
    """
    course = Course.objects.get(id=id)
    updateForm = CourseForm(instance=course)
    if request.method == 'POST':
        dataUpdateForm = CourseForm(data=request.POST, instance=course)
        if dataUpdateForm.is_valid():
            dataUpdateForm.save()
            return redirect(to='/')
    return render(request=request, template_name='courseApp/update.html', context={'updateForm':updateForm})

def deleteCourseView(_, id):
    """**Delete** view for the courses, covers logic to delete a course,\
        obtains a Model instance based on id,\
        then calls the `delete()` method on Model instance to delete it from the database.\
        redirects to the homepage '/'
    Args:
        request (HttpRequest): the Http Request generated when delete link is clicked
        id (int): the id of the record, later used to obtain the Model object to be deleted
    Returns:
        HttpResponseRedirect: redirects to the homepage '/'
    """
    course = Course.objects.get(id=id)
    course.delete()
    return redirect(to='/')
