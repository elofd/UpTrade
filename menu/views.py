from django.shortcuts import redirect, get_object_or_404
from .models import MenuItem


def menu_redirect_view(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    return redirect(menu_item.url)
