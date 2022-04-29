from django.http import JsonResponse

def getRoutes(requests):
    routes=[
        '/api/token',
        '/api/token/refresh',
    ]
    return JsonResponse(routes,safe=False)