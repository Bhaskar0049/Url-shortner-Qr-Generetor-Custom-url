

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL,Custom_url
import string
import random
import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings
import re


def index(request):
    return render(request, 'index.html')

#url shortner
def generate_short_url():
    letters = string.ascii_letters + string.digits + string.ascii_letters + string.digits + string.ascii_letters 
    while True:
        short_url = ''.join(random.choice(letters) for i in range(random.randrange(6,9)))
        if not URL.objects.filter(short_url=short_url).exists():
            return short_url

def shorturl(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url = generate_short_url()
        url = URL(original_url=original_url, short_url=short_url)
        url.save()
        short_url = request.build_absolute_uri('/') + short_url
        return render(request, 'shortener/shortened.html', {'short_url': short_url})
    return render(request, 'shortener/shorturl.html')

def redirect_original(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return HttpResponse('Invalid URL')


#####custom url create
def customurl(request):
    if request.method == 'POST':
        original_url=request.POST['ori_url']
        cus_slug=request.POST['cus_slug']
        if re.search(r"^[\w-]*$", cus_slug):
            if  Custom_url.objects.filter(custom_url=cus_slug).exists():
                used=cus_slug
                return render(request,'custom/custom.html',{'used':used})
            url=Custom_url(original_url=original_url,custom_url=cus_slug)
            url.save()
            customurl= request.build_absolute_uri('/') +'c/'+ cus_slug
            return render(request,'custom/customurl.html',{'custom_url':customurl})
        else:
            slug=cus_slug
            return render(request,'custom/custom.html',{'slug':slug})
    return render(request,'custom/custom.html')

def redirect_custom_to_original(request,customurl):
    try:
        url = Custom_url.objects.get(custom_url=customurl)
        return redirect(url.original_url)
    except Custom_url.DoesNotExist:
        return HttpResponse("<h1>Invalid Url</h1>")




#qr code generator
def generate_qr(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        letter = string.ascii_letters 
        name_qr = ''.join(random.choice(letter) for i in range(random.randrange(5,12)))
        file_name = f'qr_code_{name_qr}.png'
        
        file_path = f'{settings.MEDIA_ROOT}/qr/{file_name}'
        print(file_path)
        with open(file_path, 'wb') as f:
            img.save(f, 'PNG') 
        # this is the URL path for browser
        image_url = settings.MEDIA_URL + "qr/" + file_name
        print(image_url)     
        return render(request, 'qrcode/qrcode.html', {'qr_code':file_path,
                                                      'file_name':file_name,
                                                      'file_path':image_url,
                                                      })
    return render(request, 'qrcode/qrcode.html')

def about(request):
    return render(request,'about.html')

def privacy(request):
    return render(request,'policy.html')

def test(request):
    return HttpResponse("<h1>Test is successful</h1>")
