from django import forms
from .models import Note # Import your Note model

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note  # Specify which model this form is for
        fields = ['text'] # Specify which fields from the model should be in the form
        # You can also use fields = '__all__' to include all fields,
        # or exclude = ['created_at'] to exclude specific fields.

        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your note here...'}),
        }
        labels = {
            'text': 'Your Note',
        }
        help_texts = {
            'text': 'Write down what you want to remember.',
        }
