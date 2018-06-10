from django.http import JsonResponse
from django.views import View
def get(request):
  print(request)
  dict2 = {
    'asdf': 'ii',
  }
  data = {
    'name': dict2,
    'version': 'oh wait',
  }
  return JsonResponse(data)