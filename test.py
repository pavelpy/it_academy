
def application(env, start_response):
    start_response('200 OK', [('Contet-Type', 'text/html')])
    return [b"Hello World"]