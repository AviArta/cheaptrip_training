from time import perf_counter


def working_time_decorator(some_function):
    
    def new_function(*args, **kwargs):
        start_time = perf_counter()
        result = some_function(*args, **kwargs)
        working_time = perf_counter() - start_time
        print(f"Working time of function '{some_function.__name__}' = {working_time} сек.")
        return result
    
    return new_function