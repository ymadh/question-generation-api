from models import Question 

def saveNewQuestion(question):
    q = Question(
        name=question.name,
        questionText=question.questionText,
        answer=question.answer,
        difficulty=question.difficulty,
        NuumInputs=question.numInputs,
    )
    q.save()