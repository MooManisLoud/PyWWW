import datetime

log_file = open("", "a")

log_file.write(str(datetime.datetime.now()) + "\n")

log_file.write("PyWWW has seemed to have crashed or has been asked to close by another process\n")
log_file.write("\n")

log_file.close()