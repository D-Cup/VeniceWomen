import hashlib
import uuid

import os

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from VeniceWomen import settings
from mainApp.models import User, swImg, content
from django.core.paginator import Paginator


def index(req, page):
    id = req.session.get('user_id')

    sImg = swImg.objects.all()
    contents = content.objects.all()
    orderImg = content.objects.order_by('-cnt').all()

    paginator = Paginator(contents, 15)
    paginator2 = Paginator(orderImg, 15)
    pager1 = paginator.page(page)
    pager2 = paginator2.page(page)
    print(pager1)

    if id == None:
        return render(req, 'index.html', {'sImgs': sImg,
                                          'contents': pager1.object_list,
                                          'orderImgs': pager2.object_list, })
    qs = User.objects.filter(id=id)
    if qs.exists():
        user = qs.first()
        return render(req, "index.html", {'userName': user.userName,
                                          'sImgs': sImg,
                                          'contents': pager1.object_list,
                                          'orderImgs': pager2.object_list,
                                          })
    return render(req, 'index.html', {'sImgs': sImg,
                                      'contents': pager1.object_list,
                                      'orderImgs': pager2.object_list,
                                      })


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
    resp = redirect('')
    req.session['uesr_id'] = user.id
    return resp


def login(req):
    if req.method == 'GET':
        if req.session.get('user_id'):
            return redirect('/1')
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
        return redirect('/1')
    else:
        return render(req, 'login.html',
                      {'error_msg': '用户登录失败，请重试'})


def loginout(req):
    id = req.session.get('user_id')
    if id == None:
        return render(req, 'loginout.html', {'msg': '你可能还没登录!'})
    req.session.clear()
    return render(req, 'loginout.html', {'msg': '退出成功'})


def mine(req):
    id = req.session.get('user_id')
    user = User.objects.get(id=id)

    if not req.session.get('user_id'):
        return redirect('/app/login')
    return render(req, 'mine.html',
                  {'loginUser': user})


def show(req):
    return render(req, 'show.html')


def newFileName(contentType):
    fileName = crypt(str(uuid.uuid4()))
    extName = '.jpg'
    if contentType == 'image/png':
        extName = '.png'
    return fileName + extName


@csrf_exempt  # 不做csrf_token验证
def upload(req):
    msg = {}
    session_id = req.session.get('user_id')
    if not session_id:
        msg['state'] = 'fail'
        msg['msg'] = '请先登录'
    else:
        qs = User.objects.filter(id=session_id)
        if not qs.exists():
            msg['state'] = 'fail'
            msg['msg'] = '登录失效，请重新登录'
        else:
            # 开始上传
            uploadFile = req.FILES.get('img')
            saveFileName = newFileName(uploadFile.content_type)
            saveFilePath = os.path.join(settings.MEDIA_ROOT, saveFileName)

            # 将上传文件的数据分段写入到目标文件（存入到当前服务端）中
            with open(saveFilePath, 'wb') as f:
                for part in uploadFile.chunks():
                    f.write(part)
                    f.flush()

            # 将上传文件的路径更新到用户
            qs.update(imgPath='uploads/' + saveFileName)
            msg['state'] = 'ok'
            msg['msg'] = '上传成功'
            msg['code'] = '200'
            msg['path'] = 'uploads/' + saveFileName

    return JsonResponse(msg)


def change_password(req):
    if req.method == 'GET':
        pass
    id = req.session.get('user_id')
    print(id)
    user = User.objects.get(id=id)
    pass1=req.POST.get('password1')
    print(pass1)
    user.userPasswd = crypt(req.POST.get('password'))
    user.save()
    return redirect('/app/mine')
