from django.utils.deprecation import MiddlewareMixin


# django 解决使用django rest framework时web请求报CSRF Failed: CSRF cookie not set
class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
