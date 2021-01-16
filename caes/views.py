from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from caes.forms import SignUpForm, ProfileForm
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.urls import reverse



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    
        return render(request, 'index.html', {})
        
def voiceind(request):
    
        return render(request, 'voiceind.html', {})        
        
def profile(request):
        return render(request, 'profile.html', {}) 
        
def edit(request):
        return render(request, 'edit.html', {})        

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)        
        
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'edit.html'  
    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user
    

    def get_success_url(self, *args, **kwargs):
        return reverse("profile")        
        



 
