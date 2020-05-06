import json

from django.shortcuts import render

from socials_api_api.views import fetch_url


def index(request):
    return render(request, "web/index.html")


def try_it(request):
    url = request.POST.get("url", "")
    if url:
        response = fetch_url(request)
        context = {
            "response_str": json.dumps(response.data, indent=2),
            "response_data": response.data,
            "url": url,
        }
    else:
        context = {"response_str": None, "response_data": None, "url": url}
    return render(request, "web/try.html", context)
