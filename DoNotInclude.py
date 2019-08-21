import math

print(math.pi)

text = "Enjoy the test"
result = text.strip().split()[0]

print(result)
try:
    x = int("zero")
    print(10 / x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")
a = open

# x = str(int('1.0'))
# x[-1] = '2'
# x = str(1.0)
# x[-1] = '2'
