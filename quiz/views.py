from rest_framework import generics

from .models import (
    Category,
    Quiz,
    Question,
    Option
)

from .serializers import (
    CategorySerializers,
    QuizSerializers,
)

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers   


