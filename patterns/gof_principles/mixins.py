from patterns.gof_principles import Logger, SocketLogger
import socket
import sys


class FilteredLogger(Logger):
    pattern = ''

    def log(self, message):
        if self.pattern in message:
            super().log(message)


class FilteredSocketLogger(FilteredLogger, SocketLogger):
    pass


sock1, sock2 = socket.socketpair()
# The caller can just set “pattern” directly.
logger = FilteredSocketLogger(sock1)
logger.pattern = 'Error'


logger.log('Warning: not that important')
logger.log('Error: this is important')

print('The socket received: %r' % sock2.recv(512))


class FileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()


# Simplify the filter by making it a mixin.

class FilterMixin:
    pattern = ''

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# Multiple inheritance looks the same as above.


class FilteredLogger(FilterMixin, FileLogger):
    pass  # Again, the subclass needs no extra code.


logger = FilteredLogger(sys.stdout)
logger.pattern = 'Error'
logger.log('Warning: not that important')
logger.log('Error: this is important')
