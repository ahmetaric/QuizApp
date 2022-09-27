from rest_framework import serializers

from .models import (
    Category,
    Quiz,
    Question,
    Option
)

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz_count",
        )


class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            "id",
            "title",
            "category",
            "question_count",
        )
