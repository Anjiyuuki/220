def linear_search(my_list, target):
    for i in range(len(my_list)):
        if target == my_list[i]:
            return i
    return -1





if __name__ == '__main__':
    my_list= [2,3,5,1,7,8,23,99]
    target = 6
    result = linear_search(my_list, target)

    if result >= 0:
        print('found target {}'.format(target))
    else:
        print('target: {} does not exist'.format(target))
