import logging


def get_all_loggers():
    return logging.Logger.manager.loggerDict.keys()


def get_all_base_loggers():
    return {x.split('.')[0] for x in get_all_loggers()}


def set_loglevel(debug=False):
    mylevel = logging.DEBUG if debug else logging.INFO
    logging.getLogger().setLevel(mylevel)

    liblevel = mylevel + 10
    for logger in get_all_base_loggers():
        logging.getLogger(logger).setLevel(liblevel)
