from django.contrib.auth.models import Group
from .models import UserAccount

def create_account(email, first, last, password):
    '''
    Create a new user account
    '''
    user = UserAccount.objects.create_user(email, email, password)
    user.first_name = first
    user.last_name = last
    user.save()
    return user

def update_account_data(user, email, first, last, birthday):
    '''
    Update the user with info from the accountInfo dictionary
    '''
    user.email = email
    user.first_name = first
    user.last_name = last
    if birthday != '':
        user.birthday = birthday
    user.save()

def add_funds(user, amount):
    # print("Adding " + str(amount) + " to " + str(user.funds))
    user.funds = user.funds + amount
    # print("Final: " + str(user.funds))
    user.save()
    pass