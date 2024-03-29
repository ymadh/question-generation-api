import itertools
import json
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from string import Template
from random import randint
from django.views.decorators.csrf import csrf_protect
from .utils import *
from .pokerHandQuestionGen import *
from .genericHandQuestionGen import *
from .serializers import QuestionSerializer
from .models import Question
from rest_framework.decorators import api_view

numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suites = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
color = ['Red', 'Black']

# make a deck of cards
deck = list(itertools.product(numbers, suites))


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


@csrf_protect
def generate(request):

    # add more question types here
    # ex: probabliyt of a 4 being drawn
    singleCardNumberOnly(deck)

    # ex: probability of a 4 of diamonds
    singleCard(deck)

    # ex: probabiliy of 3 7's in a 5 card draw
    multipleCards(deck)

    # AAA QQ
    fullhouse(deck)

    # combinatorics
    # color OR number
    colorOrNumber(numbers, color)
    # latest_question_list = Question.objects.order_by('-id')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])

    ''' Poker Questions '''
    # It can work with only one parameter where the default question amount is 1.
    # Ex: highCard(deck)

    # If the number of questions requested is > the max possibilities, you will only
    # get the max number of possibilities for your question generation.
    # Ex: royalFlush(deck, 7) only generates 4 questions as there are only 4
    # possible.

    highCard(deck, 10)
    onePair(deck, 10)
    twoPair(deck, 10)
    threeOfAKind(deck, 10)
    fourOfAKind(deck, 10)
    straight(deck, 10)
    straightFlush(deck, 10)
    flush(deck, 10)
    royalFlush(deck, 10)
    fullHouse(deck, 10)

    '''Generic Hand Questions'''
    notContainsCardInHand(deck, 10)
    containCardsInHand(deck, 10)
    exactlyOneValueInHand(deck, 10)
    atLeastOneValueInHand(deck, 10)

    context = {"generated": True}
    return render(request, "index.html", context=context)


@csrf_protect
def returnQuestions(request):
    difficulty = request.GET.get('difficulty', 1)
    numQuestions = request.GET.get('numQuestions', 10)
    questions = Question.objects.all().filter(
        difficulty__lte=difficulty).order_by("?")[:int(numQuestions)]
    context = {"list": questions}
    return render(request, "questionView.html", context)


@csrf_protect
def ui(request):
    emptyDb = Question.objects.all().count() == 0
    context = {"data": {"firstTime": emptyDb}}
    return render(request, "index.html", context)


@csrf_protect
def clearDb(request):
    Question.objects.all().delete()
    context = {"data": {"dbClear": True, "firstTime": True}}
    return render(request, "index.html", context)


@api_view(['GET'])
def singleQuestion(request):
    count = Question.objects.all().count()
    random_index = randint(0, count - 1)
    question = Question.objects.all()[random_index]
    print(question)
    print(question.questionText)
    questionParts = {"name": question.name, "question": question.questionText, "answer": question.answer, "difficulty": question.difficulty}
    context = {'data': {"singleQuestion": True, "question": questionParts}}
    return render(request, "index.html", context)
