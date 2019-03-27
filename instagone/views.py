from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Image, instagoneLetterRecipients
from .forms import instagoneLetterForm,NewImageForm,ProfileUploadForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.
# def welcome(request):
#     return render(request, 'all-photos/today-photos.html', {"date": date,})

@login_required(login_url='/accounts/login/')
def instagone_today(request):
    date = dt.date.today()
    all_images = Image.all_images()
    images= Image.objects.all()
    print(images)
    # image = Image.today-photos()
    if request.method == 'POST':
        form = instagoneLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = instagonesLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('instagones_today')
    else:
        form = instagoneLetterForm()
        form = NewImageForm()
    return render(request, 'all-instagone/today-instagone.html', {"date": date,"letterForm":form, "ImageForm":form,'images':images})


def past_days_instagone(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(instagones_today)

    instagone_today = Image.past_days_instagone(date)
    return render(request, 'all-instagone/past-instagone.html',{"date": date,"instagone":instagone})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-instagone/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-instagone/search.html',{"message":message})

@login_required(login_url='/accounts/login/')

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    title = 'New image'
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('InstagoneToday')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form,"current_user":current_user,"title":title})

@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['image']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(image = form.cleaned_data['image'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})