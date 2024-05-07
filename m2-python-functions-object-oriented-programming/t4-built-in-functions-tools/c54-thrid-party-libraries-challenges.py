# Third Party Libraries Challenge

from dateutil import parser
log_line = 'INFO 2020-07-03T23:27:51 Shutdown complete.'

timestamp = parser.parse(log_line, fuzzy=True)
print(timestamp)
