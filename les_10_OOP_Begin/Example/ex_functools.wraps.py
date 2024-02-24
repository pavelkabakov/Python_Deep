"""
@functools.wraps: Этот декоратор используется в создании собственных декораторов. Он помогает сохранить метаданные
декорируемой функции, такие как имя, документацию и список аргументов. Это важно для поддержки интроспекции и отладки.
"""

from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Что-то выполняется перед функцией")
        result = f(*args, **kwargs)
        print("Что-то выполняется после функции")
        return result
    return wrapper
