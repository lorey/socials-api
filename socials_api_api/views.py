import requests
import socials
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.reverse import reverse

import socials_api_api
from socials_api import settings


@api_view(["GET"])
def api_root(request, format=None):
    response_data = {
        "endpoints": {
            "fetch-url": reverse("socials_api_api:fetch-url", request=request, format=format)
        },
        "versions": {"api": socials_api_api.__version__, "socials": socials.__version__},
    }

    if settings.DEBUG:
        response_data["debug"] = {
            "headers": request.headers,
            "meta": request.META.get("REMOTE_ADDR"),
        }

    return Response(response_data)


@api_view(["POST"])
def fetch_url(request):
    url = request.POST.get("url")
    if not url:
        raise APIException(f"Parameter url must be non-empty: {request.POST}")

    try:
        response = requests.get(url, headers={"user-agent": "socials-api"})
    except Exception as e:
        raise APIException("Could not fetch the given url. Is it valid?")

    if response.status_code != 200:
        raise APIException(f"Response status code was {response.status_code}, not 200")

    soup = BeautifulSoup(response.content, "lxml")
    hrefs = [a.get("href") for a in soup.find_all("a", attrs={"href": True})]
    return make_extraction_response(socials.extract(hrefs))


def make_extraction_response(extraction):
    return Response({"matches_per_platform": extraction.get_matches_per_platform()})
