from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Post

# Create your views here.

class IndexView(generic.ListView):
        template_name = 'blog/index.html'
        context_object_name = 'post_list'

        def get_queryset(self):
                return Post.objects.filter(
                        posted_date__lte=timezone.now()
                ).order_by('-posted_date')[:5]

def ResumeView(request):
	template = loader.get_template("blog/resume.html")
	context = {
		'content' : "Hello this is my resume page. This will hold a PDF eventually",
	}
	return HttpResponse(template.render(context, request))
