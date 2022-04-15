from graphics import*


def aug():
    user_in = input("Enter #(enter again to quit)")
    acc = 0
    count = 0
    while user_in != "":
        acc += float(user_in)
        count += 1
        user_in = input("Enter #(enter again to quit)")
    return acc/count


def get_num():
    nums = []
    user_input = input("ENter a number(enter again to quit)")
    while user_input != '':
        nums.append(eval(user_input))
        user_input = input("ENter a number(enter again to quit)")
    return nums


def mean(nums):
    return sum(nums)/len(nums)


def std_dev(nums, avg):
    acc = 0
    for num in nums:
        acc += (avg-num)**2
    return acc / (len(nums)-1)**0.5


def median(nums):
    nums.sort()
    middle_index = len(nums)//2
    if len(nums) % 2 == 0:
        middle_right = nums[middle_index]
        middle_left = nums[middle_index-1]
        return (middle_right+middle_left)/2
    else:
        return nums[middle_index]
# ---------------------------------------------------------------


def print_circles(circles):
    for circle in circles:
        print('({},{}) {}'.format(circle.getCenter().getX(), circle.getCenter().getY(), circle.getRadius(), end=''))


def x_sort(circle):
    return circle.getCenter().getX()


def y_sort(circle):
    return circle.getCenter().getY()


def radius_sort(circle):
    return circle.getRadius()


def main():
    # user_numbers = get_num()
    # avg = mean(user_numbers)
    # s = std_dev(user_numbers, avg)
    # middle = median(user_numbers)
    # print(user_numbers, avg, s, middle)

# ------------------------------------------------------
    #circle_data = [((12, 56), 45), ((213, 96), 85), ((112, 98), 95), ((432, 526), 5)]
    c1 = Circle(Point(12, 56), 45)
    c2 = Circle(Point(213, 96), 85)
    c3 = Circle(Point(112, 98), 95)
    c4 = Circle(Point(432, 526), 5)
    # circles = []
    # for data in circle_data:
    #     circles.append(Circle(Point(data[0], data[1]), data[2]))

    circles = [c1, c2, c3, c4]
    print_circles(circles)
    print()
    circles.sort(key=x_sort)
    print_circles(circles)
    print()
    circles.sort(key=y_sort)
    print_circles(circles)
    print()
    circles.sort(key=radius_sort)
    print_circles(circles)


main()

# if you're trying to add two list together don't just append [the list] because it will
# put it into a sub list, you acc to do acc = acc + [1,2,3]
# tuple - are lists that aren't mutiable (doesn't change)


def more_dict_example():
    families = {'jon': ['bob', 'ki', 'so'], 'angie': ['kat', 't', 'v']}
    # families['jon'] = ['bob', 'ki', 'so']
    # families['angie'] = ['kat', 't', 'v']
    for family in families:
        print(family, end='\n\t')
        for name in families[family]:
            print(name, end=' ')
        print()
