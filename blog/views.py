from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import PostForm
from .models import Post, Contact, Action
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from django.contrib.contenttypes.models import ContentType
# Create your views here.


def dashboard_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        users = User.objects.all()
        return render(request, 'dashboard.html', {'posts': posts, 'users': users})


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
    

@require_POST
def follow_view(request):
    print(request)
    data = json.loads(request.body)
    user_to = get_object_or_404(User, id=data['id'])
    action = data['action']
    if user_to and action:
        if action == 'follow':
            Contact.objects.get_or_create(
                user_from = request.user,
                user_to = user_to
            )
            user_ct = ContentType.objects.get_for_model(User)
            Action.objects.get_or_create(
                user=request.user,
                action=' is follow ',
                target_ct = user_ct,
                target_id = user_to.id)
        elif action == 'unfollow':
            Contact.objects.get(
                user_from = request.user,
                user_to = user_to
            ).delete()
    return JsonResponse({'status': 'ok'})
    

def notifications_view(request):
    actions = Action.objects.all().exclude(user=request.user)
    posts = Post.objects.filter(user=request.user).order_by('-pub_date')
    return render(request, 'notifications.html', {'actions': actions, 'posts': posts})