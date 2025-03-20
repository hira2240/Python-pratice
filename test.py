queue = []

def enqueue(): 
    a = str(input('\nAdd an element to do list: \n'))
    queue.append(a)
    print(queue)

def dequeue():
    for i, element in enumerate(queue, 0): 
        print(f"{i}. {element}")
    a = int(input('\nWhich element would you like to mark as completed?: \n'))
    if 0 <= a < len(queue): #this checks that the index a, is greater than or equal to zero and lesser than the length of the queue. the length of the queue which would be one more than the last valid index. 
        queue.pop(a)
        print('\nItem completed:', queue)
    else: 
        print('\nInvalid')

def run():
    b = input('\nWould you like to add or complete something from your to do list?: \n').lower()
    option = b[:3]

    options = {
        'add' : enqueue,
        'com' : dequeue
    }
    if option in options: 
        do = options[option]()
    else: 
        print('invalid option')
run()

done = False
while not done: 
    run()
    c = input('\nAre you done with adding or completing your to do list?: yes/no \n').lower()
    if c == 'yes': 
        done = True
    elif c == 'no': 
        done = False
    else: 
        print('Invalid')





