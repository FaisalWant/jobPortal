from django.urls import path
from .views import *

app_name= "users"


urlpatterns =[

	path('register', UserRegisterView.as_view(), name="register"),
	path('login/', UserLoginView.as_view(), name="login"),
	path('logout/', UserLogoutView.as_view(), name="logout"),
	path('update-profile/<int:pk>/', UserUpdateView.as_view(), name="update_profile"),
	path('employee-profile/<int:employee_id>/<int:job_id>/', EmployeeProfileView.as_view(), name="employee_profile"),
	path('employer-jobs/', EmployerPostedJobsView.as_view(), name="employer_jobs"),
	path('employee-messages/<int:employee_id>/', EmployeeMessagesView.as_view(), name="employer_messages"),



]