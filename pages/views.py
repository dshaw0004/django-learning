import datetime
from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    """
    A view that renders the home page template.
    and passes dynamic data via context.
    """
    template_name = "pages/home.html"
    # create some dynamic data
    current_time = datetime.datetime.now()
    user_name = "Student"
    cource_list = ["Python", "Django", "CSS", "HTML"]
    logged_in = True

    # Build the context dictionary
    context = {
        "current_datetime": current_time,
        "name": user_name,
        "courses": cource_list,
        "is_logged_in": logged_in,
        'info': {
            'project': 'Django Learning',
            'lesson': 5
        },
    }
    return render(request, template_name, context)
