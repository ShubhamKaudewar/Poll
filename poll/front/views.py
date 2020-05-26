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

def Create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        time = request.POST.get('time')
        view = request.POST.get('views')

        Values.objects.create(
            name = name,
            desc = desc,
            time = time,
            view = view
        )
        return HttpResponse('')
