from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Category
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import TaskForm, CategoryForm


from django.template import RequestContext

# def home(request):
#     return render(request, 'home.html', {})
cat_url = ''
cat_name = ''


def delete(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    messages.success(request, ('Task has been deleted!'))
    return redirect(cat_url)


def deleteCat(request, pk):
    item = Category.objects.get(id=pk)
    item.delete()
    return redirect('home')


def tocross(request, pk):
    item = Task.objects.get(id=pk)
    item.completed = True
    item.save()
    return redirect(cat_url)


def uncross(request, pk):
    item = Task.objects.get(id=pk)
    item.completed = False
    item.save()

    return redirect(cat_url)


def CategoryView(request, categ):
    category_tasks = Task.objects.filter(category=categ.replace('-', ' '))

    # print(cat_url)
    listOfGlobals = globals()
    listOfGlobals['cat_url'] = request.get_full_path()
    return render(request, 'categories.html', {'categ': categ, 'category_tasks': category_tasks})


class HomeView(ListView):
    model = Task
    template_name = 'home.html'
    ordering = ['task_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm

    template_name = 'add_task.html'

    # fields = ('title')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm

    template_name = 'add_category.html'
    # fields = '__all__'


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    # fields = ('title', 'body')


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('cat_url')  # return home after deleting


class DeleteTest(DeleteView):
    model = Task
    template_name = 'cat_url'
