from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm
)
from django.contrib.auth import login, logout, authenticate
from account.forms import (
    RegistrationForm,
    StudentProfileForm,
    EditUserForm,
    EditStudentForm,
)
from django.contrib import messages
from .models import Kolegij
from django.contrib.auth import update_session_auth_hash #za ponovnu prijavu nakon promjene lozinke!

def login_view(request):
    if request.method== 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                messages.info(request, f"hey {username}")
                return redirect('account/mypage.html')
            else:
                messages.error(request, "Ne valja nesto!")
        else:
                messages.error(request, "AA")
    form = AuthenticationForm()
    return render(request, "account/login.html", {'form':form})

def settings_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=request.user)
            student_form = EditStudentForm(request.POST, request.FILES, instance=request.user.student)
            if form.is_valid() and student_form.is_valid():
                user_form = form.save()
                student = student_form.save(commit=False)
                student.user = user_form
                student.save()
                return redirect('account:settings')
        else:
            form = EditUserForm(instance=request.user)
            student_form = EditStudentForm(instance=request.user.student)
            context = {'form': form, 'student_form': student_form}
            return render(request, "account/settings.html", context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            #jedno kad se promjeni lozinka django automatski odjavi usera jer se promjene podaci
            return redirect('account:mypage')
            #neka poruka uspješna promjena blabla
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form' : form}
        return render(request, 'account/change_password.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        student_form = StudentProfileForm(request.POST)

        if form.is_valid() and student_form.is_valid():
            user = form.save() #prvo spremim podatke iz forme u DJANGO USER MODEL
            student = student_form.save(commit=False) #želim spremiti u studenta al prvo pohranim podatke (commit - false) i onda nadodam podatke iz usera)
            student.user = user
            student.save()
            return redirect('homepage') #riješiti redirect

    else:

        form = RegistrationForm()
        student_form = StudentProfileForm()
        student_form.fields['studij_id'].widget.attrs = {'class': 'form-control'}

    context = {'form' : form, 'student_form' : student_form}
    return render(request, "account/signup.html", context)



def mypage_view(request):
    #ispis sve moje kolegije
    username = request.session['username']
    svi_moji_kolegiji = Kolegij.objects.raw('select * from studij_kolegij, account_moj_kolegij where studij_kolegij.kolegij_id=account_moj_kolegij.kolegij_id and account_moj_kolegij.username= %s and studij_kolegij.studij_id_id=account_moj_kolegij.studij_id_id', [username])
    context = {'svi_moji_kolegiji' : svi_moji_kolegiji}
    return render(request, "account/mypage.html", context)

def logout_view(request):
    logout(request)
    return redirect('homepage')