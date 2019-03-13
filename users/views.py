from django.shortcuts import render,HttpResponse
from . import models,utils
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
def user_loging(requset):
    pass


def user_logout(request):
    pass

def register(request):
    if request.method == 'GET':
        return render(request,'users/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        newpwd = request.POST.get('newpwd')
        code = request.POST.get('code')
        if code == request.session['check_code']:
            try:
                models.Users.objects.get(username=username,)
            except:
                pass



@csrf_exempt
# 验证码
def addutils(req):
    # 开辟内存空间
    B = BytesIO()
    # 引入utils的产生图片和数字的方法
    img, code = utils.create_code()
    # 保存图片和数字
    req.session['check_code'] = code
    img.save(B, 'PNG')
    return HttpResponse(B.getvalue())

# Create your views here.
