import logging
import os


class AlienLogger(object):
    """
    A simple class to handle logging in the game
    """
    def __init__(self, name, level):
        self.level = level
        self.log_name = name

        self._log_path = None

    @property
    def log_path(self):
        """
        Set the log path creating the log dir if it does not exist
        :return: path to the log directory
        """
        if not self._log_path:
            log_dir = os.path.dirname(os.path.abspath(__file__))

            # Check if directory exists if not create it
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)

            self._log_path = log_dir
        return self._log_path

    def logger(self):
        """
        Set up the logging formatter and root logger
        :return: A logger configured with the correct handlers for the log level
        """
        log_name = '{path}/{file}.log'.format(path=self.log_path, file=self.log_name)

        # Delete the old log before creating the new one.
        if os.path.exists(log_name):
            os.remove(log_name)

        log_formatter = logging.Formatter("%(asctime)s [%(levelname)-7.7s] [%(module)s] %(message)s")
        root_logger = logging.getLogger()

        file_handler = logging.FileHandler(log_name)
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)

        root_logger.setLevel(self.level)

        return root_logger

# Initialize the logger
logger = AlienLogger('alien', level=logging.WARN).logger()
