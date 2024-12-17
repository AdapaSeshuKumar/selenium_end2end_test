import logging
def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logging_info.log")

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    logger.debug("Debug is created")
    logger.info("Logger is created as info")
    logger.warning("seelkl warning!")
    logger.error("An error occured")
    logger.critical("Critical")