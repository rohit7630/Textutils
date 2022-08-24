# I have created this file
#jango sabse phle urls.py me aayega aur aane k bd wo check krega ki apka home jo hai wo views.py me hai
#view.py me aane k bd jo bhi funtion hoga wo print krwa dega srver pe
#hamara views return krta hai http response isle httprsponse import krna padta hai
# jaha pe manage.py hai waha pe hm banate hain directory templates naam ki

#templates use krne k lie hm pakcge import krte hi jiska nam hai 'django.shortcuts import render'

from django.http import HttpResponse
from django.shortcuts import render

# code of video 6:
# def index(request):
#return HttpResponse("<h1>Hello Rohit!!</h1> <a href = 'https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'> CodeWithharry </a>")
#
# def about(request):
#     return HttpResponse("About Rohit")

# code for video 7:
#Get method: GET is used to request data from a specified resource. and Note that the query string (name/value pairs)
# is sent in the URL of a GET request:
#GET requests have length restrictions,GET requests can be cached
# GET requests remain in the browser history,GET requests should never be used when dealing with sensitive data

# POST is used to send data to a server to create/update a resource.
# POST requests are never cached
# POST requests do not remain in the browser history

#PUT is used to send data to a server to create/update a resource.
#The difference between POST and PUT is that PUT requests are idempotent.
# That is, calling the same PUT request multiple times will always produce the same result.

#The PATCH method is used to apply partial modifications to a resource.

def index(request):
     # params = {'name':'rohit','place':'banglore'}
     return render(request,'index.html')
    # return  HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    #check checkbox values
    rempunc = request.POST.get('rempunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    #analyze the text/ check which checkbox is on
    if rempunc == "on":
        punctuations = "'!()@#$%^&*<>?[]/.,:;""~'"
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request,'analyze.html',params)
    if(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char
        params = {'purpose': 'changed to newlineremover', 'analyzed_text': analyzed}

    if (rempunc != "on" and fullcaps != "on" and newlineremover != "on"):
        return HttpResponse("please select below any buttons")

    return render(request, 'analyze.html', params)

# def capfirst(request):

    # return HttpResponse("Capitalize first <a href = '/'>back</a>")

# def newlineremove(request):
#     return HttpResponse("New Line Remover <a href = '/'>back</a>")
# def spaceremove(request):
#     return HttpResponse("Space remover <a href = '/'>back</a>")
# def charcount(request):
#     return HttpResponse("Character count <a href = '/'>back</a>")

