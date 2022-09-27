from dataclasses import fields
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
    category = serializers.StringRelatedField()
    class Meta:
        model = Quiz
        fields = (
            "id",
            "title",
            "category",
            "question_count",
        )


class OptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            "id",
            "option_text",
            "is_right"
        )

class QuestionSerializers(serializers.ModelSerializer):
    options = OptionSerializers(many=True)
    class Meta:
        model = Question
        fields = (
            "id",
            "title",
            "options",
            "difficulty",
        )
