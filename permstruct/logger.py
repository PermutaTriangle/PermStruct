import datetime
import sys

class StructLogger(object):
    INFO = 0
    WARNING = 1
    ERROR = 2

    def __init__(self, verbosity=WARNING):
        self.verbosity = verbosity
        self.output = sys.stderr
        self.output_format = '[%(date)s] %(message)s\n'

    def log(self, message, level=INFO):
        if level >= self.verbosity:
            self.output.write(self.output_format % { 'date': datetime.datetime.now(), 'message': message })

    def warn(self, message):
        self.log(message, level=StructLogger.WARNING)

    def error(self, message):
        self.log(message, level=StructLogger.ERROR)

