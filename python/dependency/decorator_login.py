

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):

        if request['id'] == 'admin':
            print('관리자에요')
            return func(self, request, *args, **kwargs)
        else:
            print('일반 사용자네요')
            return


    return wrapper


class Handler:
    def __init__(self):
        pass

    @login_decorator
    def admin_something(self, request):
        print("관리자 기능을 실행합니다.")

h = Handler()
h.admin_something({
    'id' : 'admin',
    'password' : 'world'
})