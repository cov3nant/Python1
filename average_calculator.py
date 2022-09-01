all_inputs= []
while True:
    user_inputs=input('Please type in a number:  ')
    if user_inputs == 'done':
        break
    try:
        converted_inputs=int(user_inputs)
        all_inputs.append(converted_inputs)
    except:
        print('Invalid input')
total=sum(all_inputs)
average=total/(len(all_inputs))
print('Total: ', total,' | Number of Inputs: ', len(all_inputs), ' | Average: ', average)tus