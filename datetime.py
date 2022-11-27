from time import localtime, strftime

now = 1407694710
my_tuple = localtime(now)
my_format = '%Y-%m-%d %H-%M-%S'
my_string = strftime(my_format, my_tuple) 

print(my_string)
