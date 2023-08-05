from django.urls import path
from ProfileAdmin import views
from django.contrib.auth.views import LogoutView
from .views import LoginPage, PageRegister, UserEdition, ChangePassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', PageRegister.as_view(), name='register'),
    path('profileEdition/', UserEdition.as_view(), name='profileEdit'),
    path('changePassword/', ChangePassword.as_view(), name='changePassword'),
    path('passwordSucces/' , views.password_succes, name='passwordSucces'),
    
]