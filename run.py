#!/usr/bin/env python

from werkzeug.serving import run_simple
from frontend import create_app

if __name__ == '__main__':
    app = create_app()
    run_simple(
        hostname=app.config['SERVER_HOSTNAME'],
        port=app.config['SERVER_PORT'],
        application=app,
        use_reloader=app.debug
    )
