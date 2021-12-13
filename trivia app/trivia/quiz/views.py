from collections import UserList
from django.shortcuts import render,redirect
from django.http.response import *
from quiz.forms import  UserCreateForm
from .models import Name
# Create your views here.

def home(request):
    if request.method=="GET":
        user=UserCreateForm()
        return render(request,"home.html",{'user':user})
    else:
        user=UserCreateForm(request.POST)
        user.save()
        return render(request,'game.html',{'user':user})
      

def createExam():
	questions=[
		{
			'question1':'Who is the best cricketer in the world?',
			'answers': ['Sachin Tendulkar', 'Virat Kohli', 'Adam Gilchrist','Jacque kallis'],
			'correct': 'Sachin Tendulkar',
			'answer': ''
		},
		{
			'question2':'What are the colors in the Indian national flag?',
			'answers':['White',' Yellow','Orange','Green'],
			'correct': ['White','Orange','Green'],
			'answer': '',
		},
		
	]

	return questions



def startExam(request):
	if(request.method=='GET'):
		questionBank = createExam()
		request.session['questionBank']=questionBank
		request.session['current']=1

		question = questionBank[0]
		return render(request,'exam.html',{'qno':1,'total':2,'question':question})
	else:
		questionBank = request.session['questionBank']
		current = request.session['current']
		answer = request.POST.get('answer')

		if(answer!=None):
			questionBank[current-1]['answer'] = answer

		action = request.POST.get('action')
		if(action=='Previous'):
			current=current-1
		elif(action=='Next'):
			current=current+1
		else:
			return redirect('/result/')


		request.session['questionBank']=questionBank
		request.session['current']=current

		question = questionBank[current-1]
		return render(request,'exam.html',{'qno':current,'total':2,'question':question})

def result(request):
	score = 0
	questionBank = request.session['questionBank']

	for question in questionBank:
		if(question['correct'] == question['answer']):
			score+=1
		else:
			score-=0.1

	del request.session['questionBank']
	del request.session['current']
	return render(request,'result.html',{'score':score})     
        
def history(request):
	user=UserCreateForm()
	for i in user:
			print(i)
			
	return render(request,'history.html',{'user':user})   