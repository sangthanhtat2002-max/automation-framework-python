import logging

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        handlers = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handlers.setFormatter(formatter)
        logger.addHandler(handlers)
        logger.setLevel(logging.INFO)

    return logger