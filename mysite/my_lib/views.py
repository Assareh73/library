from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Document

class IndexView(generic.ListView):
    template_name="my_lib/index.html"
    context_object_name= "books_list"

    def get_queryset(self):
        return Document.objects.all()

class DetailView(generic.DetailView):
    model = Document
    template_name = 'my_lib/document_detail.html'

class ResultsView(generic.DetailView):
    model = Document
    template_name = 'my_lib/document_results.html'

def vote(request, D_id):
    document = get_object_or_404(Document, pk=D_id)
    try:
        selected_choice = document.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'my_lib/detail.html', {
            'document': document,
            'error_message': "you didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('document:results', args=(document.id,)))