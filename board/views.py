from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import QuestionFilter
from .models import Question, Answer, Exam
from .serializers import QuestionSerializer, AnswerSerializer, ExamSerializers


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #filterset_fields
    filter_class = QuestionFilter
    search_fields = ['text']
    pagination_class = PageNumberPagination

""" 
 class QuestionList(ListCreateAPIView):
    
    # def get_queryset(self):
    #     return Question.objects.all()
    
    # def get_serializer_class(self):
    #     return QuestionSerializer


        
class QuestionDetail(RetrieveUpdateDestroyAPIView):
    #queryset = get_object_or_404(Question)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
   
    
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    def post(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        question = get_object_or_404(Question, pk=id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers