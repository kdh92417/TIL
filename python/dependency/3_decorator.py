

def logger(log_type):

    def logger_decorator(func):
        def wrapper(self, request, *args, **kwargs):
            print(f'[{log_type}] 요청이 들어왔습니다 - ', request)
            return func(self, request, *args, **kwargs)
        return wrapper
    return logger_decorator

class Handler:

    def __init__(self):
        pass

    @logger('info')
    def handleRequest(self, request):
        print("request를 처리했습니다.")

h = Handler()
h.handleRequest('요청입니다.!!')