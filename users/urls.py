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
	path('employee-messages/<int:pk>/', EmployeeMessagesView.as_view(), name="employer_messages"),
	path('employee-display-messages/<int:pk>/', EmployeeDisplayMessages.as_view(), name="employee_display_messages"),
	path('add-wishlist/<int:pk>/', AddWishListView.as_view(), name="add-wishlist"),
	path('remove-from-wishlist/<int:pk>/', RemoveFromWishListView.as_view(), name="remove_from_wishlist"),


]