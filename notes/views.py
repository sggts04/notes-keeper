from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from .models import Note

def index(request):
    return render(request, 'notes/index.html')

@login_required
def new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.author = request.user
            stock.save()
            messages.success(request, f'New Note Created!')
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'notes/new.html', {'form': form})

def view(request, note_id):
    obj = Note.objects.get(id=note_id)
    if request.user == obj.author:
        return render(request, 'notes/view.html', {'note': obj, 'read_only': False})
    elif obj.is_public:
        return render(request, 'notes/view.html', {'note': obj, 'read_only': True})
    return redirect('index')

@login_required
def edit(request, note_id):
    obj = Note.objects.get(id=note_id)
    if request.user == obj.author:
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=obj)
            if form.is_valid():
                stock = form.save(commit=False)
                stock.author = request.user
                stock.save()
                messages.success(request, f'Note Edited!')
                return redirect('index')
        else:
            form = NoteForm(instance=obj)
        return render(request, 'notes/edit.html', {'form': form})
    return redirect('index')

@login_required
def delete(request, note_id):
    obj = Note.objects.get(id=note_id)
    if request.user == obj.author:
        Note.objects.filter(id=note_id).delete()
    return redirect('index')