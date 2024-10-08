from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import context, loader
from .models import Agent


def agent_profile_view(request):
    agent = Agent.objects.first()  # Assuming you have an Agent object
    template = loader.get_template('agent/agentprofile.html')
    context = {
        'agent': agent,
               }
    #return render(request, 'agentprofile.html', {'agent': agent})
    return HttpResponse(template.render(context, request))
