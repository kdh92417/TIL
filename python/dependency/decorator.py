
''' 함수형 Decorator
def decorator(func):
    def wrapper(*args, **kwargs):
        print("전처리")

        func(*args, **kwargs)

        print("후처리")

    return wrapper

@decorator
def test():
    print("함수 내부")

test()
'''

# class 형 Decorator


class Decorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("전처리")
        self.function(*args, **kwargs)
        print("후처리")

@Decorator
def test():
    print("함수 실행")


test()