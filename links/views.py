from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Link
from .utils import saturate


class UrlForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url"]
        widgets = {"url": forms.URLInput(attrs={
            "class": "flex-1 shadow-lg shadow-inner border-none text-2xl px-8 py-4 text-blue-900 "
                     "rounded-l-lg",
            "placeholder": "www.example.com"})}


def home_page(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        form.creator = request.user
        if form.is_valid():
            obj = form.save(commit=False)  # Return an object without saving to the DB
            obj.creator = request.user if request.user.is_authenticated else None  # Add an author field which
            # will contain
            # current
            # user's id
            obj.save()  # Save the final "real form" to the DB
            return HttpResponseRedirect("/")

    else:
        all_links = Link.objects.order_by('-id')[:5]
        form = UrlForm()
        uri = f"{request.scheme}://{request.get_host()}"
        return render(request, "links/home.html", {"form": form, "all_links": all_links, "uri": uri})


def single_link(request, guid):
    link = Link.objects.get(id=saturate(guid))
    link.add_view()
    return HttpResponseRedirect(link.url)


def details(request, guid):
    link = get_object_or_404(Link, pk=saturate(guid))
    return render(request, "links/detail.html", {"link": link})


def user_links(request):
    all_links = request.user.links.all()
    form = UrlForm()
    return render(request, "links/user.html", {"form": form, "all_links": all_links})
