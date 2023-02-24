import datetime

x = datetime.datetime.now()

print(x)

#string format

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%m_%d_%Y_%H_%M_%S_%f"))