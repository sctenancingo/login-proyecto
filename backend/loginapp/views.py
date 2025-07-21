from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'fail'}, status=401)
    return JsonResponse({'detail': 'Method not allowed'}, status=405)

@login_required
def dashboard_view(request):
    return render(request, 'loginapp/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')