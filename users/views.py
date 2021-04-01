from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AccountRegisterForm, UserUpdateForm
from .models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class UserRegisterView(SuccessMessageMixin, CreateView):
	template_name= 'users/user-register.html'
	form_class=AccountRegisterForm
	success_url='/job'
	success_message="your user account has been created"


	def form_valid(self, form):
		user=form.save(commit=False)
		user_type= form.cleaned_data['user_types']

		if user_type == 'is_employee':
			user.is_employee=True

		elif user_type == 'is_employer':
			user.is_employer= True

		user.save()

		return redirect(self.success_url)	


class UserLoginView(LoginView):
	template_name='users/login.html'


class UserLogoutView(LogoutView):
	template_name='users/logout.html'

@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
	model= Profile
	success_message="You Updated Your Profile"
	template_name="users/update.html"
	form_class=UserUpdateForm


	def form_valid(self, form):
		form.instance.user= self.request.user
		return super(UserUpdateView, self).form_valid(form)


	def get(self, request, *args, **kwargs):
		self.object=self.get_object()
		if self.object.user!= request.user:
			return HttpResponseRedirect('/job')

		return super(UserUpdateView,self).get(request, *args, **kwargs)


	def get_success_url(self):
		return reverse('users:update_profile', kwargs={'pk':self.object.pk})



