import logging


def get_logger(name):
  logger = logging.getLogger(name)
  if name.startswith('__'):
    name = "log"
  hdlr = logging.FileHandler('./{}.txt'.format(name))
  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  hdlr.setFormatter(formatter)
  logger.addHandler(hdlr)
  logger.setLevel(logging.INFO)
  return logger
