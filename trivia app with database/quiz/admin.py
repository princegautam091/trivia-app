from django.contrib import admin
from .models import Question, Choices, QuizHistory

admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(QuizHistory)
