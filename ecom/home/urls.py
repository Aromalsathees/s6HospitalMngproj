from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('checking/',views.checking,name='checking'),
    path('profile/<id>',views.profile,name='profile'),
    path('prescription/',views.prescription,name='prescription'),
    # path('appoiments/',views.appoiments,name='appoiments')
]
