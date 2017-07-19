#!/usr/bin/env python
#coding=utf8
import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger = logging.getLogger()
logger.debug('This is a logging test')
