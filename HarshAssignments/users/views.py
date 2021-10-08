from django.shortcuts import  render, redirect
from .forms import NewUserForm,User
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import get_user_model

def home_view(request):
    return render(request, 'homepage.html')

def edit_view(request):
    return render(request, 'user_updated.html')

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login_done.html')

def delete_view(request):
    return render(request, 'user_deleted.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/login_done")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def user_details(request):
		#User = get_user_model()
		user = User.objects.all().order_by('username')
		uid_list = []

		return render(request, 'user_profile.html', {"user":user})
def update(request):

    user = NewUserForm(request.POST, instance = request.user)
    if user.is_valid():
        user.save()
        return redirect("/user_profile")
    return render(request, 'edit.html', {'user': user})
def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/user_deleted")