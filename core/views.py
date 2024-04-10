from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import Service


class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.mail()
        messages.success(self.request, 'E-mail successfully sent')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error sending message')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)