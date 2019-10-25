from django.shortcuts import render
from .forms import ProfileForm
from  .models import Profile
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


def search_projects(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        Ip = Article.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": IP})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})




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


# @login_required(login_url='/accounts/login/')
def profile(request):
 current_user = request.user
 myprofile = Profile.objects.filter(username = current_user).first()
 return render(request, 'profile.html', { "myprofile":mypicture})
