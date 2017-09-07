def odd_even():
    for i in range(1, 2001):
        if (i % 2 == 0):
            print 'Number is {}. This is an even number'.format(i)
        else:
            print 'Number is {}. This is an odd number'.format(i)

odd_even()



def multiply(a, val):
    arr = []
    for number in a:
        arr.append(number * val)
    print arr

multiply(a, 5)


def multiply1(nums, factor):
    for i, val in enumerate(nums):
        nums[i] *= factor
    return nums

print multiply1([1,2,3,4,5],5)


def layered_multiples(arr):
    new_array = []
    for number in arr:
        a = []
        for i in range(number):
            a.append(1)
        new_array.append(a)
    return new_array

layered_multiples(multiply1([2,3,5],3))


def layered_multiples(multiplied_list):
    new_list = []
    for num in multipled_list:
        new_list.append([1] * num)
    return new_list

print layered_multiples( multiply1 ( [2,4,6], 2))
