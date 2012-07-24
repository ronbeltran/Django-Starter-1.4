from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    variables = RequestContext(request, {
    })
    return render_to_response(
        'home.html', variables,
    )
