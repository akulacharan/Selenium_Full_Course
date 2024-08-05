import logging

logging.basicConfig(filename=r"C:\Users\charanteja\PycharmProjects\Selenium_Full_Course\seleniumlogs\test2.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%d/%m/%y %I:%m:%s %p")

# In real-time projects we weill not use the logging module directlly, instead we create a logger object and we will use it.

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) #Both are same but if we want to change le level in project it is easy way

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is Warning message")
logger.error("This is Error message")
logger.critical("This is Critical message")