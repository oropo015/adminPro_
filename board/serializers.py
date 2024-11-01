from rest_framework import serializers
from board.models import Answer, Question, Exam, Candidate



class QuestionSerializer(serializers.ModelSerializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = Question
        fields = ['id', 'exam', 'text', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    #question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ['question', 'text', 'is_correct']

class ExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'duration','pass_mark', 'is_active']

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
