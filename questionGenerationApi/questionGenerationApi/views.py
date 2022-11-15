from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import QuestionSerializer
from .models import Question
from .generator_utils import Generator

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('name')
    serializer_class = QuestionSerializer

@api_view(['GET'])
def generate(request):
    print('in generate')
    queryset = Question.objects.all().order_by('name')
    serializer_class = QuestionSerializer
    question = Generator.cardProbability.one_pair
    print('queryset: ', queryset)
    return HttpResponse('question', status=201)
