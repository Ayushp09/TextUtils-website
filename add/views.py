from typing import Counter
from django.http import HttpResponse
from django.shortcuts import render  
def index(request):
    return render(request,"index.html")
         
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    charcount = request.POST.get('charcount','off')
    lineremove = request.POST.get('lineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext = analyzed    
        
    if (fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase','analyzed_text': analyzed}
        djtext = analyzed    
       
    if (lineremove == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines','analyzed_text': analyzed}
        djtext = analyzed    
        
    if (extraspaceremove == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose':'Removed extra spaces','analyzed_text': analyzed} 
        djtext = analyzed   
        
    if (charcount == 'on'):
        djtext = ''.join(djtext.split())
        analyzed = 0
        for char in djtext:
            analyzed = analyzed +1
        params = {'purpose':'Char Counts','analyzed_text': analyzed}
        print(analyzed)
    if(removepunc!= 'on' and fullcaps!='on' and lineremove!='on' and extraspaceremove!='on' and charcount!='on'):
        return HttpResponse('Select a switch and try again <a href="/"> HOME</a>')
    else:   
        return render(request, 'analyze.html', params)    
def contact(request):
    return render(request, 'contact.html')    

     
