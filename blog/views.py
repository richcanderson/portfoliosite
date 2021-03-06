from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
import mimetypes

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def dbmsproject(request):
    return render(request, 'blog/dbmsproject.html', {'title': 'DBMS Project'})


def download_file(request):
    # fill these variables with real values
    fl_path = '/dbmsproject/'
    filename = 'dbreport.pdf'


    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
