
from django.urls import path
from .views import Create, home, select
urlpatterns = [
    path('', select, name='select'),
    path('home/', home, name="home"),
    path('create/', Create, name="create")

]