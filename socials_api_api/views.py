import socials

# Create your views here.
from rest_framework.decorators import api_view
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
    raise NotImplementedError()


@api_view(["POST"])
def filter_url_list(request):
    raise NotImplementedError()


@api_view(["POST"])
def filter_url(request):
    url = request.POST.get("url")
    return Response(socials.extract([url]).get_matches_per_platform())
