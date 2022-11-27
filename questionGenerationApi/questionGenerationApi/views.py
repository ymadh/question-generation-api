import itertools
import json
from urllib import response
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from string import Template

from .utils import multipleCards, singleCard, singleCardNumberOnly

from .serializers import QuestionSerializer
from .models import Question


# make a deck of cards
deck = list(itertools.product(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
                              ['Spade', 'Heart', 'Diamond', 'Club']))


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('name')
    serializer_class = QuestionSerializer

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


# sample view
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def generate(request):

    # add more question types here
    # ex: probabliyt of a 4 being drawn
    singleCardNumberOnly(deck)

    # ex: probability of a 4 of diamonds
    singleCard(deck)

    # ex: probabiliy of 3 7's in a 5 card draw
    multipleCards(deck)

    # latest_question_list = Question.objects.order_by('-id')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse("OK")


def returnQuestions(request, numQuestions):
    questions = Question.objects.all()
    difficulty = request.GET['difficulty']
    print(f'difficulty recieved: {difficulty}')
    questionText = []
    newQuestionsTemplate = Template(
        'question : $questionText -> answer: $answer')
    count = 0
    for q in questions:

        if count == numQuestions:
            continue
        count += 1
        questionString = newQuestionsTemplate.substitute(
            questionText=q.questionText, answer=q.answer)
        print(newQuestionsTemplate.substitute(
            questionText=q.questionText, answer=q.answer))
        questionText.append(questionString)
    responseQuestions = '\n'.join(questionText)
    print(responseQuestions)
    return HttpResponse(responseQuestions, content_type='text/plain')
