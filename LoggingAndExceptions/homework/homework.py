import logging.handlers


class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:
    # add 2 class attributes - max_visitors (200) and min_visitors (10)
    max_visitors = 200
    min_visitors = 10

    def __init__(self, visitors_num):
        """
        if visitors num is bigger than max_visitors - raise TooManyVisitors error
        if visitors num is less than min_visitors - raise TooFewVisitors error
        """
        if visitors_num > self.max_visitors:
            raise TooManyVisitors
        elif visitors_num < self.min_visitors:
            raise TooFewVisitors


def make_concert(visitors_num):
    """
    create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
    in case if caught - log error to console and return False, in case of successful initialization - return True
    """
    try:
        Concert(visitors_num=visitors_num)
    except TooManyVisitors:
        log_message("Too many visitors to do concert", 20)
        return False
    except TooFewVisitors:
        log_message("Too few visitors to do concert", 30)
        return False
    else:
        return True


# create Logger object
# set level to debug
# add handler to write logs to file "test.log"

# create logger and set level to debug
my_logger = logging.getLogger("logger_for_homework")
my_logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
handler = logging.handlers.RotatingFileHandler("test.log", maxBytes=40, backupCount=1)
handler.setLevel(logging.DEBUG)

# create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d %b %y, %H:%M:%S')
# add formatter to handler
# handler.setFormatter(formatter)

# add handler to my_logger
my_logger.addHandler(handler)


def log_message(message, level):
    """
    this function should use the logger defined above and log messages.
    level is the numeric representation of log level the message should refer to.
    :param message:
    :param level:
    """
    if level == 10:
        return my_logger.debug(f"{message}")
    elif level == 20:
        return my_logger.info(f"{message}")
    elif level == 30:
        return my_logger.warning(f"{message}")
    elif level == 40:
        return my_logger.error(f"{message}")
    elif level == 50:
        return my_logger.critical(f"{message}")
