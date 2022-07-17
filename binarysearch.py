my_list = [2,3,4,5,6,7,8,9,10,12,15,]
def binary_sort(n, my_list):
    left_pointer = 0
    right_pointer =len(my_list) - 1
    mid_point = (left_pointer + right_pointer) // 2
    while mid_point - n <= 0.01:
        if n == my_list[mid_point]:
            return mid_point
        elif n > my_list[mid_point]:
            left_pointer =  mid_point


f = binary_sort(12, my_list)       
print(f)


