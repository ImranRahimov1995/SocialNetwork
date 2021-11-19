import datetime

from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from friendship.models import FriendshipRequest


def check_sended_fr(profile1,profile2):
    check = profile2.fr_request.filter(user_from=profile1,accepted=False)

    if check:
        return True
    else:
        return False


# in devoloping ,need optimization,
def check_friendship(user, profile):
    """

    Using in handler profile detail*
    Using for checking friendship of two profiles

    return boolean which i used in templates
    """

    check = FriendshipRequest.objects.filter(
        Q(Q(user_from=user.pk) & Q(user_to=profile.pk)) &
        Q(accepted=True)
    )
    check_two = FriendshipRequest.objects.filter(
        Q(Q(user_from=profile.pk) & Q(user_to=user.pk)) &
        Q(accepted=True)
    )

    if check or check_two:
        return True
    else:
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
