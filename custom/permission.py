from typing import List, Optional  # noqa: F401
from lib.data import CustomFieldArgs


async def fieldPermission(args: CustomFieldArgs) -> Optional[str]:
    if args.field.lower() in ['permission', 'level']:
        prefix: str = args.prefix or ''
        suffix: str = args.suffix or ''
        if args.permissions.owner:
            return prefix + 'owner' + suffix
        if args.permissions.twitchStaff:
            return prefix + 'staff' + suffix
        if args.permissions.twitchAdmin:
            return prefix + 'admin' + suffix
        if args.permissions.globalModerator:
            return prefix + 'globalmod' + suffix
        if args.permissions.broadcaster:
            return prefix + 'broadcaster' + suffix
        if args.permissions.moderator:
            return prefix + 'moderator' + suffix
        if args.permissions.subscriber:
            return prefix + 'subscriber' + suffix
        return args.default or ''
    return None


async def fieldMultiPermission(args: CustomFieldArgs) -> Optional[str]:
    if args.field.lower() in ['multipermission', 'multilevel',
                              'multi-permission', 'multi-level']:
        prefix: str = args.prefix or ''
        suffix: str = args.suffix or ''
        permissions: List[str] = []
        if args.permissions.owner:
            permissions.append('owner')
        elif args.permissions.twitchStaff:
            permissions.append('staff')
        elif args.permissions.twitchAdmin:
            permissions.append('admin')
        elif args.permissions.globalModerator:
            permissions.append('globalmod')
        elif args.permissions.broadcaster:
            permissions.append('broadcaster')
        elif args.permissions.moderator:
            permissions.append('moderator')
        if args.permissions.subscriber:
            permissions.append('subscriber')
        if permissions:
            return prefix + ','.join(permissions) + suffix
        return args.default or ''
    return None
