my_list =[]
while True:
    number = input('Enter number: ')
    if number == 'done':
        print('done')
        break
    try:
        ray=int(number)
        my_list.append(ray)
    except:
        print('try again, this with a number')
maximum = max(my_list)
minimum = min(my_list)
print('min number: ', minimum ,'max number ', maximum)