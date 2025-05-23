from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweet.forms import AddTweetForm
from tweet.forms import AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

@login_required(login_url='/login')
def addTweetModelForm(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data['tweet']
            TweetData = models.Tweet.objects.create(user=request.user, tweet=tweet)
            TweetData.save()
            return redirect(reverse('tweet:list_tweet'))
    else:
        form = AddTweetModelForm()
        return render(request, 'tweet/addTweetModelForm.html', context={'form': form})

@login_required(login_url='/login')
def addTweetForm(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data['Tweet']
            TweetData = models.Tweet.objects.create(user=request.user, tweet=tweet)
            TweetData.save()
        return redirect(reverse('tweet:list_tweet'))
    else:
        form = AddTweetForm()
        return render(request, 'tweet/addtweetForm.html', context={'form': form})

@login_required(login_url='/login')
def addtweet(request):
    if request.method == "POST":
        tweet = request.POST.get("tweet")
        TweetData = models.Tweet.objects.create(user=request.user, tweet=tweet)
        TweetData.save()
        return redirect(reverse('tweet:list_tweet'))
    else:
        return render(request, 'tweet/addtweet.html')

@login_required(login_url='/login')
def deletetweet(request, tweetID):
    tweet = models.Tweet.objects.get(id=tweetID)
    if request.user == tweet.user:
        tweet.delete()
        return redirect(reverse('tweet:list_tweet'))

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    return render(request, 'tweet/listtweet.html', context={'tweets': all_tweets})

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')