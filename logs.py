#!/usr/bin/env python3

import logging
from logging import handlers

log = logging.Logger("Davi", logging.DEBUG)
#console_handler = logging.StreamHandler()
#console_handler.setLevel(logging.DEBUG)
file_handler = handlers.RotatingFileHandler(
    filename="logs.log", maxBytes=300, backupCount=10
)
log_formatter = logging.Formatter("%(asctime)s %(name)s: %(message)s")
# console_handler.setFormatter(log_formatter)
file_handler.setFormatter(log_formatter)
log.addHandler(file_handler)

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Operação inválida: %s" % str(e))
