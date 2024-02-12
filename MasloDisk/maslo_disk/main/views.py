from django.shortcuts import render, redirect
from .models import Document1
from .forms import Document1Form, CreateUserForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

import mimetypes
import os

# Create your views here.

class NewsDetailView(DetailView):
    model = Document1
    template_name = 'main/document_details.html'
    context_object_name = 'document'



def index(request):
    files = Document1.objects.order_by('-created_at')
    return render(request, 'main/index.html', {'files': files})
def about(request):
    return render(request, 'main/about.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def login(request):
    return render(request, 'main/login.html')

def registration(request):

    form = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')

            messages.success(request, 'Поздравляем, ' + user + '! Вы успешно создали аккаунт')
            return redirect('login')

    context = {'form': form}
    return render(request, 'main/registration.html', context)

def add(request):
    error = ''
    errorF = ''

    if request.method == 'POST':

        form = Document1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
            for field in form:
                errorF = field.name
                error = field.errors

    form = Document1Form()

    data = {
        'form': form,
        'error': error,
        'errorF': errorF,
    }
    return render(request, 'main/add.html', data)

def deleteDocument(request, id):
    selectedDocument = Document1.objects.get(id=id)
    selectedDocument.delete()
    return redirect('/')


# def download_file(request):
#     # fill these variables with real values
#     fl_path = '/'
#     filename = '3V9A1049.JPG'
#
#     fl = open(fl_path, 'r')
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#
#     return response




# вспомогательные функции
# def get_file_extension(filename):
#     return os.path.splitext(filename)[1]
#
# def print_file_extension(file):
#     print(get_file_extension(file))



