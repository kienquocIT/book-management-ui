from functools import wraps

import jwt
from django.shortcuts import redirect, render
from jwt import ExpiredSignatureError, InvalidTokenError
from rest_framework import status

from ui import settings


def mask_view(auth_require=False, admin_require=False, template=None, response_key=""):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(self, request, *args, **kwargs):
            token = request.COOKIES.get("access_token")

            if auth_require:
                if not token:
                    return redirect('authentication:AuthenticationLogin')
                try:
                    payload = jwt.decode(
                        token,
                        settings.SECRET_API_KEY,
                        algorithms=["HS256"],
                    )
                    print(payload)
                    if admin_require:
                        if not payload["is_superuser"]:
                            return redirect('book:BookListView')
                except (ExpiredSignatureError, InvalidTokenError):
                    return redirect("authentication:AuthenticationLogin")

            result = view_func(self, request, *args, **kwargs)

            if isinstance(result, tuple):
                context, status_code = result
            else:
                context, status_code = result, status.HTTP_200_OK
            if template:
                return render(request, template, {response_key or 'data': context}, status=status_code)
            return context
        return _wrapped_view
    return decorator