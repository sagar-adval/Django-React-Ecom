from django.http import JsonResponse


def home(req):
    return JsonResponse({'Admin': 'Sagar'})