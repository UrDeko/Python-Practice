import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("Training/log_file.txt")
file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.ERROR)

logger.addHandler(file_handler)

def logging_in_loop():
    current_logger = logging.getLogger(__name__)
    current_logger.setLevel(level=logging.DEBUG)
    current_formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

    increment = 0

    while increment < 4:
        for old_handler in current_logger.handlers:
            current_logger.removeHandler(old_handler)

        new_filename = "Training/log_file.txt"
        current_file_handler = logging.FileHandler(filename=new_filename, mode='a')
        current_file_handler.setFormatter(current_formatter)
        current_logger.addHandler(current_file_handler)

        current_logger.debug(increment)
        increment += 1
        
        time.sleep(3)

def to_dict(items):
    result = {}

    for item in items:
        try:
            result[item] += 1
        except KeyError:
            logger.exception("Adding new entry to the dictionary {}".format(result))
            result[item] = 1

    return result

if __name__ == "__main__":
    with open("Training/log_file.txt", "a") as file:
        file.write("\n" * 3)

    # logger.debug('Hello there')
    # words = ["banana", "strawberry", "cherry", "banana"]
    # logger.debug("Dictionary: {}".format(to_dict(words)))
    
    logging_in_loop()