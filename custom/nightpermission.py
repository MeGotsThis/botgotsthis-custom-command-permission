from typing import Optional
from lib.data import CustomFieldArgs


async def fieldNightPermission(args: CustomFieldArgs) -> Optional[str]:
    if args.field.lower() in ['night-permission', 'night-level']:
        prefix: str = args.prefix or ''
        suffix: str = args.suffix or ''
        if args.permissions.owner:
            return prefix + 'owner' + suffix
        if args.permissions.broadcaster:
            return prefix + 'broadcaster' + suffix
        if args.permissions.moderator:
            return prefix + 'moderator' + suffix
        if args.permissions.subscriber:
            return prefix + 'subscriber' + suffix
        return prefix + 'everyone' + suffix
    return None
