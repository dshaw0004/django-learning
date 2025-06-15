from django.shortcuts import render, redirect # Add redirect
from django.utils import timezone # For explicit created_at if not using auto_now_add fully
import datetime
from .models import Note
from .forms import NoteForm # <--- IMPORT YOUR FORM

def home_page_view(request):
    template_name = "pages/home.html"

    # --- Form Handling ---
    if request.method == 'POST':
        form = NoteForm(request.POST) # Create form instance with submitted data
        if form.is_valid():
            # If you want to set created_at manually (e.g., if auto_now_add=False or for custom logic)
            # new_note = form.save(commit=False) # Don't save to DB yet
            # new_note.created_at = timezone.now() # Set additional fields
            # new_note.save() # Now save to DB

            # Since our 'created_at' has auto_now_add=True, we can just save directly
            form.save() # Saves the new note to the database
            return redirect('home') # Redirect to the same page (or another) to avoid re-POSTing
    else: # GET request
        form = NoteForm() # Create an empty form instance

    # --- Fetching existing data ---
    all_notes = Note.objects.all().order_by('-created_at')

    # --- Old dynamic data (can be kept or removed) ---
    current_time = datetime.datetime.now()
    user_name = "Student"
    course_list = ["Python", "HTML", "Django", "CSS"]
    logged_in = True
    info = {
        'project': 'Django Learning',
        'lesson': 8 # Updated lesson number
    }

    context = {
        'form': form, # <--- ADD THE FORM TO THE CONTEXT
        'notes_list': all_notes,
        'current_datetime': current_time,
        'name': user_name,
        'courses': course_list,
        'is_logged_in': logged_in,
        'info': info,
    }
    return render(request, template_name, context)
