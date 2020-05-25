from django.shortcuts import render
from front.models import Values
from django.http import HttpResponse

# Create your views here.
def Values_view(request):
    obj = Values.objects.all()
    views_content = {
        "content": obj
    }
    return render(request,"front/index.html",views_content)

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        time = request.POST['time']
        view = request.POST['views']

        Values.objects.create(
            name = name,
            desc = desc,
            time = time,
            view = view
        )
        return HttpResponse('')
