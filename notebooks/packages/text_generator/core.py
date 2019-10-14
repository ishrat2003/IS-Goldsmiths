import logging
import sys

class Core(object):

    def __init__(self, loggingLevel = None):
        self._reset()
        self.__setLogger(loggingLevel)
        return

    def _reset(self):
        pass
        return

    def __setLogger(self, loggingLevel):
        self.logger = logging.getLogger()
        self.logger.setLevel(loggingLevel if loggingLevel else logging.ERROR)
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        self.logger.handlers = [handler]
        return
	