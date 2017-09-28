# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice, Photo
from .forms import PhotoForm, UploadFileForm


def ind(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('app1/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    path = request.path
    return render(request, 'index.html', locals())
    #return HttpResponse(template.render(context, request))
    
def photo(request):
    photo_list = Photo.objects.all()
    context = {'photo_list': photo_list}
    return render(request, 'app1/showphoto.html', context)

def new_photo(request):
    if request.method != 'POST':
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app1:photo'))
    context = {'form': form}
    return render(request, 'app1/new_showphoto.html', context)

def detail(request):
    question = Question.q.order_by('-pub_date')
    context = {'question': question}
    return render(request, 'app1/detail.html', context)
    #return HttpResponse("You're looking at question %s." % question_id)
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app1/results.html', {'question': question})
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app1/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app1:results', args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)