from django.shortcuts import render,redirect
from .models import Category,Photo
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def gallery(request):
    category=request.GET.get('category')
    if category==None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)    
    categories=Category.objects.all()
    context = {'categories':categories,'photos':photos}
    return render(request,'photos/gallery.html',context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

def addPhoto(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category']!='none':
            category=Category.objects.get(id=data['category'])
        elif data['category']!='':
            category,created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo=Photo.objects.create(
            category=category,
            description = data['description'],
            image=image
        )
        return redirect('gallery')

    context = {'categories':categories}
    return render(request,'photos/add.html',context)



def singlePostView(request, pic_id = None):
    pic = Photo.objects.get(id = pic_id)
    print(pic)

    context = {
    'pic':pic,
    }
    return render(request,"gallery.html", context)



def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # result = Category.objects.filter(name__contains=searched)
        result_two = Photo.objects.filter(category__name=searched)
        return render(request,"photos/search.html",{'searched':searched, 'result_two':result_two})
       
    else:
        return render(request,"photos/search.html",{})