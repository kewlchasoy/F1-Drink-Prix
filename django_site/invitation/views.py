from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Page
import string, random


def create_page(request):
  if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']

    # Generate a random 6 letter name for the page.
    code = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

    # Create a new page object and save it to the database.
    page = Page(title=title, content=content, code=code)
    page.save()

    # Redirect the user to the new page.
    url = reverse('page', kwargs={'code': code})
    return redirect(url)

  else:
    return render(request, 'create_page.html')

def page(request, code):
  page = Page.objects.get(code=code)
  return render(request, 'page.html', {'page': page})
    


# def invite_user(request, code):
#     if request.method == 'POST':
#         email = request.POST['email']

#         # Get the page object for the given code.
#         page = Page.objects.get(code=code)

#         # Send an email to the invited user.
#         send_mail(
#             'Invitation to page',
#             'You have been invited to the page {}.'.format(page.title),
#             'me@example.com',
#             [email],
#             fail_silently=False
#         )

#         # Redirect the user to the page.
#         return redirect('page', code=code)

#     else:
#         return render(request, 'invite_user.html', {'code': code})


# def generate_code(length = 6):
#     characters = 'abcdefghjkmnpqrstuvwxyz23456789'
#     code = ''
#     for i in range(length):
#         code += random.choice(characters)
#     return code