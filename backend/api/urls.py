from django.urls import path

from .views import OpinionList

urlpatterns = [
        path('all', OpinionList.as_view(), name="option_list")       
]
