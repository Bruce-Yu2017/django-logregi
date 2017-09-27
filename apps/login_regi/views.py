# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt

def index(request):
  request.session['log'] = False
  return render(request, 'login_regi/index.html')

def regi(request):
  if request.method == "POST":
    print request.POST['email']
    request.session['loginregi'] = 'regi'
    errors = User.objects.create_validator(request.POST)
    if len(errors):
      for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags = tag)
      return redirect('/')
   
    exist = User.objects.filter(email = request.POST['email'])
    if exist:
      messages.error(request, "Please enter a valid email", extra_tags = 'email')
      return redirect('/')
    
    salted_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = salted_password)
    request.session['log'] = True
    request.session['user_id'] = User.objects.last().id
    return redirect('/success')  
  return redirect('/')

def login(request):
  if request.method == 'POST':
    request.session['loginregi'] = 'log'
    exist = User.objects.filter(email = request.POST['email'])
    if exist and bcrypt.checkpw(request.POST['password'].encode(), exist[0].password.encode()):
      request.session['log'] = True
      request.session['user_id'] = exist[0].id
      return redirect('/success')
    else:
      messages.error(request, "Your email and password are not match", extra_tags = "login")
      return redirect('/')

  return redirect('/')

def success(request):
  # if request.session['loginregi'] == 'log' and request.session['log']:
  if request.session['log']:
    user = User.objects.get(id = request.session['user_id'])
    context = {
      'user': user
    }
    return render(request, "login_regi/success.html", context)
  return redirect('/')






















