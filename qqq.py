from logging import *
# debug("this is debug")
# info("this is info")
basicConfig(filename='logfile.log', level=DEBUG, filemode='w', format='%(asctime)s -- %(message)s')
debug("this is debug in w mode")
info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")

