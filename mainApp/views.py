import hashlib

from django.shortcuts import render, redirect

# Create your views here.
from mainApp.models import User


def index(req):
    id = req.session.get('user_id')
    if id == None:
        return render(req, 'index.html')
    qs = User.objects.filter(id=id)
    if qs.exists():
        user = qs.first()
        return render(req, "index.html", {'userName': user.userName})
    return render(req, 'index.html')


def crypt(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()


def register(req):
    if req.method == 'GET':
        return render(req, 'register.html')

    user = User()
    user.userName = req.POST.get('username')
    user.userPasswd = crypt(req.POST.get('password'))
    user.email = crypt(req.POST.get('email'))
    user.phone = req.POST.get('phone')
    user.save()

    # 将id设置到session中
    resp = redirect('/index')
    req.session['uesr_id'] = user.id
    return resp


def login(req):
    if req.method == 'GET':
        if req.session.get('user_id'):
            return redirect('/index')
        return render(req, 'login.html')

    username = req.POST.get('username')
    password = req.POST.get('password')
    qs = User.objects.filter(userName=username,
                             userPasswd=crypt(password))
    if qs.exists():
        user = qs.first()
        # 向session中存放user_id, 用于判断用户是否登录
        req.session['user_id'] = user.id
        # 用户登录成功
        return redirect('/index')
    else:
        return render(req, 'login.html',
                      {'error_msg': '用户登录失败，请重试'})


def loginout(req):
    id = req.session.get('user_id')
    if id == None:
        return render(req, 'loginout.html', {'msg': '你可能还没登录!'})
    req.session.clear()
    return render(req, 'loginout.html', {'msg': '退出成功'})

def show(req):
    return render(req, 'show.html')
