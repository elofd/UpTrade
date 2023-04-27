from django import template
from django.core.exceptions import ObjectDoesNotExist
from menu.models import MenuItem, Menu


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_title, active_item=''):
    try:
        menu_items = Menu.objects.get(title=menu_title).items.all()
    except ObjectDoesNotExist:
        menu_items = []
    menu_output = generate_menu(menu_items, int(active_item))
    return menu_output


def generate_menu(menu_items, active_item_id=None):
    output = '<ul class="menu">'
    for item in menu_items:
        child_items = item.children.all()
        children_output = ''
        if child_items:
            children_output = generate_menu(child_items, active_item_id)
        class_name = ''
        if item.id == active_item_id:
            class_name = 'class="active"'
        output += '<li{class_name}s><a href="{item_url}s">{item_title}s</a>{children_output}s</li>'.format(
            class_name=class_name, item_url=item.url, item_title=item.title, children_output=children_output
        )
    output += '</ul>'
    return output