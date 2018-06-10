from django.http import JsonResponse
from django.views import View
def get(request):
  print(request)
  dict2 = {
    'melhor': 'api',
  }
  data = {
    'name': dict2,
    'lovelace': 'que vc respeita',
  }
  return JsonResponse(data)