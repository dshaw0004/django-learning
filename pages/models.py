from django.db import models

# Create your models here.
class Note(models.Model):
    """
        A simple model to store a text note.
    """
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set on creation

    def __str__(self):
        """String representation of the Note object."""
        # Limit the text length for display
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
