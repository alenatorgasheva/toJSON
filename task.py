import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        result = json.dumps(result)
        return result
    return wrapped
