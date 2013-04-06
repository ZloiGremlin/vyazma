# vim:fileencoding=utf-8
from django import template
import string
import re
from urllib import urlencode

register = template.Library()


def arrayValues(value):
    if value:
        if value[-1] == '-': value = value[0:len(value) - 1]
        s = value.split('-')
        return [int(x) for x in s]
    return []


def price_format(value):
    decimal_points = 3
    seperator = u' '
    value = str(value)
    if len(value) <= decimal_points:
        return value
    parts = []
    while value:
        parts.append(value[-decimal_points:])
        value = value[:-decimal_points]
    parts.reverse()
    return seperator.join(parts)


def encode_parameters(value, arg):
    s = {}
    e_s = {}
    s.update(value)
    for k, v in s.items():
        if not isinstance(v[0], unicode):
            v[0] = v[0].encode('utf-8')
        e_s[k] = v[0]
    s = e_s
    if s.__contains__('page'):
        s.__setitem__('page', arg)
    else:
        s.__setitem__('page', arg)
    s = urlencode(s, doseq=True)
    return s


def cut_values(value, arg):
    return value[:arg]


def list(value):
    paras = re.split(r'[\r\n]+', value)
    strings = []
    for s in paras:
        s = s.split(':')
        if len(s[0]):
            s[0] = '%s:' % s[0]
        strings.append('<strong>%s</strong> %s' % (s[0], s[1]))
    paras = ['<li>%s</li>' % p.strip() for p in strings]
    return '\n'.join(paras)


def paragraphs(value):
    paras = re.split(r'[\r\n]+', value)
    paras = ['<p>%s</p>' % p.strip() for p in paras]
    return '\n'.join(paras)



def parse_int(value):
    return int(value)


def plus(value, arg):
    return int(value) + int(arg)


register.filter('encode_parameters', encode_parameters)
register.filter('values', arrayValues)
register.filter('integer', parse_int)
register.filter('price', price_format)
register.filter('list', list)
register.filter('paragraphs', paragraphs)
register.filter('plus', plus)
register.filter('cut_values', cut_values)


