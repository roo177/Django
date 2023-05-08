from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Question,R1Code,R2Code
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def r1_codes(request):
    r1_code_list =  R1Code.objects.all().order_by('r_1_code')
    context = {"R1_kod_listesi": r1_code_list}
    return render(request, "polls/r1_codes.html", context)

def r2_codes(request):
    r2_code_list =  R2Code.objects.all().order_by('r_1_code','r_2_code')
    context = {"R2_kod_listesi": r2_code_list}
    return render(request, "polls/r2_codes.html", context) 

def r1_codes_detail(request, r_1_code):
    r1_code = get_object_or_404(R1Code, pk=r_1_code)
    r2_code_list = R2Code.objects.filter(r_1_code=r_1_code).order_by('r_1_code','r_2_code')
    context = {"R1_kod": r1_code, "R2_kod_listesi": r2_code_list}
    return render(request, "polls/r1_codes_detail.html", context)

def r2_codes_detail(request, r_1_code, r_2_code):
    r2_code = get_object_or_404(R2Code, r_1_code=r_1_code, r_2_code=r_2_code)
    r2_code_list = R2Code.objects.filter(r_1_code=r_1_code ,r_2_code = r_2_code).order_by('r_1_code','r_2_code')
    context = {"R1_kod": r_1_code, "R2_kod" : r2_code, "R2_kod_listesi": r2_code_list}
    return render(request, "polls/r2_codes_detail.html", context)