import sys

from logger import logging



def error_message_detail(error, error_detail:sys):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno
    
    error_message = "error details: script_name:[{0}]\n line_number:[{1}]\n message:[{2}]".format(file_name, line_number, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
    
    def __str__(self) -> str:
        return self.error_message


# Testing logging 
# if __name__ == "__main__":
#     try:
#         x=1/0
#     except Exception as exception:
#         logging.info("division by zero error")
#         raise CustomException(exception, sys)
    