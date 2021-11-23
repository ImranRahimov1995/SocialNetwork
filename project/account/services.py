import datetime

from django.contrib.auth import authenticate, login, logout
from friendship.models import FriendshipRequest


def check_accepted_fr_req(profile1, profile2):
    check = profile2.received_requests.filter(user_from=profile1,
                                              accepted=True)
    #   Есть его запрос дружбы,
    second_check = profile1.received_requests.filter(user_from=profile2,
                                                     accepted=True)

    if check:
        return check[0]
    elif second_check:
        return second_check[0]
    else:
        return False


def check_friendship_request(profile1, profile2):
    # has request not accepted from me,
    check = profile2.received_requests.filter(user_from=profile1,
                                              accepted=False)

    if check:
        return check[0]

    else:
        return False


# in devoloping ,need optimization,
def check_friendship(my_profile, profile):
    """

    Using in handler profile detail*
    Using for checking friendship of two profiles

    return boolean which i used in templates
    """
    for x in profile.friends.all():
        if x == my_profile:
            return True

    return False


def get_years_range(start_year=1950):
    """
    Using in forms ,this function for
     get years list for birthday fields
    """
    birth_years_range = []
    a = start_year
    for i in range(100):
        a += 1
        if a == 2021:
            break
        birth_years_range.append(a)
    return birth_years_range


def check_user_auth(request, cleaned_data):
    """"
    
    User's Authenticate checking function

    """
    user = authenticate(request, username=cleaned_data['username'],
                        password=cleaned_data['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            return user
        else:
            return 'Disabled account'
    else:
        return None
