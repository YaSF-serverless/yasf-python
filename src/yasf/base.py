from functools import wraps
import importlib
from typing import Callable

import os

base_providers = {
    "AWS": ".aws.aws",
    "GCP": ".gcp.gcp"
}

provider_env = os.getenv('PROVIDER')
provider_path = base_providers[provider_env]

provider = importlib.import_module(provider_path, "yasf")


def entrypoint_decorator(handler: Callable):
    """
    Handler decorator to convert provided specific arguments into standard GenericContext code.
    """
    @wraps(handler)
    def standardise_parameters(*args, **kwargs):
        # Parse the arguments into a standard format
        parsed_args = provider.parse_args(*args, **kwargs)

        # Execute the handler function
        response = handler(*parsed_args)

        # Format the response to the provider's standard
        return provider.format_output(response)

    return standardise_parameters
