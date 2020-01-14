from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),

    path('<username>/', views.ProfileDashboard, name='dashboard'),
    # path('<username>/edit_student_profile', views.EditStudentProfileView, name='edit_student_profile'),

]
