import logging

#logging.basicConfig(filename="/Users/akulac/PycharmProjects/Selenium project/seleniumlogs/test.log",level=logging.DEBUG)

logging.basicConfig(filename=r"C:\Users\charanteja\PycharmProjects\Selenium_Full_Course\seleniumlogs\test.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%d/%m/%y %I:%m:%s %p",
                    level=logging.DEBUG)
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is Warning message")
logging.error("This is Error message")
logging.critical("This is Critical message")