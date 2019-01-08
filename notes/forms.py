from django import forms
from .models import Note
from ckeditor.widgets import CKEditorWidget

class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    is_public = forms.BooleanField(initial=False, required=False, label="Is a Public Note", help_text="If ticked, people with the correct link can view this note(read only).")
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note
        fields = ['title', 'is_public', 'content']