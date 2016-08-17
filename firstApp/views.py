# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author: Alexander ATOMIC Miller
# Author last edited: Alexander ATOMIC Miller
# Name: views.py
# Description: ---

# import lib
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Question, Choice

# Create your views here
# Home applications
def index(request):
    """Home applications"""
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'firstApp/index.html', context)

# Get more information about the issue
def detail(request, question_id):
    """Get more information about the issue"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstApp/detail.html', {'question': question})

# Output voting results
def results(request, question_id):
    """Output voting results"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstApp/results.html', {'question': question})

# The voting process
def vote(request, question_id):
    """The voting process"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'firstApp/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('firstApp:results', args=(question.id,)))
