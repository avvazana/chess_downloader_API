# main.py
import logging

def init_logger():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default_handler': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'standard',
                'filename': os.path.join('logs', 'application.log'),
                'encoding': 'utf8'
            },
            'default_stdout': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',  # Default is stderr
            },
        },
        'loggers': {
            '': {
                'handlers': ['default_handler', 'default_stdout'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }
    logging.config.dictConfig(logging_config)