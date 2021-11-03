from django.contrib.auth import authenticate,login,logout



def check_user_auth(request,cleaned_data):

    """"
    
    User's Authenticate checking function

    """
    user = authenticate(request,username=cleaned_data['username'],password=cleaned_data['password'])
    if user is not None:
        if user.is_active:
            login(request,user)
            return user
        else:
            return 'Disabled account'
    else:
        return None