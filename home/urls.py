from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('quiz2', views.quiz, name = 'quiz'),
    path('scenario', views.scenario, name = 'scenario'),
    path('quiz', views.quiz2, name='quiz2'),
    path('thankyou', views.resultsPage, name='resultsPage'),
    path('moderator', views.moderator, name='moderator'),
    path('info', views.info, name='info'),
    path('feedback', views.feedback, name='feedback'),
    path('reattempt', views.reattempt, name='reattempt'),
    path('revisit', views.revisit, name='revisit'),
    path('preresults', views.preresults, name='preresults'),
    path('comeback/<pk>', views.comeback, name='comeback'),
    path('view_feedback', views.view_feedback, name='view_feedback'),
    path('', views.home, name='home')
]
