import bleach
from markdown import markdown
from django.utils.safestring import mark_safe


class MarkdownType(str):
    def as_html(self):
        return render_markdown_as_html(str(self))


def render_markdown_as_html(content):
    """
    Converts markdown to html and marks it safe for django.
    """
    return mark_safe(
        markdown(
            bleach.clean(content, tags=[]),
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.nl2br',
                'markdown.extensions.sane_lists'
            ]
        )
    )
