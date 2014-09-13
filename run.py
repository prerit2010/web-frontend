#!/usr/bin/env python

from werkzeug.serving import run_simple
from frontend import create_app

# Note: This function will be removed during deployment.
def extra_files():
    """
    Watch files and reload the server when they change.
    """

    import os

    extra_dirs = [
        'frontend/static',
        'frontend/templates'
    ]

    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = os.path.join(dirname, filename)
                if os.path.isfile(filename):
                    extra_files.append(filename)

    return extra_files


if __name__ == '__main__':
    app = create_app()
    run_simple(
        hostname=app.config['SERVER_HOSTNAME'],
        port=app.config['SERVER_PORT'],
        application=app,
        use_reloader=app.debug,
        extra_files=extra_files()
    )
