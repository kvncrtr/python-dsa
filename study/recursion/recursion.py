# # Infinite Loop
# def countdown(i):
#     print(i)
#     countdown(i - 1)

# countdown(20)

# # Break with a base case
# def countdown(i):
#     print(i)
#     if i <= 1:
#         return
#     else:
#         countdown(i - 1)

# countdown(20)

# # Call Stack Understanding
# def greeting(name):
#     print("Hello, " + name + "!")
#     greet2(name)
#     print("getting ready to say bye")
#     bye()

# def greet2(name):
#     print("how are you " + name + "?")

# def bye():
#     print("ok, bye!")

# greeting("maggie")

# # 3.1 Suppose I show you a call stack like this.
# '''
# What information can you give me, just based on this call stack?

# Answer: From this call stack, I can determine that the program is currently 
# executing the greet2 function, which was called by greeting. The 
# parameter name has the value "maggie" in both stack frames. Once greet2 
# finishes execution, control will return to greeting, which will then 
# continue executing the next line after the function call.
# '''

# # 3.1 Example call stack
# '''
# Top (currently executing)

# Stack Frame # 2 (eryuewiry4839)
# - function name: greet2
# - parameters: name
# - local variables: null
# - return address: fhuer438ry4729ur83029

# Stack Frame # 1 (fhuer438ry4729ur83029)
# - function name: greeting
# - parameters: name
# - local variables: null
# - return address: null

# Bottom
# '''

# # Factorial of a Number
# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)

# print(fact(5))