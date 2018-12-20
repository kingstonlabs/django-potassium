import random
import string

from django import template
from sorl.thumbnail import get_thumbnail

register = template.Library()


@register.simple_tag
def get_random_id(length=6):
    return ''.join([
        random.choice(string.ascii_lowercase) for i in range(length)
    ])


@register.inclusion_tag('potassium/_flexi_image.html')
def render_flexi_image(image):
    return {
        'element_id': get_random_id(),
        'thumbnails': [
            {
                'min_width': 0,
                'image': get_thumbnail(image, "800"),
            },
            {
                'min_width': 800,
                'image': get_thumbnail(image, "1170"),
            },
            {
                'min_width': 1170,
                'image': get_thumbnail(image, "1440"),
            },
            {
                'min_width': 1440,
                'image': get_thumbnail(image, "1920"),
            }
        ]
    }
