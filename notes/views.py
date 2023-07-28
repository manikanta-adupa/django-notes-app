from typing import Any
# from django.db.models.query import QuerySet
# from django.forms.models import BaseModelForm
# from django.shortcuts import render
# from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/notes'
    template_name = 'notes/notes_delete.html'
    
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/notes/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/all_notes.html"
    login_url = "/login"
    
    def get_queryset(self):
        return  self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_details.html'

# def list(request):  
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/all_notes.html', {'notes': all_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_details.html', {'note': note})