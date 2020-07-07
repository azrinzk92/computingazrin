"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.transcription, name='perumah'),
    path('transcriptionresult', views.transcriptionresult),
    path('translation', views.translation, name='mukasurat1'),
    path('translationresult', views.translationresult),
    path('gcpercentage', views.gcpercentage, name='mukasurat2'),
    path('gcpercentageresult', views.gcpercentageresult),
    path('pairwisealignment', views.pairwisealignment, name='mukasurat3'),
    path('pairwiseresult', views.pairwiseresult),
    path('revcom', views.reversecomplement, name='mukasurat4'),
    path('reversecomplementresult', views.reversecomplementresult),
]
