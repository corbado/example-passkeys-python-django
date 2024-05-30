from corbado_python_sdk import Config, CorbadoSDK, SessionInterface, UserEntity
from django.http import HttpResponse
from django.shortcuts import redirect, render
from werkzeug.exceptions import Unauthorized

from passkeys_demo.settings import API_SECRET, PROJECT_ID

# Config has a default values for 'short_session_cookie_name' and 'BACKEND_API'
config: Config = Config(
    api_secret=API_SECRET,
    project_id=PROJECT_ID,
)

# Initialize SDK
sdk: CorbadoSDK = CorbadoSDK(config=config)
sessions: SessionInterface = sdk.sessions


def index(request) -> HttpResponse:
    context = {
        "PROJECT_ID": PROJECT_ID,
    }
    return render(request, "index.html", context)


def profile(
    request,
) -> HttpResponse:
    token = request.COOKIES.get(config.short_session_cookie_name)

    try:
        if not token:
            raise ValueError("No token found")

        user: UserEntity = sessions.get_current_user(short_session=token)
        if user.authenticated:
            context = {
                "request": request,
                "PROJECT_ID": PROJECT_ID,
                "USER_ID": user.user_id,
                "USER_NAME": user.name,
                "USER_EMAIL": user.email,
            }

            return render(request, "profile.html", context)
        else:
            raise Unauthorized()

    except Exception as e:
        print(e)
        return redirect("/")
