import sys
import logging


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message


# This defines a new class called CustomException.
# It inherts from Python’s built-in Exception class, meaning:
class CustomException(Exception):
# This is the constructor method __init__. It runs when you create a new object of this class.
    def __init__(self,error_message,error_detail:sys):
#This line calls the parent class constructor (Exception.__init__) and passes it the error_message.
        super().__init__(error_message)
# It calls your helper function:
# And it stores that message in the object:
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

# __str__() tells Python to return the custom error message   
    def __str__(self):
        return self.error_message

