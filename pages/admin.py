from django.contrib import admin
from .models import Note # Import your Note model

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    """
    Customizes how the Note model is displayed and managed in the admin.
    """
    list_display = ('text_summary', 'created_at', 'id') # Fields to show in the list view
    list_filter = ('created_at',)                      # Fields to filter by in the sidebar
    search_fields = ('text',)                          # Fields to search through
    ordering = ('-created_at',)                        # Default ordering

    def text_summary(self, obj):
        """Returns a short summary of the note's text."""
        if len(obj.text) > 70:
            return f"{obj.text[:70]}..."
        return obj.text
    text_summary.short_description = 'Note Summary' # Column header for this custom method


admin.site.register(Note, NoteAdmin) # Register Note model with its custom admin options
# If you don't need custom options, you can simply do:
# admin.site.register(Note)
