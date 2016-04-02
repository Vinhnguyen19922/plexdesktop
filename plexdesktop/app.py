import os
import sys
import logging
import pickle
from logging.config import dictConfig
from PyQt5.QtWidgets import QApplication
from plexdesktop.settings import Settings
from plexdesktop.mainwindow import PlexApp
from plexdesktop.browser import Browser
import plexdevices


def run():
    # for cx_Freeze and requests ssl issues
    os.environ["REQUESTS_CA_BUNDLE"] = os.path.join(os.getcwd(), "resources", "cacert.pem")
    # mpv on ubuntu
    os.environ["LC_NUMERIC"] = "C"
    # Logging
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'f': {'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s'}
        },
        'handlers': {
            'h': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'plexdesktop.log',
                'formatter': 'f',
                'backupCount': 1,
                'level': logging.DEBUG
            }
        },
        'loggers': {
            'plexdesktop': {
                'handlers': ['h'],
                'level': logging.DEBUG
            },
            'plexdesktop.mpv': {
                'handlers': ['h'],
                'level': logging.INFO
            },
            'plexdevices.device': {
                'handlers': ['h'],
                'level': logging.DEBUG,
                'propagate': True
            },
            'plexdevices.session': {
                'handlers': ['h'],
                'level': logging.DEBUG,
                'propagate': True
            },
            'plexdevices.media': {
                'handlers': ['h'],
                'level': logging.DEBUG,
                'propagate': True
            },
        }
    }
    dictConfig(logging_config)
    logger = logging.getLogger('plexdesktop')
    logger.handlers[0].doRollover()
    logger.info("Application Started")
    app = QApplication(sys.argv)
    with open('resources/plexdesktop.qss', 'r') as stylesheet:
        app.setStyleSheet(stylesheet.read())
    settings = Settings()
    # form = PlexApp()
    # form.show()
    # try:
    #     session = pickle.loads(settings.value('session'))
    # except Exception as e:
    #     session = None
    # else:
    #     try:
    #         server = [x for x in session.servers
    #                   if x.client_identifier == settings.value('last_server')][0]
    #     except ValueError:
    #         server = None

    form = Browser()#session=session, server=server)
    form.show()
    sys.exit(app.exec_())
