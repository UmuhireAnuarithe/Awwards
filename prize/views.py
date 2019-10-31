from django.shortcuts import render,redirect
from .forms import ProfileForm,PostForm
from  .models import Profile,Projects,User
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectsSerializer

#........
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)
        return Response(serializers.data)

# Create your views here.

def home(request):
    projects = Projects.objects.all()
    return render(request,'home.html',{'projects':projects})

@login_required(login_url='/accounts/login/')
def search_projects(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        IP = Projects.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects":IP})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')       
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'new.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
  current_user = request.user
  new_profile = Profile.objects.filter(id=current_user.id)
  if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES)
      if form.is_valid():
          profile = form.save(commit=False)
          profile.username = current_user
          profile.save()
      return redirect('profile')
  else:
      form = ProfileForm()
  return render(request, 'new-profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def profile(request):
 current_user = request.user
 myprofile = Profile.objects.filter(username = current_user).first()
 username = User.objects.filter(username = current_user).first()
 IP = Projects.objects.all()
 return render(request, 'profile.html', { "myprofile":myprofile,"projects":IP})


# def user_projects(request):
#     current_user = request.user
#     username = User.objects.filter(username = current_user).first()
#     # IP = Projects.objects.filter(username_id = username.id).all()
#     username = User.objects.filter(username = current_user).first()
#     IP = Projects.objects.all()

#     return render(request,'myip.html', {"username":username, "IP":IP})
# ---------------------------------------
def edit_profile(request):
    # disp_user = request.user
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    title = "Edit Profile"
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('success')
            return redirect('profile', user_edit.id)
    else:
        form=ProfileForm(instance=request.user.profile)
        print('error')
    return render(request,'edit_profile.html',{"form":form})