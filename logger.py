import logging

# name of logger
logger = logging.getLogger("TEST by me")

# set level of all logger , DEBUG=lowest=log all
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
# "-8" or "-18" = "-lenth" for free space , don't use for set space = lenth string
# can switch sequence
formatter = logging.Formatter('%(levelname)-8s - %(name)-18s - %(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an informational message ')
logger.warning('This is a warning message ')
logger.error('This is an error message')
logger.critical('This is a critical message ')


logger2 = logging.getLogger("TEST by me ABCD")


logger2.setLevel(logging.DEBUG)

handler2 = logging.StreamHandler()
formatter2 = logging.Formatter('%(levelname)-8s - %(name)-18s - %(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler2.setFormatter(formatter2)
logger2.addHandler(handler2)

# Example usage
logger2.debug('This is a debug message')
logger2.info('This is an informational message ')
logger2.warning('This is a warning message ')
logger2.error('This is an error message')
logger2.critical('This is a critical message ')


