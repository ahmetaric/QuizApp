from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import (
    Category,
    Quiz,
    Question,
    Option
)

from .serializers import (
    CategorySerializers,
    QuizSerializers,
    QuestionSerializers,
)

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["title"]  

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
