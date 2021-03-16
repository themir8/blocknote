import time
from django.utils.text import slugify

def generate_url(request):
	slugify(request.POST.get("title") + "-" + str(time.strftime("%m-%d")))