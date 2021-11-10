from django.contrib.auth import authenticate,login,logout

import datetime


def get_years_range(start_year=1950):
    """
    Using in forms ,this function for
     get years list for birthday fields
    """
    birth_years_range=[]
    a = start_year
    for i in range(100):
        a +=1 
        if a == 2021:
            break
        birth_years_range.append(a)
    return birth_years_range


def check_user_auth(request,cleaned_data):

    """"
    
    User's Authenticate checking function

    """
    user = authenticate(request,username=cleaned_data['username'],
                        password=cleaned_data['password'])
    if user is not None:
        if user.is_active:
            login(request,user)
            return user
        else:
            return 'Disabled account'
    else:
        return None