import logging


def calc(x):
    try:
        result = x / 2
    except(TypeError, ValueError) as e:
        logging.error(f"Value invalid: {x}. Error: {str(e)}")
        return None
    else:
        logging.info(f"Calculation successful for value: {x}")
        return result



result = calc(3)
print(result)


result = calc("a")
print(result)