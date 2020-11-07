from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.template import loader
from blogging.models import Post
# Create your views here.

def stub_view(request, *args, **kwargs):
    body = 'Stub View \n\n'
    if args:
        body += 'args:\n'
        body += '\n'.join(['\t%s' % a for a in args])
    if kwargs:
        body += 'kwargs:\n'
        body += '\n'.join(['\t%s: %s' % i for i in kwargs.items()])
    return HttpResponse(body, content_type='text/plain')

# responsibility of a view is to accept a request
def list_view(request):
    # query publihsed posts
    published = Post.objects.exclude(published_date__exact=None)
    # sort the query in reverse order
    posts = published.order_by('-published_date')
    # the following 3 comments so common, theres a shortcut
    # and that shortcut is the return render()
    # template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    # body = template.render(context)
    # return HttpResponse(body, content_type='text/html')
    return render(request, 'list.html', context)
