from django.shortcuts import render, redirect
from fruitipedia_app.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, \
    FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipedia_app.web.models import Profile, Fruit



# Create your views here.

def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def show_home(request):
    profile = get_profile()
    if profile is None:
        return redirect('create profile')

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context=context)

def show_dashboard(request):
    profile = get_profile()
    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'dashboard.html', context=context)


def create_profile(request):
    profile = get_profile()
    if profile is not None:
        return redirect('index')

    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileCreateForm()

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-profile.html', context)

def details_profile(request):
    profile = get_profile()
    fruits_count = Fruit.objects.all().count()


    context = {
        'profile': profile,
        'fruits_count': fruits_count,
    }

    return render(request, 'details-profile.html', context)
def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)

def delete_profile(request):
    profile = get_profile()
    fruits = Fruit.objects.all()

    if request.method == 'POST':
        form = ProfileDeleteForm(profile, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'profile': profile,
        'forms': form,

    }
    return render(request, 'delete-profile.html', context)


def create_fruit(request):
    profile = get_profile()

    if request.method == 'POST':
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitCreateForm()

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-fruit.html', context)

def details_fruit(request, pk):
    profile = get_profile()
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, 'details-fruit.html', context)

def edit_fruit(request, pk):
    profile = get_profile()
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('details fruit', fruit.pk)
    else:
        form = FruitEditForm(instance=fruit)

    context = {
        "profile": profile,
        "fruit": fruit,
        'form': form,

    }
    return render(request, 'edit-fruit.html', context)

def delete_fruit(request, pk):
    profile = get_profile()
    fruit = Fruit.objects.\
        filter(pk=pk).\
        get()

    if request.method == 'POST':
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')
    else:
        form = FruitDeleteForm(instance=fruit)

    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form,
    }
    return render(request, 'delete-fruit.html', context)
