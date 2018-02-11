class WSGIRequest:
    """Create request object class"""

    def __init(self, environ):
        self.environ = environ
        self.path_info = environ['PATH_INFO']


class WSGIHandler:
    """WSGI application class"""

    request_class = WSGIRequest

    def __call__(self, environ, start_response):
        """WSGI interface"""
        request = self.request_class(environ)
        response = self.get_response(request)
        status = '{} {}'.format(response.status_code, response.reason_phrase)
        start_response(status, response.headers)
        return response

    def get_response(self, request):
        """call view, and return HttpResponse object"""
        from core.response import HttpResponse
        return HttpResponse('Hello World')


