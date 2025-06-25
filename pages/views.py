from django.shortcuts import render, redirect, get_object_or_404 # Add get_object_or_404
from django.utils import timezone
import datetime
from .models import Note
from .forms import NoteForm

# ... home_page_view remains the same ...
def home_page_view(request):
    # (Existing code for home_page_view)
    template_name = "pages/home.html"
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home') # Updated to use namespace
    else:
        form = NoteForm()

    all_notes = Note.objects.all().order_by('-created_at')
    current_time = datetime.datetime.now()
    user_name = "Student"
    course_list = ["Python", "HTML", "Django", "CSS"]
    logged_in = True
    info = {
        'project': 'Django Learning',
        'lesson': 10 # Updated lesson number
    }
    context = {
        'form': form,
        'notes_list': all_notes,
        'current_datetime': current_time,
        'name': user_name,
        'courses': course_list,
        'is_logged_in': logged_in,
        'info': info,
    }
    return render(request, template_name, context)


# NEW VIEW for About Page
def about_page_view(request):
    """
    A simple view for the About Us page.
    """
    template_name = "pages/about.html" # We'll create this template next
    context = {
        'page_title': 'About Our Awesome Site',
        'contact_email': 'info@awesomesite.com',
    }
    return render(request, template_name, context)

# NEW VIEW for Note Detail Page
def note_detail_view(request, note_id):
    """
    Displays the details of a single note.
    """
    # Attempt to get the note with the given id.
    # If not found, it will automatically raise a 404 error.
    note = get_object_or_404(Note, pk=note_id)

    template_name = "pages/note_detail.html" # We'll create this template
    context = {
        'note': note, # Pass the single note object to the template
    }
    return render(request, template_name, context)


