from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from .models import Question
from generator_utils import Generator

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('name')
    serializer_class = QuestionSerializer

@api_view
def generate():
    print('in generate')
    question = Generator.cardProbability.one_pair
    return Response(data={'question': question}, status=201)
