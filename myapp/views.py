from django.shortcuts import render , get_object_or_404, redirect
from django.utils import timezone
from .models import Diary

# Create your views here.

def main(request):
    return render(request,"main.html")

# Create your views here.
def diary(request):
    diary=Diary.objects.all().order_by('-id')
    return render(request,"diary.html",{'diary':diary})

def detail(request,diary_id):
    diary = get_object_or_404(Diary,pk=diary_id)
    first=Diary.objects.first()
    last=Diary.objects.last()
    count=Diary.objects.count()
    return render(request,"detail.html",{'diary_detail':diary,'first':first,'last':last,'count':count})

def next(request,diary_id):
    diary=Diary.objects.all()
    diary1=Diary.objects.filter(id__gt=diary_id).order_by('id').first()
    return redirect('detail',diary1.id)

def previous(request,diary_id):
    diary=Diary.objects.all()
    diary1=Diary.objects.filter(id__lt=diary_id).order_by('id').last()
    return redirect('detail',diary1.id)

def write(request):
    if request.method=='POST':
        #디비에 저장하는 방법이 들어감.
        diary=Diary()
        diary.title=request.POST['title']
        diary.body=request.POST['body']
        diary.pub_date=timezone.datetime.now()
        diary.save()
        #처음 경로로 간다.
        return redirect('/')
    else:
         return render(request,"write.html")

def rewrite(request,diary_id):
    if request.method=='POST':
        diary=get_object_or_404(Diary,pk=diary_id)
        diary.title=request.POST['title']
        diary.body=request.POST['body']
        diary.pub_date=timezone.datetime.now()
        diary.save()
        #처음 경로로 간다.
        return redirect('/detail/'+str(diary.id))
    else:
        diary=get_object_or_404(Diary,pk=diary_id)
        return render(request,'rewrite.html',{'diary':diary})


def remove(request,diary_id):
    diary=get_object_or_404(Diary,pk=diary_id)
    diary.delete()
    return redirect('/')

def community(request):
    return render(request,"community.html")