# projects/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm


def project_list(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('projects:project_list')
    else:
        form = ProjectForm()

    projects = Project.objects.filter(user=request.user).order_by('-created_at')
    context = {'projects': projects, 'form': form}
    return render(request, 'projects/projects_list.html', context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:project_list')
    return redirect('projects:project_list')


def edit_project(request, project_id):
    pass
