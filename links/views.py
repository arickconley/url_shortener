from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .models import Link
from .utils import saturate


class UrlForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url"]
        widgets = {"url": forms.URLInput(attrs={
            "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1  w-full sm:text-sm border-gray-300",
            "placeholder": "www.example.com"})}


def home_page(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            values = form.save()
            return HttpResponseRedirect("/")

    else:
        all_links = Link.objects.all()
        form = UrlForm()
        uri = f"{request.scheme}://{request.get_host()}"
        return render(request, "links/home.html", {"form": form, "all_links": all_links, "uri": uri})


def single_link(request, guid):
    link = Link.objects.get(id=saturate(guid))
    link.add_view()
    return HttpResponseRedirect(link.url)
