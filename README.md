# socials API: extract social media profiles
The [socials API](http://socials.karllorey.com) allows you to extract social media profiles from urls.
It is an API version of my library called [socials for Python](https://github.com/lorey/socials).

Try it at [socials.karllorey.com](http://socials.karllorey.com).

## Example
Requesting `http://socials.karllorey.com/api/fetch-url` 
with a POST request and `url=https://karllorey.com` as parameter 
will return all social media profiles 
linked from [karllorey.com](https://karllorey.com) (my personal website).
For example, with cURL:
```bash
curl --data "url=https://karllorey.com" http:/socials.karllorey.com/api/fetch-url
```

Response:

```json
{
    "matches_per_platform": {
        "facebook": [],
        "twitter": [
            "https://twitter.com/karllorey"
        ],
        "linkedin": [],
        "github": [
            "https://github.com/lorey/karllorey.com",
            "https://github.com/lorey"
        ],
        "email": []
    }
}
```

## Test it (on the website)
There's a page, [socials.karllorey.com/try](http://socials.karllorey.com/try), 
where you can preview the functionality.

## Test it (with the browsable API)
Django REST Framework offers a browsable API where you can test all functionality in the browser.

1. Go to [socials.karllorey.com/api/fetch-url](http://socials.karllorey.com/api/fetch-url)
2. Select for `Media type`: `application/x-www-form-urlencoded`
3. Enter in `Content`: `url=https://karllorey.com` or any other url

![Screenshot of socials API's browsable API](.github/socials-browsable-api.png)

## Set it up for yourself
socials API is dockerized and can be set up via docker-compose within seconds:
```bash
docker-compose build
docker-compose up -f docker-compose.yml -f docker-compose.prod.yml -d
```

It should now be accessible at port 80.
The development version you get with `docker-compose up` is at port 8016.
Make sure to adapt the [rate limit in `socials_api/settings.py`](socials_api/settings.py).

I have personal ansible and terraform files for deployment via docker-compose on AWS.
Reach out if you're interested.

# References
- [socials](https://github.com/lorey/socials), a Python library to check if urls are social media profiles
- [social-media-profiles-regexs](https://github.com/lorey/social-media-profiles-regexs):
  extract urls of social media profiles with regular expressions
