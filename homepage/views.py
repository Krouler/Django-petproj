from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage_list(request, *args):
    return render(request, 'homepage/homepage_list.html', {})


def biography(request, *args):
    return render(request, 'homepage/biography.html', {})

def skills(request, *args):
    return render(request, 'homepage/skills.html', {})

def aboutwww(request,*args):
    CompanyName = 'Shrek ili da?'
    AboutCompany = 'Ответ на вопрос обязательный. Без него Вы будете считаться опущенцем и никто с вами не будет дужить'
    return render(request, 'homepage/about.html',{'CompanyName': CompanyName, 'AboutCompany': AboutCompany})

def contacts(request,*args):
    Phonee = 'SomeBodyOnceToldMe'
    emaill = 'That_world@IsGonnaRollMe'
    return render(request, 'homepage/contacts.html',{'Phone':Phonee,'Email': emaill})

def categories(request,*args):
    ProgrammingLanguages=['Python','C#','Java','VB(S)','Javascript']
    SQLSkills=['Easy queries','diff queries','transaction','procedure','cursor']
    Charackter=['Logical mindset','Object mindset','Critical','Humble','Accurate','Fun(not on work >:d)']
    return render(request, 'homepage/categories.html',{'PrL':ProgrammingLanguages,'SQL':SQLSkills,'Charr':Charackter})