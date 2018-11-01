import logging


def get_all_loggers():
    return logging.Logger.manager.loggerDict.keys()


def get_all_base_loggers():
    return {x.split('.')[0] for x in get_all_loggers()}


def set_handler(handler, logger=None):
    logging.getLogger(logger).handlers = []
    logging.getLogger(logger).addHandler(handler)


def set_handler_globally(handler, logger=None, ignore=None):
    ignore = ignore or set()

    for liblogger in get_all_base_loggers():
        if liblogger not in ignore:
            set_handler(handler, logger=liblogger)

    if logger:
        # avoid log duplication
        logging.getLogger().handlers = []
    # this may or may not be set above based on import order, do it here to be
    # explicitly sure
    set_handler(handler, logger=logger)


def set_loglevel(logger=None, debug=False):
    mylevel = logging.DEBUG if debug else logging.INFO
    logging.getLogger(logger).setLevel(mylevel)

    liblevel = mylevel + 10
    for liblogger in get_all_base_loggers():
        if logger == liblogger:
            continue

        logging.getLogger(liblogger).setLevel(liblevel)
