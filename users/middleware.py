# users/middleware.py

from django.shortcuts import redirect
from django.urls import reverse, NoReverseMatch
from django.conf import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Список ИМЕН URL, которые будут доступны без аутентификации
        exempt_url_names = [
            'login',
            'users:signup',
            'password_reset',
            'password_reset_done',
            'password_reset_confirm',
            'password_reset_complete',
        ]

        self.exempt_paths = []
        for name in exempt_url_names:
            try:
                self.exempt_paths.append(reverse(name))
            except NoReverseMatch:
                pass

        try:
            self.admin_path = reverse('admin:index')
        except NoReverseMatch:
            self.admin_path = '/admin/'

    def __call__(self, request):
        if not request.user.is_authenticated:
            is_exempt = any(request.path.startswith(path) for path in self.exempt_paths)
            is_admin = request.path.startswith(self.admin_path)

            if not is_exempt and not is_admin:
                login_url = reverse(settings.LOGIN_URL)
                return redirect(f'{login_url}?next={request.path}')

        response = self.get_response(request)
        return response
