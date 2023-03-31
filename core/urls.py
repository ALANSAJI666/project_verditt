from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),

    path('upload',views.upload,name = 'upload'),
    path('follow',views.follow,name = 'follow'),
    path('search',views.search,name = 'search'),
    path('profile/<str:pk>',views.profile,name = 'profile'),
    path('profile_firm/<str:pk>',views.profile_firm,name = 'profile_firm'),
    path('profile_statements/<str:pk>',views.profile_statements,name = 'profile_statements'),
    path('profile_statements_firm/<str:pk>',views.profile_statements,name = 'profile_statements'),
    path('like_post',views.like_post,name = 'like_post'),
    path('comment_post',views.comment_post,name = 'comment_post'),
    path('settings',views.settings,name = 'settings'),
    path('settings_firm',views.settings_firm,name = 'settings_firm'),
    path('trending',views.trending_page,name = 'trending_page'),
    path('notepad',views.notepad,name = 'notepad'),
    path('messaging',views.messaging,name = 'messaging'),
    path('signup_firm',views.signup_firm,name = 'signup_firm'),
    path('signup_user',views.signup_user,name = 'signup_user'),
    path('signin',views.signin,name = 'signin'),
    path('logout',views.logout,name = 'logout')
]