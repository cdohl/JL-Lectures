# This is my very first module. Yes!

print('Module loaded. This is my very first module. Yes!')

def countup(val_max):
    print('Counting up!')

    if val_max > 100:
        print('Woah, I cannot count that much.')
        return
    else:
        for i in range(val_max):
            print('{}'.format(i))
