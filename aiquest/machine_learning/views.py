from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def apps(request):
    return render(request,'machine_learnings/apps.html')
    #HttpResponse('<br>Apps url directions:<br>1. http://127.0.0.1:8000/ml/machine/ <br>2. http://127.0.0.1:8000/ml/dl/   <br>3. http://127.0.0.1:8000/ml/about/')

def decision_tree(request):
    return render(request,'machine_learnings/dt.html')

def random_forest(request):
    Students={'names':['Karim','CR','Flash']}
    return render(request,'machine_learnings/random_forest.html',context=Students)


def machine(request):
    level= 'beginner'
    duration=2
    offering={'a':level,'b':duration}
    return render(request,'machine_learnings/machine_learning.html',context=offering)

def about(request):
    #print(request)
    return HttpResponse('Welcome to About Us')

def deep_learning(request):                                             #function based View
    return render(request,'machine_learnings/deep_learning.html')
    #return HttpResponse('Welcome to Django  Deep Learning')

class DeepLearning(View):                                              #class based view
    def get(self, request):
        return render(request,'machine_learnings/class_deep_learning.html')
    