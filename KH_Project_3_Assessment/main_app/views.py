  
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Widget
from .forms import WidgetForm
# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, "widget_form" : widget_form})

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"

def delete_todo(request, id):
    Widget.objects.get(id=id).delete()
    return redirect('/')
