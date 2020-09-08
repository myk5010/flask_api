from ..utils import PatchedApi
# from .example import ns as example_ns
from .account import ns as account_ns

api = PatchedApi()

# api.add_namespace(example_ns)
api.add_namespace(account_ns)
