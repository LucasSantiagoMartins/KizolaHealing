from rolepermissions.roles import AbstractUserRole


class Patient(AbstractUserRole):
    available_permissions = {
        'can_add_profile': True,
        'can_view_profile': True,
        'can_change_profile': True,
        'can_delete_profile': True,
        'can_add_consultation': True,
        'can_view_consultation': True,
        'can_change_consultation': True,
        'can_delete_consultation': True,
    }   
