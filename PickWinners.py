'''
Goal is to pick three winners for this months contest!
- Prize Choice ($50)
- Prize Choice ($50)
- Prize Choice ($50)
- Nitro 1 Month
- Nitro 1 Month
'''

import csv
import random
import time

def load_csv():
    filename = "HideUserData.csv"

    fields = []
    rows = []

    with open(filename, 'r', encoding="utf-8") as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        fields = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            rows.append((row[0], int(row[4])))

        return rows

def multiply_tickets(ticket_data):
    tickets = []
    for name, points in ticket_data:
        users_tickets = [name] * points
        tickets = tickets + users_tickets

    return tickets

def pick_winners(tickets):
    # Note first in list is top pize last is low prize
    winners = []
    random.shuffle(tickets)

    for ticket in tickets:
        if ticket not in winners:
            winners.append(ticket)
        if len(winners) >= 5:
            break

    return winners

contest_data = load_csv()
Final_list = multiply_tickets(contest_data)
win_win_chicken_dinner = pick_winners(Final_list)
for i, winner in enumerate(win_win_chicken_dinner):
    print(f"{i+1} - {winner}")
    #sleep for drama haha...
    time.sleep(5)