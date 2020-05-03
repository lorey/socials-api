import requests
import socials

# Create your views here.
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "fetch-url": reverse("socials_api_api:fetch-url", request=request, format=format),
            "filter-url-list": reverse(
                "socials_api_api:filter-url-list", request=request, format=format
            ),
            "filter-url": reverse("socials_api_api:filter-url", request=request, format=format),
        }
    )


@api_view(["POST"])
def fetch_url(request):
    url = request.POST.get("url")
    if not url:
        raise APIException("Parameter url must be non-empty")

    try:
        response = requests.get(url, headers={"user-agent": "socials-api"})
    except Exception as e:
        raise APIException("Could not fetch the given url. Is it valid?")

    if response.status_code != 200:
        raise APIException(f"Response status code was {response.status_code}, not 200")

    soup = BeautifulSoup(response.content, "lxml")
    hrefs = [a.get("href") for a in soup.find_all("a", attrs={"href": True})]
    return make_extraction_response(socials.extract(hrefs))


@api_view(["POST"])
def filter_url_list(request):
    raise NotImplementedError()


@api_view(["POST"])
def filter_url(request):
    url = request.POST.get("url")
    return make_extraction_response(socials.extract([url]))


def make_extraction_response(extraction):
    return Response({"matches_per_platform": extraction.get_matches_per_platform()})
