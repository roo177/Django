from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Question,R1Code,R2Code,R3Code,R4Code,Choice
from django.template import loader
from django.urls import reverse

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

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

def r1_codes(request):
    r1_code_list =  R1Code.objects.all().order_by('r_1_code')
    context = {"R1_kod_listesi": r1_code_list}
    return render(request, "polls/r1_codes.html", context)

def r2_codes(request):
    r2_code_list =  R2Code.objects.all().order_by('r_1_code','r_2_code')
    context = {"R2_kod_listesi": r2_code_list}
    return render(request, "polls/r2_codes.html", context) 

def r3_codes(request):
    r3_code_list =  R3Code.objects.all().order_by('r_1_code','r_2_code','r_3_code')
    context = {"R3_kod_listesi": r3_code_list}
    return render(request, "polls/r3_codes.html", context) 

def r4_codes(request):
    r4_code_list =  R4Code.objects.all().order_by('r_1_code','r_2_code','r_3_code','r_4_code')
    context = {"R4_kod_listesi": r4_code_list}
    return render(request, "polls/r4_codes.html", context) 

def r1_codes_detail(request, r_1_code):
    r1_code = get_object_or_404(R1Code, pk=r_1_code)
    r1_code_list = R1Code.objects.filter(r_1_code=r_1_code).order_by('r_1_code')
    context = {"R1_kod": r1_code, "R1_kod_listesi": r1_code_list}
    return render(request, "polls/r1_codes_detail.html", context)

def r2_codes_detail(request, r_1_code, r_2_code):
    r2_code = get_object_or_404(R2Code, r_1_code=r_1_code, r_2_code=r_2_code)
    r2_code_list = R2Code.objects.filter(r_1_code=r_1_code ,r_2_code = r_2_code).order_by('r_1_code','r_2_code')
    context = {"R1_kod": r_1_code, "R2_kod" : r2_code, "R2_kod_listesi": r2_code_list}
    return render(request, "polls/r2_codes_detail.html", context)

def r3_codes_detail(request, r_1_code, r_2_code, r_3_code):
    r3_code = get_object_or_404(R3Code, r_1_code=r_1_code, r_2_code=r_2_code, r_3_code=r_3_code)
    r3_code_list = R3Code.objects.filter(r_1_code=r_1_code ,r_2_code = r_2_code, r_3_code= r_3_code).order_by('r_1_code','r_2_code','r_3_code')
    context = {"R1_kod": r_1_code, "R2_kod" : r_2_code, "R3_kod": r3_code, "R3_kod_listesi": r3_code_list}
    return render(request, "polls/r3_codes_detail.html", context)

def r4_codes_detail(request, r_1_code, r_2_code, r_3_code, r_4_code):
    r4_code = get_object_or_404(R4Code, r_1_code=r_1_code, r_2_code=r_2_code, r_3_code=r_3_code, r_4_code=r_4_code)
    r4_code_list = R4Code.objects.filter(r_1_code=r_1_code ,r_2_code = r_2_code, r_3_code= r_3_code, r_4_code= r_4_code).order_by('r_1_code','r_2_code','r_3_code', 'r_4_code')
    context = {"R1_kod": r_1_code, "R2_kod" : r_2_code, "R3_kod": r_3_code, "R4_kod": r4_code, "R4_kod_listesi": r4_code_list}
    return render(request, "polls/r4_codes_detail.html", context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


