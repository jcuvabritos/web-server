from wsgiref.simple_server import make_server
import json


def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "application/json")]
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO').split('/')
    response_body = b""
    tasks = dict()

    if len(path) == 2 and path[1] == 'tasks':

        if method == 'GET':
            response_body = json.dumps(list(tasks.values())).encode("utf-8")

    elif len(path) == 3 and path[1] == 'tasks' and path[2].isdigit():

        if method == 'GET':
            id = int(path[2])
            if id in tasks:
                response_body = json.dumps(tasks.get(id)).encode("utf-8")
            else:
                status = "404 Not Found"
    
    else:
        pass


    start_response(status, headers)

    return [response_body]

with make_server("", 9292, app) as httpd:
    print("Listening on http://localhost:9292")
    httpd.serve_forever()