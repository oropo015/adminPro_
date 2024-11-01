from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('answers', views.AnswerViewSet)
router.register('exams', views.ExamViewSet)
router.register('students', views.CandidateViewSet)



questions_router = routers.NestedDefaultRouter(router, 'questions', lookup='questions')
questions_router.register('answers', views.AnswerViewSet, basename='question-answers')

urlpatterns = router.urls + questions_router.urls
#URLConf
#urlpatterns = [""" 
 #   path('questions/', views.QuestionList.as_view()),
  #  path('questions/<int:id>/', views.QuestionDetail.as_view()) """
#]