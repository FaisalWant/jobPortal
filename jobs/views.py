from django.views.generic import TemplateView, ListView

# Create your views here.
from .models import Job


class HomeView(ListView):
	template_name='jobs/index.html'
	context_object_name='jobs'
	model=Job
