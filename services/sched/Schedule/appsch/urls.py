from django.urls import path
from . import views

app_name = 'appsch'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('login/', views.AuthPage.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('userpage/<str:account>', views.UserPage.as_view(), name='userpage'),
    path('Mypage', views.Mypage.as_view(), name='mypage'),
    path('Mypage/edit', views.UserPageEdit.as_view(), name='edit_profile'),
    path('lessons/', views.MyLessons.as_view(), name='mylessons'),
    path('deletelesson/<int:idlesson>', views.acceptLesson.as_view(), name='deletelesson'),
    path('acceptlesson/<int:idlesson>', views.acceptLesson.as_view(), name='acceptlesson'),

]
