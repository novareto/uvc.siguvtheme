# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('uvc.siguvtheme', 'static')

bootstrap_css = Resource(
    library, 'bootstrap.css',
    compiler="sass",
    source='siguvtheme.scss'
)

main_css = Resource(library, 'main.css', depends=[bootstrap_css, ])
main_js = Resource(library, 'main.js', depends=[jquery, ])
