from django.shortcuts import render, redirect
from . models import Shows

# Create your views here.
def index(request):
    context = {
        "all_the_shows": Shows.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    Shows.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        network = request.POST['network'],
        release_date = request.POST['release_date'] ,
    )
    return redirect('/shows/')

def edit(request, shows_id):
    show = Shows.objects.get(id=shows_id)
    context = {
        'show' : show
    }
    return render(request, 'edit.html', context)

def show(request, shows_id):
    show = Shows.objects.get(id=shows_id)
    context = {
        'show' : show
    }
    return render(request, 'show.html', context)

def update(request, shows_id):
    update = Shows.objects.get(id=shows_id)
    update.title = request.POST['title']
    update.description = request.POST['description']
    update.network = request.POST['network']
    update.release_date = request.POST['release_date']
    update.save()

    return redirect('/shows/')

def destroy(request, shows_id):
    destroy = Shows.objects.get(id=shows_id)
    destroy.delete()
    return render(request, 'index.html')