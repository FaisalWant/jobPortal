from django.views.generic import TemplateView, ListView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Job, Category
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
from django.views.generic import DetailView
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



@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class CreateJobView(SuccessMessageMixin, CreateView ):
	model= Job
	template_name= 'jobs/create-jobs.html'
	form_class=CreateJobForm
	success_url = '/job'
	success_message="Job has been posted"

	def form_valid(self, form):
		job= form.save(commit=False)
		job.employer=self.request.user
		job.save()
		return super(CreateJobView,self).form_valid(form)


class SingleJobView(DetailView):
	template_name='jobs/single.html'
	model=Job
	context_object_name="job"

	def get_context_data(self, **kwargs):
		context= super(SingleJobView,self).get_context_data(**kwargs)
		context['categories']=Category.objects.all()
		return context

