# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
  def create_validator(self, postData):
    errors = {}
   
    if len(postData['first_name']) < 2:
      errors['first_name'] = "Your first name need to more than 2 characters."
    if not NAME_REGEX.match(postData['first_name']):
      errors['first_name'] = "First name should contain letter only."
    if len(postData['last_name']) < 2:
      errors['last_name'] = "Your last name need to more than 2 characters."
    if not NAME_REGEX.match(postData['last_name']):
      errors['last_name'] = "Last name should contain letter only."
    if len(postData['email']) < 1:
      errors['email'] = "Please enter your email address."
    if not EMAIL_REGEX.match(postData['email']):
      errors['email'] = 'Please enter a valid email address.'
    if len(postData['password']) < 8:
      errors['password'] = "Your password need to more than 8 characters."
    if postData['password'] != postData['confirm_pw']:
      errors['password'] = "Please confirm your password."
    return errors

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  objects = UserManager()












