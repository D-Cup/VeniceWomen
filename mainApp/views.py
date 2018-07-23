import hashlib

from django.shortcuts import render, redirect

# Create your views here.
from mainApp.models import User, swImg, content


def index(request):
    sImg = swImg.objects.all()
    contents = content.objects.all()
    orderImg = content.objects.order_by('-cnt').all()
    return render(request, 'index.html',
                  {'sImgs':sImg,
                    'contents':contents,
                   'orderImgs':orderImg})

def crypt(pwd, cryptName='md5'):
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
    # user.nickName = req.POST.get('nickname')
    # 设置用户token
    # user.token = newToken(user.userName)
    user.save()

    # 将id设置到session中
    resp = redirect('/index')
    req.session['uesr_id'] = user.id
    return resp


def login(req):
    if req.method == 'GET':
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

