import logging


def binary_search(nums, target, format):
    logger = setup_logger('binary_search',
                          'logs/binary_search.log',
                          format)
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


def factorial_iterative(n):
    result = 1
    if n in [0, 1, 2]:
        return n
    for num in range(n, 1, -1):
        result = result * num
    return result


def factorial_recursive(n):
    # base case
    if n <= 1:
        return n
    # return case
    return n * factorial_recursive(n-1)


def rotated_binary_search(nums, target, format):
    logger = setup_logger('rotated_binary_search',
                          'logs/rotated_binary_search',
                          format)

    # fixing rotated list
    offset = 0
    logger.info(f'Initial List : {nums}')
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            offset = i+1
            nums = nums[i+1:] + nums[:i+1]
            break
    logger.info(f'After sorting list : {nums}\n')

    start_index = 0
    logger.info(f'Starting Index : {start_index}')
    end_index = len(nums) - 1
    logger.info(f'Ending Index : {end_index}')
    mid_index = (start_index + end_index) // 2
    logger.info(f'Mid Index : {mid_index}\n')

    while start_index <= end_index:
        mid_value = nums[mid_index]
        logger.info(f'New middle value : {mid_value}')
        if mid_value > target:
            logger.info(f'{mid_value} > {target}')
            end_index = mid_index - 1
            logger.info(f'New ending index : {end_index}')
            mid_index = (start_index + end_index) // 2
            logger.info(f'New middle index : {mid_index}\n')
        elif mid_value < target:
            logger.info(f'{mid_value} < {target}')
            start_index = mid_index + 1
            logger.info(f'New starting index : {start_index}')
            mid_index = (start_index + end_index) // 2
            logger.info(f'New middle index : {mid_index}\n')
        else:
            element_index = (mid_index + offset) % len(nums)
            logger.info(f'Element is found in index {element_index}')
            return element_index
    logger.info('Element not found in list')
    return -1


def fibonacci_iterative(n):
    result_list = [0, 1 ,1]
    if n <= len(result_list) - 1:
        return result_list[n]
    else:
        first_num = result_list[1]
        second_num = result_list[2]
        for i in range(3, n+1):
            current_sum = first_num + second_num
            first_num = second_num
            second_num = current_sum
    return second_num


def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)



def setup_logger(name, log_file, format, level=logging.INFO):
    handler = logging.FileHandler(log_file,
                                  mode='w')
    handler.setFormatter(format)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    print(reverse_string('hello j'))
