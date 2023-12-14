from django.urls import path
from . import views as ml

urlpatterns = [
    path('', ml.apps),      #   http://127.0.0.1:8000/ml/
    path('machine/', ml.machine, name='machine_learning_base'), #using function 'machine' defined in views of machine_leaning app
    path('dl/',ml.deep_learning),
    path('about/',ml.about),
    path('dt/',ml.decision_tree),
    path('rf/',ml.random_forest),
    path('class/',ml.DeepLearning.as_view()),
]