# Funcion Basic
def changeme(list_val):
    list_val.append([1, 2, 3, 4])
    print("Nilai dalam fungsi: ", list_val)
    return


mylist = [10, 20, 30]
changeme(mylist)

print("Nilai luar fungsi: ", mylist)


def changeme():
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4];  # This would assign new reference in mylist
    print("Nilai di dalam fungsi: ", mylist)
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme()
print("Nilai di luar fungsi: ", mylist)


# Another Function
def printinfo(name, umur):
    print("Name: ", name)
    print("Age :", umur)
    return


printinfo("Rifqi", 25)


# Function with default arguments
def printinfo(name, umur=20):
    print("Name: ", name)
    print("Age :", umur)
    return


printinfo(name="Rifqi")


# Implementasi Variable Length *(star) parameter *var_args_tuple
def printinfo(arg1, *vartuple):
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo(10)
printinfo(10, 60, 79)

# Anonymous Functions - keyword: lambda
# Basic Syntax = lambda [arg1 [,arg2,.....argn]]:expression
jumlahkan = lambda arg1, arg2: arg1 + arg2;

print("Value of total : ", jumlahkan(10, 20))
print("Value of total : ", jumlahkan(20, 20))


# Return Value

def return_test(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


total = return_test(10, 20);
print("Outside the function : ", total)

# Scope
total = 0
def return_test(arg1, arg2):
    # global total  # change to global scope

    # Add both the parameters and return them."
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


return_test(10, 20);
print("Outside the function : ", total)