from django.shortcuts import render ,HttpResponse,redirect
from home.models import Home
from django.views.generic.edit import DeleteView
"""
def showform(request):
    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'Blog/tvreview.html', context)
"""
def home(request):
    if request.method =="POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Home(title=title,desc=desc)
        ins.save()
        print("done for the data")
    return render(request,'home.html')
# Create your views here.
def task(request):

    dataa = Home.objects.all()
    context = {'dataa' :dataa}
    
    return render(request,'task.html',context)
# Create your views here.
def delete_task(request,id):
    dataaz = Home.objects.get(id=id)
    dataaz.delete
    return redirect("task/")
    