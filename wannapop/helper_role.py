from flask import current_app
from flask_login import current_user
from flask_principal import identity_loaded, identity_changed, ActionNeed, Permission, Identity, AnonymousIdentity
from enum import Enum

# Custom roles and actions
class Role(str, Enum):
    admin = "admin"
    moderator = "moderator"
    wanner = "wanner"

class Action(str, Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"

# Needs
__admin_role_need = ActionNeed(Role.admin)
__moderator_role_need = ActionNeed(Role.moderator)
__wanner_role_need = ActionNeed(Role.wanner)

__create_action_need = ActionNeed(Action.create)
__read_action_need = ActionNeed(Action.read)
__update_action_need = ActionNeed(Action.update)
__delete_action_need = ActionNeed(Action.delete)

# Permissions
require_admin_role = Permission(__admin_role_need)
require_moderator_role = Permission(__moderator_role_need)
require_wanner_role = Permission(__wanner_role_need)

require_create_permission = Permission(__create_action_need)
require_read_permission = Permission(__read_action_need)
require_update_permission = Permission(__update_action_need)
require_delete_permission = Permission(__delete_action_need)

@identity_loaded.connect
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'role'):
        if current_user.role == Role.admin:
            # Role needs
            identity.provides.add(__admin_role_need)
            # Action needs
            identity.provides.add(__create_action_need)
            identity.provides.add(__read_action_need)
            identity.provides.add(__update_action_need)
            identity.provides.add(__delete_action_need)
        elif current_user.role == Role.moderator:
            # Role needs
            identity.provides.add(__moderator_role_need)
            # Action needs
            identity.provides.add(__read_action_need)
        elif current_user.role == Role.wanner:
            # Role needs
            identity.provides.add(__wanner_role_need)
            # Action needs
            identity.provides.add(__create_action_need)
            identity.provides.add(__read_action_need)
            identity.provides.add(__update_action_need)
            identity.provides.add(__delete_action_need)
        else:
            current_app.logger.debug("Unkown role")

def notify_identity_changed():
    if hasattr(current_user, 'email'):
        identity = Identity(current_user.email)
    else:
        identity = AnonymousIdentity()
    
    identity_changed.send(current_app._get_current_object(), identity=identity)
