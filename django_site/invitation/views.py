from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Page
import string, random


def create_page(request):
    """Creates a new page with random url and permissions"""
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        # Generate a random 5 letter name for the page.
        code = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

        # Check if the page with the generated code already exists.
        while Page.objects.filter(code=code).exists():
            code = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

        # Create a new page object and save it to the database.
        page = Page(title=title, content=content, code=code, owner=request.user)
        page.save()

        # Create a permission for the page.
        permission = Permission.objects.create(
            codename='view_{}'.format(page.code),
            name='Can view page {}'.format(page.code),
            content_type=ContentType.objects.get_for_model(Page)
        )

        # Add the permission to the page's owner.
        page.owner.user_permissions.add(permission)

        url = reverse('page', kwargs={'code': code})
        return redirect(url)
    else:
        return render(request, 'create_page')

def page(request, code):
    page = None
    try:
        page = Page.objects.get(code=code)
    except Page.DoesNotExist:
        raise Http404('Page not found.')

    return render(request, 'template_page.html', {'page': page})



def group_page(request, code):
    # Check if the user has permission to view the group page.
    if not request.user.has_perm('view_{}'.format(code)):
        raise PermissionDenied()

    # ...

    return render(request, 'group_page.html')