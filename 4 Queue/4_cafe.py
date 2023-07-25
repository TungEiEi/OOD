class Queue:

    def __init__(self , list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def enQueue(self,item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

def cafe(line):
    command = Queue(line)
    barista1 = 0
    barista2 = 0
    customer_who_wasted_their_time_the_most = 0
    max_wait_time = 0
    finish_list = []
    while not command.isEmpty():
        in_time, coffee_time, customer_number = command.deQueue()
        if barista1 > barista2 and in_time < barista1:
            barista1, barista2 = barista2, barista1
        current_customer_wait_time = 0
        if in_time < barista1:
            current_customer_wait_time = barista1 - in_time
        else:
            barista1 = in_time

        # print(customer_number, current_customer_wait_time)
        if current_customer_wait_time > max_wait_time:
            max_wait_time = current_customer_wait_time
            customer_who_wasted_their_time_the_most = customer_number

        barista1 += coffee_time

        finish_list.append([barista1, customer_number])

    finish_list.sort()
    [print(f'Time {e[0]} customer {e[1]} get coffee') for e in finish_list]

    if max_wait_time == 0:
        print(f'No waiting')
    else:
        print(f'The customer who waited the longest is : {customer_who_wasted_their_time_the_most}')
        print(f'The customer waited for {max_wait_time} minutes')


print(" ***Cafe***")
inp = [[int(c) for c in e.split(',')] + [i + 1] for i, e in enumerate(input("Log : ").split('/'))]
# inp.sort(key=lambda x: x[0])
cafe(inp[:])