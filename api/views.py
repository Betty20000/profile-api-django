import requests
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def me(request):
    """
    Returns user profile info with a dynamic cat fact.
    """

    # Fetch cat fact from the external API
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx
        cat_fact = response.json().get("fact", "Cats are awesome!")
    except requests.exceptions.RequestException:
        cat_fact = "Could not fetch cat fact at this time."

    # Current UTC timestamp in ISO 8601 format
    timestamp = datetime.now(timezone.utc).isoformat()

    # Construct the response
    data = {
        "status": "success",
        "user": {
            "email": "beatricegachigi@gmail.com",          # <-- change this
            "name": "Beatrice Gachigi",                  # <-- change this
            "stack": "Python/Django REST Framework"    # <-- change this
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }

    return Response(data, status=status.HTTP_200_OK)
