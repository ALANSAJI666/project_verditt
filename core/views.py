from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Post,LikePost, FollowersCount
from itertools import chain
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import uuid

from django.http import HttpResponse



# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)


        if user is not None:
            auth.login(request, user)
            # redirecting to home page
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def index(request):
    # if request.user.is_authenticated:
    #
    #     user_object = User.objects.get(username=request.user.username)
    #     return HttpResponse(user_object)
    # else:
    #     return redirect('signin')

    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user =user_object)

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower = request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user = usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    posts = Post.objects.all()
    return render(request, 'index.html',{'user_profile': user_profile,'posts':feed_list})
    # return render(request,'index.html')





@login_required(login_url='signin')
def upload(request):
    if request.method=='POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user,image=image,caption = caption)
        new_post.save()
        
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user = user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username_icontains = username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user = ids)
            username_profile_list.append(profile_lists)

    username_profile_list = list(chain(*username_profile_list))
    return render(request,'search.html', {'user_profile': user_profile,'username_profile_list': username_profile_list })

@login_required(login_url='signin')
def profile(request,pk):
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(user =pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower = follower,user = user).first():
        button_text = 'Following'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user = pk))
    user_following = len(FollowersCount.objects.filter(follower = pk))
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts' :  user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following

    }
    return render(request,'profile.html', context)

@login_required(login_url='signin')
def profile_statements(request,pk):
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(user =pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower = follower,user = user).first():
        button_text = 'Following'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user = pk))
    user_following = len(FollowersCount.objects.filter(follower = pk))
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts' :  user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following

    }
    return render(request,'profile_statements.html', context)

@login_required(login_url='signin')
def profile_firm(request,pk):
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(user =pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower = follower,user = user).first():
        button_text = 'Following'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user = pk))
    user_following = len(FollowersCount.objects.filter(follower = pk))
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts' :  user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following

    }
    return render(request,'profile_firm.html', context)

@login_required(login_url='signin')
def profile_statements_firm(request,pk):
    user_object = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(user =pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower = follower,user = user).first():
        button_text = 'Following'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user = pk))
    user_following = len(FollowersCount.objects.filter(follower = pk))
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts' :  user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following

    }
    return render(request,'profile_statements_firm.html', context)

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower,user = user).first():
            delete_follower = FollowersCount.objects.get(follower=follower,user = user)
            delete_follower.delete()
            return redirect('/profile/' +user )
        else:
            new_follower = FollowersCount.objects.create(follower = follower,user = user)
            new_follower.save()
            return redirect('/profile/' + user)
    else:
        return redirect('/')


@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)




    like_filter = LikePost.objects.filter(post_id = post_id,username = username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id = post_id,username = username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')



@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user = request.user)

    if request.method =='POST':
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            current_status = request.POST['current_status']
            educational_qualifications = request.POST['educational_qualifications']
            contact_info = request.POST['contact_info']
            open_to_work = request.POST['open_to_work']
            location = request.POST['location']


            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.current_status = current_status
            user_profile.educational_qualifications = educational_qualifications
            user_profile.contact_info = contact_info
            user_profile.open_to_work = open_to_work
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image =  request.FILES.get('image')
            bio = request.POST['bio']
            current_status = request.POST['current_status']
            educational_qualifications = request.POST['educational_qualifications']
            contact_info = request.POST['contact_info']
            open_to_work = request.POST['open_to_work']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.current_status = current_status
            user_profile.educational_qualifications = educational_qualifications
            user_profile.contact_info = contact_info
            user_profile.open_to_work = open_to_work
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('settings')





    return render(request, 'setting.html',{'user_profile': user_profile})


@login_required(login_url='signin')
def settings_firm(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            current_status = request.POST['current_status']
            educational_qualifications = request.POST['educational_qualifications']
            contact_info = request.POST['contact_info']
            open_to_work = request.POST['open_to_work']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.current_status = current_status
            user_profile.educational_qualifications = educational_qualifications
            user_profile.contact_info = contact_info
            user_profile.open_to_work = open_to_work
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            current_status = request.POST['current_status']
            educational_qualifications = request.POST['educational_qualifications']
            contact_info = request.POST['contact_info']
            open_to_work = request.POST['open_to_work']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.current_status = current_status
            user_profile.educational_qualifications = educational_qualifications
            user_profile.contact_info = contact_info
            user_profile.open_to_work = open_to_work
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('settings_firm')

    return render(request, 'setting_firm.html', {'user_profile': user_profile})


def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup_user')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup_user')
            elif not username or not email or not password:
                messages.info(request, 'All of the below columns ought to be filled')
                return redirect('signup_user')
            else:
                # log user in and redirect to settings page
                # user_login = auth.authenticate(request,username=username,password =password)
                # if user_login is None:
                #     messages.info(request, 'Authentication Failed')
                #     return redirect('signup')
                # return HttpResponse(password)

                # create a profile for the new user
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                auth.login(request, user)
                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user = user_model,id_user = user_model.id)
                new_profile.save()
                return redirect('settings')





        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup_user')



    else:
        return render(request,'signup_user.html')

