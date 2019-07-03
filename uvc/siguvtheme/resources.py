# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.jquery import jquery
from js.fontawesome import fontawesome_js
from js.fontawesome import fontawesome_all_css

library = Library('uvc.siguvtheme', 'static')

bootstrap_css = Resource(
    library, 'bootstrap.css',
    compiler="sass",
    source='siguvtheme.scss'
)

bootstrap_js = Resource(
    library, 'bootstrap-4.3.1/dist/js/bootstrap.bundle.min.js', depends=[jquery, ] 
)

main_css = Resource(library, 'main.css', depends=[bootstrap_css, fontawesome_all_css ])
main_js = Resource(library, 'main.js', depends=[bootstrap_js, ])
