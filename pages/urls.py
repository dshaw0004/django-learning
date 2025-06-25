from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    # Example: /note/1/ or /note/42/
    path('note/<int:note_id>/', views.note_detail_view, name='note_detail'), # <--- ADD THIS
]
