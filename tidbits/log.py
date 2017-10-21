import logging


def get_all_loggers():
    return logging.Logger.manager.loggerDict.keys()


def get_all_base_loggers():
    return {x.split('.')[0] for x in get_all_loggers()}
