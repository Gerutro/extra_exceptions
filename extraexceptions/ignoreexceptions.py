def ignore_exc_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Exception>>> {e}")
            return
    return wrapper
