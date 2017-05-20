from django.shortcuts import redirect
from users.models import Account


def load_user(**kwargs):
    # Load user into pipeline
    try:
        user_id = kwargs['strategy'].session_get('user_id')
        user = Account.objects.get(pk=user_id)
        kwargs['user'] = user
    except:
        pass

    return kwargs