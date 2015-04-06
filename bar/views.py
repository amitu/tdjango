from django.shortcuts import render
from django.forms.models import modelform_factory
from django.shortcuts import render_to_response

from bar.models import Book

BookForm = modelform_factory(Book)

def v(request):
	form = BookForm()
	return render_to_response("foo.html", {"form": form})
