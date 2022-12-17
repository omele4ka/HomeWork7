import logger
import view
import model

def string_calculate():
    calc_str = view.input_str()
    result = model.calculate_str(calc_str)
    logger.str_logger(calc_str, result)
    view.print_result(result)

def start():
    string_calculate()

