from typing import List
from corbado_python_sdk import Config, CorbadoSDK, SessionService, UserEntity
from corbado_python_sdk.entities.session_validation_result import (
    SessionValidationResult,
)
from corbado_python_sdk.generated.models.identifier import Identifier
from corbado_python_sdk.services import IdentifierService
from django.http import HttpResponse
from django.shortcuts import redirect, render

from passkeys_demo.settings import API_SECRET, PROJECT_ID

# Config has a default values for 'short_session_cookie_name' and 'BACKEND_API'
config: Config = Config(
    api_secret=API_SECRET,
    project_id=PROJECT_ID,
)

# Initialize SDK
sdk: CorbadoSDK = CorbadoSDK(config=config)
sessions: SessionService = sdk.sessions
identifiers: IdentifierService = sdk.identifiers


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
        validation_result: SessionValidationResult = (
            sessions.get_and_validate_short_session_value(short_session=token)
        )
        if validation_result.authenticated:

            email_identifiers: List[Identifier] = (
                identifiers.list_all_emails_by_user_id(
                    user_id=validation_result.user_id
                    or ""  # at this point user_id should be non empty string since user was authenticated
                )
            )
            user: SessionValidationResult = sessions.get_current_user(
                short_session=token
            )

            context = {
                "request": request,
                "PROJECT_ID": PROJECT_ID,
                "USER_ID": user.user_id,
                "USER_NAME": user.full_name,
                "USER_EMAIL": email_identifiers[0].value,
            }

            return render(request, "profile.html", context)
        else:
            return HttpResponse(
                "You are not authenticated or have not yet confirmed your email.",
                status=401,
            )

    except Exception as e:
        print(e)
        return redirect("/")
