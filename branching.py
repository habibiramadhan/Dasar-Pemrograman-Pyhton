
# var1 = 100
# if var1:
#     print("1 - Got a true expression value")
#     print(var1)
# var2 = 0
# if var2:
#     print("2 - Got a true expression value")
#     print(var2)


amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)

print("Net payable:", amount - discount)

# condition = True
# print(2 if condition else 1 / 0)
# # Output is 2
# print((1 / 0, 2)[condition])
# # Zero Division Error

output = None
pesan = output or "No Data Returned"
print(pesan)