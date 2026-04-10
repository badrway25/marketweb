"""Template helpers for preview compositions.

These filters exist so that DNA-driven compositions can iterate over
content lists and pull the matching image out of the shared imagery
list by integer index — something the stock Django template language
cannot do natively.
"""
from django import template

register = template.Library()


@register.filter(name="at")
def at(seq, i):
    """Return ``seq[int(i)]`` or empty string if out of range / invalid.

    Usage:
        {% for sp in dna.content.specialties %}
            {{ imagery|at:forloop.counter }}
        {% endfor %}

    Falls back to the first element when the requested index overflows
    so a missing photo never blows up a screenshot run.
    """
    try:
        idx = int(i)
    except (TypeError, ValueError):
        return ""
    if not seq:
        return ""
    if 0 <= idx < len(seq):
        return seq[idx]
    return seq[0]
