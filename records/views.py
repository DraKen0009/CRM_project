from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from .models import Record
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

# def home(request):
#     return render(request,'records/home.html')

class RecordListView(LoginRequiredMixin,ListView):
    model = Record
    template_name = 'records/home.html'
    paginate_by = 20

    def get_queryset(self):
        user=self.request.user
        return Record.objects.filter(user=user)


class RecordCreateView(LoginRequiredMixin,CreateView):
    model = Record
    fields = ['name','email','country']

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class RecordUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Record
    fields = ['name', 'email', 'country']
    template_name = 'records/record_update_form.html'

    def test_func(self):
        record=self.get_object()
        if record.user==self.request.user:
            return True

        return False


class RecordDeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Record
    success_url ="/"
    def test_func(self):
        record=self.get_object()
        if record.user==self.request.user:
            return True

        return False

class RecordDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Record
    template_name = 'records/record_detail.html'
    def test_func(self):
        record=self.get_object()
        if record.user==self.request.user:
            return True

        return False