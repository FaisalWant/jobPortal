from django.views.generic import TemplateView, ListView, CreateView

# Create your views here.
from .models import Job, Category
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
class HomeView(ListView):
	template_name='jobs/index.html'
	context_object_name='jobs'
	model=Job
	paginate_by=2

	# for additional context
	def get_context_data(self, **kwargs):
		context= super(HomeView,self).get_context_data(**kwargs)
		context['categories']=Category.objects.all()
		return context

class CreateJobView(SuccessMessageMixin, CreateView ):
	model= Job
	template_name= 'jobs/create-jobs.html'
	form_class=CreateJobForm
	success_url = '/job'
	success_message="Job has been posted"
