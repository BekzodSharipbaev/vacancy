from email.policy import default
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .forms import SearchForm
from .models import *

# Create your views here.

# FILTER_FIELDS = ''


class StartPageView(ListView):
    model = Vacancy
    template_name = 'vacancyapp/vacancy_list.html'
    form_class = SearchForm
    paginate_by = 5
    extra_context = {'title': 'Вакансии'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.queries)
        return context

    def get_queryset(self, *args, **kwargs):
        fields = self.form_class.declared_fields.keys()
        GET = self.request.GET
        self.queries = {k: GET.get(k) for k in fields if GET.get(k)}
        sch = self.queries.pop('search', '')
        queryset = self.model.objects.filter(
            Q(title__icontains=sch), **self.queries)
        self.queries['search'] = sch
        return queryset


class DetailPageView(DetailView):
    model = Vacancy
    template_name = 'vacancyapp/vacancy.html'
