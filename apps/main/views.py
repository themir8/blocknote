from django.shortcuts import render
from django.views.generic.base import View


class MainView(View):
    """Основная страница"""

    def get(self, request):
    	if(not request.user.is_authenticated):
    		return render(request, 'main/login.html')
    	else:
    		return render(request, 'main/index.html')
