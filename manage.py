#!/usr/bin/env python
import os
import re
import sys
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.wsgi import app
from app.extensions import db


migrate = Migrate(app, db)
manager = Manager(app=app, usage="Perform database operations")
session = db.session
manager.add_command('db', MigrateCommand)


@manager.command
def run_development_server():
    app.run(debug=True, port=int(os.getenv('PORT', 5000)), host='0.0.0.0')


@manager.command
def run_production_server():
    from gunicorn.app.wsgiapp import run

    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', 'gunicorn')
    sys.argv[1] = 'app.wsgi:app'

    os.environ['GUNICORN_CMD_ARGS'] = "--bind=0.0.0.0:{port} \
            --workers={num_workers} \
            --timeout={app_timeout} \
            --access-logfile=- \
            --error-logfile=- \
            --capture-output \
            --limit-request-line=0 \
            --preload".format(
        port=os.getenv('PORT', 5000),
        num_workers=os.getenv('NUM_WORKERS', 4),
        app_timeout=os.getenv('APP_TIMEOUT', 1200)
    )

    sys.exit(run())

# @manager.command
# def full_clean_db():
#     from app.models.Project import (
#         FigmaNode,
#         FigmaFile,
#         FigmaFileGroup,
#         MilkyUIProject,
#         MilkView,
#         MilkViewState,
#         MilkViewCandidate
#     )

#     session.query(FigmaNode).delete()
#     session.query(MilkViewCandidate).delete()
#     session.query(MilkView).delete()
#     session.query(MilkViewState).delete()
#     session.query(MilkyUIProject).delete()
#     session.query(FigmaFile).delete()
#     session.query(FigmaFileGroup).delete()
#     session.commit()


if __name__ == '__main__':
    manager.run()
