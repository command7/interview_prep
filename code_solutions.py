import logging


def binary_search(nums, target, formatter):
    logger = setup_logger('binary_search',
                          'logs/binary_search.log',
                          formatter)
    total_numbers = len(nums)
    logger.info(f'Number of elements : {total_numbers}')
    logger.info(f'Value to be found : {target}')
    end_index = total_numbers - 1
    start_index = 0
    logger.info(f'Starting Index : {start_index}')
    logger.info(f'Ending Index : {end_index}\n')
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        logger.info(f'Middle index is {mid_index}')
        mid_value = nums[mid_index]
        logger.info(f'Middle index value : {mid_value}')
        if mid_value == target:
            logger.info(f'Element found in index {mid_index}')
            return mid_index
        elif mid_value < target:
            logger.info("Shifting search space to right")
            start_index = mid_index + 1
            logger.info(f'New starting index : {start_index}\n')
        else:
            logger.info("Shifting search space to left")
            end_index = mid_index - 1
            logger.info(f'New ending index : {end_index}\n')
    logger.info('Element not found')
    return -1


def mySqrt(x):
    return int(x ** (1/2))


def setup_logger(name, log_file, formatter, level=logging.INFO):
    handler = logging.FileHandler(log_file,
                                  mode='w')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    binary_search([1,2,3,4,5,5],
                  2,
                  formatter)
