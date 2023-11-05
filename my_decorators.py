from datetime import datetime


def working_time_decorator(some_function):
    
    def new_function(*args, **kwargs):
        start_time = datetime.now()
        result = some_function(*args, **kwargs)
        working_time = round((datetime.now() - start_time).total_seconds(), 4)
        print(f"Working time of function '{some_function.__name__}' = {working_time} сек.")
        return result
    
    return new_function