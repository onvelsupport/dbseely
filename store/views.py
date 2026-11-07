from django.shortcuts import render, redirect
from .forms import EntryForm


def giveaway(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = EntryForm()

    return render(request, "store/giveaway.html", {"form": form})


def thank_you(request):
    return render(request, "store/thank-you.html")
