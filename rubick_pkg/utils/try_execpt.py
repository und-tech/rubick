# -*- coding: utf-8 -*-
import traceback

from functools import wraps
from rubick_pkg.utils.logger import create


def handler(method):
    @wraps(method)
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            logger = create('try_except_handler')
            logger.error(e)
            if args[0].verbose:
                logger.error(traceback.format_exc())
    return method_wrapper
