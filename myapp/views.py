from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

from .forms import FormNewTask, CreateNewProject

from django.shortcuts import get_object_or_404 # si no encuentra un objeto, muestra el error 404 en lugar de que caiga el server

# Create your views here.
def index(request):
    title = 'Curso Django!!'
    return render(request, 'index.html', {
        'title':title
        })

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s!</h1>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)

    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    #return JsonResponse('task: %s' % task.title, safe=False)

    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):

    if request.method == 'GET':
        # mostrar interfaz
        return render(request, 'tasks/create_task.html', {
            'form':FormNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)

        return redirect('tasks')
    
def create_project(request):

    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])

        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    tasks = Task.objects.filter(project_id=id)

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })