from wsgiref.simple_server import make_server
from wsgiref.validate import validator
from core.wsgi import WSGIHandler


def runserver(ip='127.0.0.1', port='8000'):
    """run develop server"""
    application = validator(WSGIHandler())
    
    # move WSGI application
    with make_server(ip, int(port), application) as httpd:
        print('Serving HTTP on {}:{}...'.format(ip, port))
        httpd.serve_forever()


if __name__ == '__main__':
    from sys import argv

    try:
        if len(argv) == 2:
            ip_status = argv[1].split(':')  
            runserver(ip_status[0], ip_status[1])
        else:
            runserver()
    except KeyboardInterrupt:  # Input <C-c>
        print('Stop server')
        pass
