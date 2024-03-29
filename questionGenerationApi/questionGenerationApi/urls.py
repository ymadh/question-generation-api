"""questionGenerationApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # I changed this to uuid, which is what we have now.  It may be better if we use an int and assign a value.
    path('<uuid:question_id>/', views.detail, name='detail'),
    path('generate/', views.generate, name='generate'),
    # we can send paramt that match what we need in the view like ?difficulty=<difficulty>
    path('returnQuestions/',
         views.returnQuestions, name='returnQuestions'),
    path('gui/', views.ui, name='ui'),
    path('clearDatabase/', views.clearDb, name='clearDb'),
    path('singleQuestion/',
         views.singleQuestion, name='singleQuestion'),

]
