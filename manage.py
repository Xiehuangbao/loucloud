# -*- coding: utf-8 -*-

from flask_script import Manager
from loucloud import create_app

app = create_app()
manager = Manager(app)


@manager.command
def run():
    """run in local machine."""

    app.run()


if __name__ == '__main__':
    manager.run()
