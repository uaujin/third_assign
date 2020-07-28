from .models import Profile
from django.shortcuts import render , get_object_or_404, redirect
# Create your views here.
def index(request):
    if request.method =="POST":
        form =Profile()
        form.title=request.POST['title']
        try:
            form.image=request.FILES['image']
        except:
            pass
        form.save()
        profile=Profile.objects.all()
        return render(request,'index.html',{'profile':profile})
    else:
        profile=Profile.objects.all()
        return render(request,'index.html',{'profile':profile})

def remove_image(request,profile_id):
    profile=get_object_or_404(Profile,pk=profile_id)
    profile.delete()
    return redirect('/')