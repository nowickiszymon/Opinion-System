from django.urls import path

from .views import OpinionList
from .views import OpinionCreate

urlpatterns = [
        path('all', OpinionList.as_view(), name="option_list"),       
        path('create', OpinionCreate.as_view(), name="option_create")       
]
