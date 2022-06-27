from django.http import HttpResponse


def Saludo(request):
    return HttpResponse('hola mundo curso de django')
