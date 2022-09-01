my_file=input('Enter file name: ')
the_caps=my_file
clerics=open(the_caps)
for line in clerics:
    print(line.upper())