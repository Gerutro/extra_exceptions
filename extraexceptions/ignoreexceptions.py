def ignore_exc_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            fnc = func(*args, **kwargs)
            return fnc
        except Exception as e:
            print(f"Exception>>> {e}")
            return
    return wrapper
