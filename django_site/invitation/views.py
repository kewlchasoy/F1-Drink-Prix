from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Page

def create_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        # Generate a random 5-letter code.
        code = ''.join(random.choice(string.ascii_lowercase) for i in range(5))

        # Create a new page object and save it to the database.
        page = Page(title=title, content=content, code=code)
        page.save()

        # Redirect the user to the new page.
        return redirect('page', code=code)

    else:
        return render(request, 'create_page.html')
    


def invite_user(request, code):
    if request.method == 'POST':
        email = request.POST['email']

        # Get the page object for the given code.
        page = Page.objects.get(code=code)

        # Send an email to the invited user.
        send_mail(
            'Invitation to page',
            'You have been invited to the page {}.'.format(page.title),
            'me@example.com',
            [email],
            fail_silently=False
        )

        # Redirect the user to the page.
        return redirect('page', code=code)

    else:
        return render(request, 'invite_user.html', {'code': code})