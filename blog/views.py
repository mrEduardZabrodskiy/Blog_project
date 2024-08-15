from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import PostForm
from .models import Post
# Create your views here.


def dashboard_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'dashboard.html', {'posts': posts})


def profile_view(request, pk):
    if request.method == 'GET':
        user = get_object_or_404(User, id=pk)
        post_form = PostForm()
        posts = Post.objects.filter(user=user).order_by('-pub_date')
        return render(request, 'profile.html', {'post_form': post_form, 'user': user, 'posts':posts})
    elif request.method == 'POST':
        print(request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = form.save(commit=False)
            post.user = request.user
            post.title = cd['title']
            post.body = cd['body']
            print(post)
            post.save()
            return redirect(reverse('profile_view', kwargs={'pk': request.user.id}))
        else:
            return HttpResponse("Some data of Post fields are wrong.")




def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.user == request.user:
        post.delete()
        return redirect(reverse('profile_view', kwargs={'pk': request.user.id}))