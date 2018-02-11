from wsgiref.simple_server import make_server
from wsgiref.validate import validator
from core.wsgi import WSGIHandler


def runserver(ip='127.0.0.1', port='8000'):
    """run develop server"""
    application = validator(WSGIHandler())
    
    # move WSGI application
    with make_server('0.0.0.0', int(port), application) as httpd:
        print('Serving HTTP on {}:{}...'.format(ip, port))
        httpd.serve_forever()


if __name__ == '__main__':
    try:
        runserver()
    except KeyboardInterrupt:  # Input <C-c>
        print('Stop server')
        pass
