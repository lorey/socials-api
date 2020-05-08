__version__ = "0.0.0-alpha"

from socials_api import settings


def get_rate_limit_anon():
    default_throttle_rates = settings.REST_FRAMEWORK.get("DEFAULT_THROTTLE_RATES", {})
    throttle_rate_anon = default_throttle_rates.get("anon", None)
    return throttle_rate_anon
