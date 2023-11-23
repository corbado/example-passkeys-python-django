from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
import requests
from jose import jwt
from passkeys_demo.settings import PROJECT_ID, API_SECRET

# Session config
short_session_cookie_name = "cbo_short_session"
issuer = f"https://{PROJECT_ID}.frontendapi.corbado.io"
jwks_uri = f"https://{PROJECT_ID}.frontendapi.corbado.io/.well-known/jwks"


def index(request):
    context = {
        'PROJECT_ID': PROJECT_ID,
    }
    return render(request, "index.html", context)

def profile(request):
    token = request.COOKIES.get(short_session_cookie_name)

    try:
        if not token:
            raise ValueError("No token found")

        response = requests.get(jwks_uri)
        response.raise_for_status()

        jwks = response.json()
        public_key = jwks["keys"][0]

        payload = jwt.decode(
            token,
            key=public_key,
            algorithms=["RS256"],
            audience=API_SECRET,
            issuer=issuer,
        )

        if payload["iss"] != issuer:
            raise ValueError("Invalid issuer")

        context = {
            'PROJECT_ID': PROJECT_ID,
            'USER_ID': payload["sub"],
            'USER_NAME': payload.get("name"),
            'USER_EMAIL': payload.get("email"),
         }

        return render(request, "profile.html", context)
    
    except Exception as e:
        print(e)
        return redirect("/")

