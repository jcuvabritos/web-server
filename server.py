from wsgiref.simple_server import make_server
import json

tasks = dict()
id = 0

def app(environ, start_response):
    global tasks
    global id

    status = "200 OK"
    headers = [("Content-Type", "application/json")]
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO').split('/')
    response_body = b""

    if len(path) == 2 and path[1] == 'tasks':

        if method == 'GET':
            response_body = json.dumps(list(tasks.values())).encode("utf-8")

        elif method == 'POST':
            id += 1
            status = "201 Created"
            content_length = int(environ.get('CONTENT_LENGTH'))

            input = environ['wsgi.input']
            body = input.read(content_length)

            new_task = json.loads(body)
            new_task['id'] = id
            tasks[id] = new_task

            response_body = json.dumps(new_task).encode("utf-8")

        else: 
            status = "405 Method Not Allowed" 

    elif len(path) == 3 and path[1] == 'tasks' and path[2].isdigit():

        if method == 'GET':
            id = int(path[2])
            if id in tasks:
                response_body = json.dumps(tasks.get(id)).encode("utf-8")
            else:
                status = "404 Not Found"

        elif method == 'PATCH':
            id = int(path[2])
            if id in tasks:
                content_length = int(environ.get('CONTENT_LENGTH'))

                input = environ['wsgi.input']
                body = input.read(content_length)


                task_data = json.loads(body)
                tasks[id].update(task_data)


                response_body = json.dumps(tasks[id]).encode("utf-8")
            else: 
                status = "404 Not Found"

        elif method == 'DELETE':
            id = int(path[2])
            if id in tasks: 
                del tasks[id]
                status = "204 No Content"
            else: 
                status = "404 Not Found"

        else: 
            status = "405 Method Not Allowed"

    else:
        status = "404 Not Found"


    start_response(status, headers)

    return [response_body]

with make_server("", 9292, app) as httpd:
    print("Listening on http://localhost:9292")
    httpd.serve_forever()