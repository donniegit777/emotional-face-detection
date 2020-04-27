import logging.handlers

from greengrass_common.local_cloudwatch_handler import LocalCloudwatchLogHandler

# https://docs.python.org/2/library/logging.html#logrecord-attributes
LOCAL_CLOUDWATCH_FORMAT = '[%(levelname)s]-%(filename)s:%(lineno)d,%(message)s'

local_cloudwatch_handler = LocalCloudwatchLogHandler('GreengrassSystem', 'python_runtime')
local_cloudwatch_handler.setFormatter(logging.Formatter(LOCAL_CLOUDWATCH_FORMAT))
