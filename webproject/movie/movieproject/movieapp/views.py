from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import movie
from . forms import movieform
# Create your views here.




def index(request):
    Movie =movie.objects.all()
    context = {
        'movie_list':Movie
    }
    return render(request,'index.html',context)


def detail(request,movie_id):
    Movie = movie.objects.get(id=movie_id)

    return render(request,'details.html',{'movie':Movie})
def movie_add(request):
    if request.method =="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        date = request.POST.get('date',)
        img = request.FILES['img']
        Movie=movie(name=name,desc=desc,date=date,img=img)
        Movie.save()
    return render(request,"add.html")
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':Movie,'form':form})
def delete(request,id):
    if request.method=='POST':
        Movie = movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
