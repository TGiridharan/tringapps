from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from . models import File
from . forms import FileForm


def list(request):

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = File(docfile=request.FILES['docfile'])
            f.save()
            return HttpResponseRedirect(reverse('upload.views.list'))
    else:
        form = FileForm()

    files = File.objects.all()
    return render_to_response(
        'list.html',
        {'files': files, 'form': form},
        context_instance=RequestContext(request)
    )
