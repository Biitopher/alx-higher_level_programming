#!/usr/bin/python3
"""Defines function that returns dictionary description"""


def class_to_json(obj):
    """Represents class to json"""
    if isinstance(obj, (list, tuple)):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {class_to_json(key): class_to_json(value)
                for key, value in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, (int, float, bool)):
        return obj
    else:
        return {key: class_to_json(getattr(obj, key))
                for key in dir(obj) if not key.startswith('__')}
