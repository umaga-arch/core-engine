# utils.py

import logging
from typing import Any, Dict, List

class _SingletonMeta(type):
    _instances: Dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class _Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def info(self, message: str):
        self.logger.info(message)

    def warn(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

def get_logger() -> _Logger:
    return _Logger()

def deep_merge(dict1: Dict, dict2: Dict) -> Dict:
    merged = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged

def flatten_dict(nested: Dict) -> Dict:
    def flatten(x: Dict, parent_key: str = '', sep: str = '.'):
        result: Dict = {}
        for k, v in x.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, Dict):
                result.update(flatten(v, new_key, sep))
            else:
                result[new_key] = v
        return result
    return flatten(nested)