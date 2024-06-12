# context_processors.py
from .models import User

def custom_user(request):
    user_id = request.session.get('current_user_id')
    if user_id:
        try:
            user = User.objects.get(user_id=user_id)
            return {'current_user': user}
        except User.DoesNotExist:
            pass
    return {'current_user': None}
