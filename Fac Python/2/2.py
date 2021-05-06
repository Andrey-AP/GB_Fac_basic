my_list = input("Enter elements separated by space: ").split()
for i in range(1, len(my_list), 2):
    # if i < len(my_list)-1:
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(my_list)
