from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def answer(x):
    p = ""
    if x == 4:
        p = "Молодец"
    else:
        p = "Немолодец"
    return p


def index(request, k=''):
    if request.method == 'POST':
        x = int(request.POST['x'])
        k = answer(x)
    return render(request, 'game/gm.html', {"k": k})


#def gm(request):
 #   return render(request, 'game/gm.html')


'''
def index(request):
    print(request.GET)
    return HttpResponse("Да начнется игры!")
'''


# def g(request, gameid):
#   return HttpResponse("<h1>Да начнется!</h1><p>{gameid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Упс... Не повезло</h1>")
