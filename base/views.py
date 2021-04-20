
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


class CustomLoginView(LoginView):
    template_name =  'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')


class RegisterView(CreateView):
    template_name = 'base/register.html'
    form_class = RegisterPageForm

    def get_success_url(self):
        return reverse_lazy('home')

class TaskView(LoginRequiredMixin,ListView):

    model = Task
    #by default django looking for task_list.html
    context_object_name = 'tasks'

    #USER SPECIFIC DATA
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains = search_input)

        context['search_input'] = search_input
        return context


class DetailTaskView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'base/detail_task.html'
    context_object_name = 'task'

class CreateTaskView(LoginRequiredMixin,CreateView):
    model = Task
    # template_name = 'base/create_task.html'
    fields = ('title', 'description', 'complete')
    #after creating task relocate to home
    success_url = reverse_lazy('home')

    #user specific data

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class UpdateTaskView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ('title', 'description', 'complete')
    template_name = 'base/update_task.html'
    success_url = reverse_lazy('home')
    # template_name = 'base/'

class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('home')
    # template_name = 'base/task_confirm_delete.html'
