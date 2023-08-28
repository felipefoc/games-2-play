from models.users import User

def get_current_user(request):
    token = request.headers.get('X-API')
    return User().get_by_token(token)