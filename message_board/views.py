from django.shortcuts import render
from .models import Message
from django.views.generic import ListView
# Create your views here.

class messageListView(ListView):
    model = Message
    template_name = 'message_list.html'