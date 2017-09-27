from typing import Collection, Iterable

from lib.data import CustomCommandField, CustomCommandProcess

from ..custom import permission
from ..custom import nightpermission


def fields() -> Iterable[CustomCommandField]:
    yield permission.fieldPermission
    yield permission.fieldMultiPermission
    yield nightpermission.fieldNightPermission


def properties() -> Collection[str]:
    return []


def postProcess() -> Iterable[CustomCommandProcess]:
    return []
