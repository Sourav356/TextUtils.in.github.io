# I have created this file - Sourav
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext =(request.POST.get('text','default'))
    removepunc =(request.POST.get('removepunc','off'))
    capitalize =(request.POST.get('capitalize','off'))
    spaceremover =(request.POST.get('spaceremover','off'))
    newlineremover =(request.POST.get('newlineremover','off'))
    cahrcount =(request.POST.get('cahrcount','off'))
    if removepunc == 'on':
        punctuations = '''!()-_{}[],.<>/?@#$%^&*;':"'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Removed Punctuation' , 'analyzed_text': analyzed}
        djtext = analyzed

    if(capitalize =='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params ={'purpose':'Convert Your text into Uppercase' , 'analyzed_text': analyzed}
        djtext = analyzed

    if(spaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove The Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed=""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove The New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if(cahrcount == 'on'):
        count = len(djtext)
        analyzed= "Your text have",count,"character on it"
        params ={'purpose': 'Count How many Character is present', 'analyzed_text':  analyzed}

    if(removepunc != 'on' and capitalize != 'on' and spaceremover != 'on' and newlineremover != 'on' and cahrcount != 'on'):
        return HttpResponse("Please choose the right operation and try again")

    return render(request, 'analyze.html', params)

def Navigation(request):
    Textall = (request.POST.get('text1','default'))
    print(Textall)
    return render(request,'Navi.html')

def thanks(request):
    return HttpResponse('Thank You for Your valuable Feedback.')

def contact(request):
    contactInfo = (request.POST.get('text2','default'))
    return render(request, 'contact.html')



