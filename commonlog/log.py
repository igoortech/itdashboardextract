import logging
import logging.config
import traceback
import os
from os import path
from logging import DEBUG, WARNING, ERROR, INFO


class Logger(object):
    """
    Logger mixin/base class adding verbose logging to subclasses.
    Subclasses get info(), debug(), warning() and error() methods which, alongside
    the information given, also show location of the message (file, line and
    function).
    By default, the logging mechanism will only show warning and error messages
    without any timestamping. A static method Logger.basicConfig() is provided
    for basic usage with all debugging turned on and showing debuglevel and
    timestamps. See the documentation of logging module for information how to
    customize debug levels, formatters and outputs.
    To activate the basic configuration:
    >>> Logger.basicConfig()
    Example mixin usage:
    >>> class MyClass(Logger):
    ...    def my_method(self):
    ...        self.debug('called')
    ...    def raises_exc(self):
    ...        try:
    ...            raise Exception("error message")
    ...        except:
    ...            self.error('got exception', exc_info=True)
    ...
    >>> x = MyClass()
    >>> x.my_method()
    >>> x.raises_exc()
    Module also provides a singleton "logger" instance of Logger class, which
    can be used when it's not feasible to use the mixin. The logger provides
    the same debug(), warning() and error() methods.
    Example singleton usage:
    >>> logger.debug('This is a debug message')
    """

    show_source_location = True
    stringConnection = {}
    excution_id =""
    # Formats the message as needed and calls the correct logging method
    # to actually handle it
    def _raw_log(self, logfn, message, exc_info):
        cname = ''
        loc = ''
        fn = ''
        tb = traceback.extract_stack()
        if len(tb) > 2:
            if self.show_source_location:
                loc = '(%s:%d):' % (os.path.basename(tb[-3][0]), tb[-3][1])
            fn = tb[-3][2]
            if fn != '<module>':
                if self.__class__.__name__ != Logger.__name__:
                    fn = self.__class__.__name__ + '.' + fn
                fn += '()'

        logfn(loc + cname + fn + ': ' + message, exc_info=exc_info)

    def info(self, message="", exc_info=False):
        """
        Log a info-level message. If exc_info is True, if an exception
        was caught, show the exception information (message and stack trace).
        """
        self._raw_log(logging.info, message, exc_info)

    def debug(self, message="", case_identifier="", task="", exc_info=False):
        """
        Log a debug-level message. If exc_info is True, if an exception
        was caught, show the exception information (message and stack trace).
        """
        self._raw_log(logging.debug, message, exc_info)

    def warning(self, message="", case_identifier="", task="", exc_info=False):
        """
        Log a warning-level message. If exc_info is True, if an exception
        was caught, show the exception information (message and stack trace).
        """
        self._raw_log(logging.warning, message, exc_info)

    def error(self, message="", case_identifier="", task="", error="", exc_info=False):
        """
        Log an error-level message. If exc_info is True, if an exception
        was caught, show the exception information (message and stack trace).
        """
        self._raw_log(logging.error, message, exc_info)

    @staticmethod
    def basicConfig(level=DEBUG):
        """
        Apply a basic logging configuration which outputs the log to the
        console (stderr). Optionally, the minimum log level can be set, one
        of DEBUG, WARNING, ERROR (or any of the levels from the logging
        module). If not set, DEBUG log level is used as minimum.
        """

    @staticmethod
    def fileConfig(log_file_path, project_name, defaults={'logfilename': 'app.log'}):
        Logger.project_name = project_name
        logging.config.fileConfig(log_file_path, defaults)
        print(Logger.excution_id)
logger = Logger()

if __name__ == '__main__':
    # Run the code from examples
    import doctest
    doctest.testmod()