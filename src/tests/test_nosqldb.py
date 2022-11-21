import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize("provider", ["AWS", "GCP"])
def test_nosqldb_imports(provider: str):
    MonkeyPatch().setenv('PROVIDER', provider)
    MonkeyPatch().setenv('AWS_DEFAULT_REGION', 'eu-west-2')
    from yasf.nosqldb import client
    assert client
