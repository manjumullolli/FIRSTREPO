# import logging
# logging.debug('the debug message is displaying')
# logging.info('the info message is displaying')
# logging.warning('the warning message is displaying')
# logging.error('the error message is displaying')
# logging.critical('the critical message is displaying')

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('The debug messaged is logged')

# import logging
# logging.basicConfig(filename='msg.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')

# import logging
# logging.basicConfig(filename='newfile.log', format='%(asctime)s %(message)s', filemode='w')
# #creating an object of the logging
# logger=logging.getLogger()
#
# logger.setLevel(logging.DEBUG)
#
# logger.debug("This is a harmless debug message")
# logger.info("This is just an information")
# logger.warning("It is a warning. Please make changes")
# logger.error("You are trying to divide by zero")
# logger.critical("Internet is down")

# import logging
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a warning message')


# import logging
# logging.basicConfig(format='%(asctime)s  -   %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

# import logging
# logging.basicConfig(format='%(asctime)s  - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')


# import logging
# name='Raju Roy'
# logging.error('%s raised an error', name)

# import logging
# name="Raju Roy"
# logging.error(f'{name} raised an error')

# import logging
# a=10
# b=0
#
# try:
#     c=a/b
# except Exception as e:
#     logging.error("Exception occured", exc_info=True)

#logging.erroe(exc_info=True)

# import logging
# a=10
# b=0
#
# try:
#     c=a/b
# except Exception as e:
#     logging.exception("Exception occured", exc_info=True)

#classes and Functions
#root will not see
# import logging
# logger=logging.getLogger('first_logger')
# logger.warning('This is a warning message')

#work with handlers
# import logging
# #create a custom logger_obj
# logger_obj=logging.getLogger(__name__)
# #create handlers
# w_handler=logging.StreamHandler()
# e_handler=logging.FileHandler('file.log')
# w_handler.setLevel(logging.WARNING)
# e_handler.setLevel(logging.ERROR)
#
# #create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(messaage)s')
# w_handler.setFormatter((c_format))
# e_handler.setFormatter(f_format)
#
# #add handlers to the logger_obj
# logger_obj.addHandler(w_handler)
# logger_obj.addHandler(e_handler)
#
# logger_obj.warning('This is a warning message')
# logger_obj.error('This is an error message')



# import logging
# logging.basicConfig(filename='myapp.log', level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s')
#
#
# def add_numbers(x, y):
#     logging.debug(f"Adding {x} and {y}")
#     result = x + y
#     logging.info(f"Result: {result}")
#     return result
# add_numbers(2, 3)




#
# import logging
# logging.basicConfig(filename='addition.log', level=logging.INFO,
#                     format='%(asctime)s:%(levelname)s:%(message)s')
# def add_numbers(num1, num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         result = num1 + num2
#         logging.info(f"Addition of {num1} and {num2} = {result}")
#         return result
#     else:
#         logging.warning("input valid integer only.")
#
# print(add_numbers(8, 3))
# print(add_numbers(2.5, "3"))



# Module1.py
# import logging
#
# logger = logging.getLogger('module1')
#
# def do_something():
#     logger.debug('Doing something')
#
# # Module2.py
# import logging
#
# logger = logging.getLogger('module2')
#
# def do_something_else():
#     logger.debug('Doing something else')
#
# # Main program
# import logging
# import Module1
# import Module2
#
# logging.basicConfig(level=logging.DEBUG, filename='example.log', filemode='w')
#
# Module1.do_something()
# Module2.do_something_else()

#custom loggers and handlers
import logging

#create a custom logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

#create a console handler and set its level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

#create a file handler and set its level
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.DEBUG)


#create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

#add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

#log some messages
logger.debug('this is a debug msg')
logger.info('this is an info msg')
logger.warning('this is a warning msg')
logger.error('this is an error msg')
logger.critical('this is a critical msg')