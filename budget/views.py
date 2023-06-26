from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import TransactionForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TransactionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect("/form-sent/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransactionForm()

    return render(request, "transaction.html", {"form": form})

def form_sent(request):
    return HttpResponse("Your form was sent!")