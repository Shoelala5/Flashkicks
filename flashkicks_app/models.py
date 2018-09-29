from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+.-_]+@[a-zA-Z0-9+.-_]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def signup(self, data):
        errors={}

        if len(data['first']) < 1:
            errors['first'] = 'Pleast enter first name'
        elif len(data['name']) < 2:
            errors['first'] = 'First name must have atleast 2 characters'
        
        if len(data['last']) < 1:
            errors['last'] = 'Pleast enter last name'
        elif len(data['name']) < 2:
            errors['last'] = 'Last name must have atleast 2 characters'

        if len(data['username']) < 1:
            errors['username'] = 'Username is required'
        else:
            existing_username = User.objects.filter(username=data['username'])
            if len(existing_username) > 0:
                errors['username'] = 'Username is already in use'

        if len(data['email']) < 1:
            errors['email'] = 'Email address is required'
        elif not EMAIL_REGEX.match(data['email']):
            errors['email'] = 'Invalid email address'
        else:
            existing_email = User.objects.filter(email=data['email'])
            if len(existing_email) > 0:
                errors['email'] = 'Email address is already in use'

        if len(data['name']) < 8:
            errors['password'] = 'Password name must have atleast 8 characters'
        if data['password'] != data['confirm']
            errors['confirm'] = 'Confirm password does not match with password'
        
        if len(data['address']) < 1:
            errors['address'] = 'Please provide an address'

        if len(errors) == 0:
            return User.objects.create(
                first = data['first'],
                last = data['last'],
                username = data['username'],
                email = data['email'],
                password = data['password'],
                address = data['address']
            )

        else:
            return errors

    def login(self, data):
        errors={}

        if len(data['username']) < 1:
            errors['username'] = 'Username is required'
        else:
            existing_username = User.objects.filt(username=data['username'])
            if len(existing_username) < 1:
                errors['username'] = 'Username is not in use'

        if len(data['password']) < 8:
            errors['password'] = 'Incorrect password'

        if len(errors) == 0:
            stored_password = existing_username[0].password
            if not bcrypt.checkpw(data['password'].encode(), stored_password.encode()):
                errors['password'] = 'Incorrect Password'
                return errors
            else:
                return existing_username[0]

        else:
            return errors


class User(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    objects = UserManager()


# Create your models here.
