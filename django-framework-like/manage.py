from wsgiref.simple_server import make_server

def application(environ, start_response):
  """callable object of WSGI"""

  # setting HTTP Response Header
  start_response('200 OK', [('Content-type', 'text/plain')])

  # HTTP Response boby
  msg = 'Hello, World'
  return [msg.encode('utf-8')]


if __name__ == '__main__':
  # move WSGI application
  with make_server('', 8000, application) as httpd:
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()

