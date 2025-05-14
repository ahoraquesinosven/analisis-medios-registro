#!/usr/bin/env python3
import locale
locale.setlocale(locale.LC_TIME, 'es_AR.utf8')

import datetime as dt
from jinja2 import Template
# cargar CSV > array de diccionario con el formato que corresponde Date, integer, etc
def load_cases():
    return [
        { "fecha": dt.datetime(2020,1,20) },
        { "fecha":dt.datetime(2020,3,28) }
    ]

# agarro cada diccionario > render de un template libreria python jinja2  > array de strings
template = Template('Hello {{ fecha.strftime("%d de %B de %Y") }}!')

def render_template(case):
    return template.render(case)

def render_obituaries(data):
    obituaries = map(render_template, data)

    return obituaries



# texto plano probar
#TODO

print(list(render_obituaries(load_cases())))
