import string, random

from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseForbidden
from .models import Page

@login_required
def create_page(request):
  """Creates a new page with random url and group"""
  if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']

    # Generate a random 6 letter name for the page.
    code = ''.join(random.choices(string.ascii_lowercase, k=6))

    # Check if the page with the generated code already exists.
    while Page.objects.filter(code=code).exists():
      code = ''.join(random.choices(string.ascii_lowercase, k=6))

    # Create a new page object and save it to the database.
    page = Page(title=title, content=content, code=code, owner=request.user)
    page.save()

    # Create groups for the page.
    group_users = Group.objects.create(name='Users of {}'.format(page.code))
    group_admins = Group.objects.create(name='Admins of {}'.format(page.code))

    # Add the page's users and admins to the group.
    group_users.user_set.add(request.user)
    group_admins.user_set.add(request.user)


    url = reverse('page', kwargs={'code': code})
    return redirect(url)
  else:
    return render(request, 'create_page')


@login_required
def page(request, code):
  page = get_object_or_404(Page, code=code)

  # Check if the user has a group that contains the page.
  if not check_if_user_in_group(request.user, 'Users of {}'.format(page.code)):
    # The user does not have a group that contains the page.
    return HttpResponseForbidden()

  # The user has a group that contains the page.
  return render(request, 'template_page.html', {'page': page})


def check_if_user_in_group(user, group_name):

  group = Group.objects.get(name=group_name)
  return user in group.user_set.all()


def add_user(request, code):
  page = get_object_or_404(Page, code=code)

  if request.method == 'POST':
    username = request.POST['username']

  # Gets the username from the forms field and the current group for the page.
  user_id = User.objects.get(username=username)
  group = group = Group.objects.get(name='Users of {}'.format(page.code))

  # Check if the user is already in the group.
  if check_if_user_in_group(user_id, group):
    # The user is already in the group.
    messages.warning(request, "User already in group.")
  else:
    # Add the user to the group.
    group.user_set.add(user_id)
    messages.success(request, "User added to group.")

  return redirect('/group/{}/'.format(page.code))