from django.http import HttpResponse


def SaludoTmp(request):
    return HttpResponse('hola mundo curso de django')
