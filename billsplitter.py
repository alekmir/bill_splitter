from random import choice

guest_count = int(input('Enter the number of friends joining (including you):\n'))
guests = dict()
if guest_count > 0:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(guest_count):
        guests[input()] = None
    total_bill = int(input('\nEnter the total bill value:\n'))

    if input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n') == 'Yes':
        lucky = choice(list(guests))
        print(f'{lucky} is the lucky one!\n')
        partition = round(total_bill / (len(guests) - 1), 2)
        for guest in guests:
            if guest == lucky:
                guests[guest] = 0
            else:
                guests[guest] = partition
        print(guests)
    else:
        print("No one is going to be lucky")
        partition = round(total_bill / len(guests), 2)
        for guest in guests:
            guests[guest] = partition
        print(guests)
else:
    print("No one is joining for the party")
