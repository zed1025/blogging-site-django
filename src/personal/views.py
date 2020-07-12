from django.shortcuts import render
from account.models import Account
from blog.models import BlogPost
from operator import attrgetter
from blog.views import get_blog_query_set

# Create your views here.

def home_screen_view(request):
	context = {}

	query = ''
	if request.GET:
		query = request.GET['q']
		context['query'] = str(query)

	blog_posts = sorted(get_blog_query_set(query), key=attrgetter('date_updated'), reverse=True)

	context['blog_posts'] = blog_posts
	return render(request, 'personal/home.html', context)