def signup_firm(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup_firm')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup_firm')
            elif not username or not email or not password:
                messages.info(request, 'All of the below columns ought to be filled')
                return redirect('signup_firm')
            else:
                # log user in and redirect to settings page
                # user_login = auth.authenticate(request,username=username,password =password)
                # if user_login is None:
                #     messages.info(request, 'Authentication Failed')
                #     return redirect('signup')
                # return HttpResponse(password)

                # create a profile for the new user
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                auth.login(request, user)
                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user = user_model,id_user = user_model.id)
                new_profile.save()
                return redirect('settings_firm')





        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup_firm')



    else:
        return render(request,'signup_firm.html')

# @login_required(login_url='signin')
# def conversation_list(request):
#     conversations = Conversation.objects.filter(participants = User.objects.get(username = request.user.username))
#     return render(request, 'conversation_list.html', {'conversations': conversations})

# @login_required(login_url='signin')
# def conversation_detail(request, conversation_id):
#     conversation = Conversation.objects.get(id=conversation_id)
#     messages = conversation.messages.order_by('timestamp')
#     return render(request, 'conversation_detail.html', {'conversation': conversation, 'messages': messages})

# @login_required
# def conversations(request):
#     conversations = Conversation.objects.filter(Q(user1=request.user) | Q(user2=request.user))
#     return render(request, 'messenger/conversation_list.html', {'conversations': conversations})


# @login_required
# def messages(request, conversation_id):
#     conversation = get_object_or_404(Conversation, id=conversation_id)
#     if request.user != conversation.user1 and request.user != conversation.user2:
#         return redirect('conversations')
#     messages = Message.objects.filter(conversation=conversation).order_by('-created_at')[:50][::-1]
#     return render(request, 'messenger/messages.html', {'conversation': conversation, 'messages': messages})


# @login_required
# def start_conversation(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         recipient = get_object_or_404(User, username=username)
#         conversation = Conversation.objects.filter(user1=request.user, user2=recipient).first()
#         if conversation:
#             return redirect('messages', conversation_id=conversation.id)
#         conversation = Conversation.objects.filter(user1=recipient, user2=request.user).first()
#         if conversation:
#             return redirect('messages', conversation_id=conversation.id)
#         conversation = Conversation(user1=request.user, user2=recipient)
#         conversation.save()
#         return redirect('messages', conversation_id=conversation.id)
#     else:
#         return render(request, 'messenger/start_conversation.html')


# def message_send(request, conversation_id):
#     conversation = get_object_or_404(Conversation, id=conversation_id)
#     if request.user != conversation.user1 and request.user != conversation.user2:
#         return redirect('conversations')
#     message = Message(conversation=conversation, sender=request.user, text=request.POST.get('message'))
#     message.save()
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         f"chat_{conversation_id}",
#         {
#             "type": "chat_message",
#             "message": json.dumps({
#                 "id": message.id,
#                 "sender": message.sender.username,
#                 "text": message.text,
#                 "created_at": message.created_at.strftime('%Y-%m-%d %H:%M:%S')
#             })
#         }
#     )
#     return redirect('messages', conversation_id=conversation_id)

@login_required(login_url='signin')
def trending_page(request):
    trending_topics = ['#Panther','#workplaceharrassment','#outrageous']
    context = {'trending_topics': trending_topics}
    return render(request, 'trending_page.html', context)

@login_required(login_url='signin')
def notepad(request):
    # trending_topics = ['#Panther','#workplaceharrassment','#outrageous']
    # context = {'trending_topics': trending_topics}
    return render(request, 'notepad.html')
@login_required(login_url='signin')
def messaging(request):
    return render(request, 'messaging.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')



