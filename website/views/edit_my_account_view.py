from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from website.models.profile_model import Profile
from website.forms import MyAccountForm



def edit_my_account(request, user_id):
    """
    Function allowing a user to edit User and Profile information on My Account
    page. 

    ---Arguments---
    request: the full HTTP request object
    user_id: id of current user

    ---GET---
    renders my_account_form.py and prepopulates the fields with info for
    current user. Apart from first name and last name, fields will be empty the
    first time user is accessing this form.

    ---Context---
    'edit_my_account_form': (form): instance of user's current Profile and User
        information

    ---POST---
    Updates my account instance and redirects user back to My Account page

    ---Context---
    'form': instance of user's updated Profile and User information

    Author: Jessica Younker
    """
    if request.method == 'GET':
        template_name = 'edit_my_account.html'
        current_account_info = {
            "first_name": request.user.first_name, 
            "last_name": request.user.last_name, 
            "street_address": request.user.profile.street_address, 
            "city": request.user.profile.city, 
            "state": request.user.profile.state, 
            "postal_code": request.user.profile.postal_code, 
            "phone": request.user.profile.phone}

        edit_my_account_form = MyAccountForm(current_account_info)
        return render(request, template_name, {"edit_my_account_form": edit_my_account_form})

    elif request.method == 'POST':
            form = MyAccountForm(request.POST)
            if form.is_valid():
                form_data = request.POST
                
                updated_user_info = request.user
                updated_user_info.first_name = form.cleaned_data['first_name']
                updated_user_info.last_name = form.cleaned_data['last_name']
                updated_user_info.save()

                updated_account_info = Profile.objects.get(user=request.user)
                updated_account_info.street_address = form.cleaned_data['street_address']
                updated_account_info.city = form.cleaned_data['city']
                updated_account_info.state = form.cleaned_data['state']
                updated_account_info.postal_code = form.cleaned_data['postal_code']
                updated_account_info.phone = form.cleaned_data['phone']
                updated_account_info.save()

                return HttpResponseRedirect(reverse('website:my_account',
                    args=[request.user.id]))

    else:
        return HttpResponseForbidden('''<h1>Not your account, dawg.</h1>
        <img src="/website/static/other.jpg">''')

   