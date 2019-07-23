import inspect
import logging

def Customlogger(loglevel):
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(loglevel)
    filehandler = logging.FileHandler("{0}.log".format(loggername), mode='w')
    filehandler.setLevel(loglevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s :: %(message)s', datefmt=
                                  '%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger
