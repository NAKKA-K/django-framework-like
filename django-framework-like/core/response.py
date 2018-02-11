from http.client import responses
from wsgiref.headers import Headers
from core.wsgi import cast_finish_response


class HttpResponse:
    """Strage HttpResponse class"""

    def __init__(self, content=b'',
                 content_type='text/html; charset=UTF-8', status_code=200):
        if isinstance(content, str):
            self.content = content
        elif isinstance(content, str):
            self.content = content.encode('utf-8')

        self.content_type = content_type
        self.status_code = status_code
        self.reason_phrase = responses.get(status_code, 'Unknown Status Code')
        self.headers = [
            ('Content-Type', self.content_type),
            ('Content-Length', str(len(self.content)))
        ]
        self.headers_dict = Headers(self.headers)

    def __iter__(self):
        return cast_finish_response(self.content)
