__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from ._wrapped_ml_client import get_ml_client

__all__ = [
    "get_ml_client",
]
