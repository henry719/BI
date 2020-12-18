from django.shortcuts import render, redirect
from login import models
from .forms import UserForm, RegisterForm
import hashlib

def index(request):
    pass
    return render(request, 'login/index.html')

def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写内容'
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = models.User.objects.get(username=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = '密码不正确!'
            except:
                message = 'esraer'
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            department = register_form.cleaned_data['department']
            if password1 != password2:
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.department = department
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')

def runoob(request):
    pass
    return render(request, 'runoob.html')

def hash_code(s, salt='login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()






