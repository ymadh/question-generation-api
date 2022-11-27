from urllib import response
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from string import Template
from .serializers import QuestionSerializer
from .models import Question

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
   
    latest_question_list = Question.objects.order_by('-id')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def returnQuestions(request, numQuestions):
    questions = Question.objects.all()
    numQuestionsVar = numQuestions
    print(f'numQuestions: {numQuestionsVar}')
    difficulty = request.GET['difficulty']
    print(f'difficulty recieved: {difficulty}')
    questionText=[]
    newQuestionsTemplate = Template('question : $questionText -> answer: $answer')
    for q in questions:
        questionString=newQuestionsTemplate.substitute(questionText=q.questionText,answer=q.answer) 
        print(newQuestionsTemplate.substitute(questionText=q.questionText,answer=q.answer))
        questionText.append(questionString)
    responseQuestions = '\n'.join(questionText)
    print(responseQuestions)
    return HttpResponse(responseQuestions, content_type='text/plain')