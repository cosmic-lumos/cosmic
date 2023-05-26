from django.http import HttpResponse
from django.shortcuts import render, redirect

from project.forms import ProjectForm
from project.models import Project


def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect(f'/projects/{project.pk}/')
    else:
        form = ProjectForm()

    return render(request, 'forms/project_form.html', {
        'form': form,
    })


def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        return render(request, 'projects/project.html', {
            'projects': projects,
        })
    else:
        return HttpResponse(status=404)


def project_detail(request, pk):
    if request.method == 'GET':
        project = Project.objects.get(pk=pk)

        return render(request, 'projects/project_detail.html', {
            'project': project
        })


def project_delete(request, pk):
    if request.method == 'GET':
        return render(request, 'forms/project_delete_form.html')
    elif request.method == 'POST':
        project = Project.objects.get(pk=pk)

        project.delete()
        return redirect('/projects/')
    else:
        return HttpResponse(status=404)
