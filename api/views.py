import json
from typing import Any
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from .models import Company
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        if(id > 0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                data = {'ok': True, 'data': company}
            else:
                data = {'ok': False, 'message': 'company not found...'}
            return JsonResponse(data)
        else:
            company = list(Company.objects.values())
            if(len(company) > 0):
                data = {'ok': True, 'data': company}
            else:
                data = {'ok': False, 'message': 'company not found...'}
            return JsonResponse(data)

    def post(self, req):
        jd = json.loads(req.body)
        Company.objects.create(
            name=jd['name'],
            website=jd['website'],
            foundation=jd['foundation'])

        data = {'ok': True, 'message': 'success'}
        return JsonResponse(data)

    def put(self, req, id):
        jd = json.loads(req.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            data = {'ok': True, 'message': 'success'}
        else:
            data = {'ok': False, 'message': 'company not found...'}

        return JsonResponse(data)

    def delete(self, req, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            data = {'ok': True, 'message': 'success'}
        else:
            data = {'ok': False, 'message': 'company not found...'}
        return JsonResponse(data)
