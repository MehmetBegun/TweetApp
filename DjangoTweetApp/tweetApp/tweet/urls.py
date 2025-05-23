from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.listtweet, name='main'),
    path('addTweet/', views.addtweet, name='add_tweet'),
    path('addTweetForm/', views.addTweetForm, name='add_tweet_form'),
    path('addTweetModelForm/', views.addTweetModelForm, name='add_tweet_model_form'),
    path("deletetweet/<int:tweetID>/", views.deletetweet, name='delete_tweet'),
    path('listTweet/', views.listtweet, name='list_tweet'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]