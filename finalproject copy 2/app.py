# python -m flask run

from flask import Flask, redirect, render_template, request
from helpers import community_chest_chance, rolls, spaces, chance, community_chest


app = Flask(__name__)

inputed_turns_taken_off_amount = 0
money_from_go = 0
taxes = 0
get_out_of_jail_free = 0
collected = 0
comm_chest_lands = 0
chance_lands = 0
paid_to_leave = 0
amount_in_jail = 0
rolled_doubles = 0


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        try:
            global inputed_turns_taken_off_amount
            inputed_turns_taken_off_amount = int(request.form.get("turns_taken_off_amount"))
        except:
            return redirect("/error")
        if not inputed_turns_taken_off_amount:
            return redirect("/error")
        if inputed_turns_taken_off_amount < 1:
            return redirect("/error")
        run_simulator(inputed_turns_taken_off_amount)
        return redirect("/after")

@app.route("/error", methods=["GET", "POST"])
def error():
    if request.method == "GET":
        return render_template("error.html")
    elif request.method == "POST":
        return redirect("/")

def run_simulator(inputed_turns_taken_off_amount):
    turns_taken_off_amount = inputed_turns_taken_off_amount
    # Get the dictonaries
    spaces_dict = spaces
    chance_dict = chance
    community_chest_dict = community_chest

    # Initalize running spaces
    running_spaces = 0
    current_space = 0
    in_jail = False
    global amount_in_jail
    amount_in_jail = 0
    global money_from_go
    money_from_go = 0
    global taxes
    taxes = 0
    global get_out_of_jail_free
    get_out_of_jail_free = 0
    global collected
    collected = 0
    global comm_chest_lands
    comm_chest_lands = 0
    global chance_lands
    chance_lands = 0
    global paid_to_leave
    paid_to_leave = 0
    global rolled_doubles
    rolled_doubles = 0
    double_in_a_row = 0

    # Clear the dictonary
    for space in range(len(spaces_dict)):
        spaces_dict[space]['times_landed_on'] = 0

    for turn in range(turns_taken_off_amount):
        # Get the roll
        if in_jail == False:
            roll1, roll2 = rolls()
            if (roll1 == roll2):
                rolled_doubles += 1
                double_in_a_row += 1
                if double_in_a_row == 3:
                    in_jail = True
            else:
                double_in_a_row = 0
            # Establish old space to compare
            old_space = running_spaces % 40
            running_spaces += (roll1 + roll2)
            current_space = running_spaces % 40
            if((old_space < 40) and current_space > 0 and current_space < 13 and old_space > 27):
                money_from_go += 200
            spaces_dict[current_space]['times_landed_on'] += 1

            # Make statements for every special Space
            # (Jail, Community Chest, Chance, Taxes (for stats), etc)
            if spaces_dict[current_space]['name'] == 'GO!':
                money_from_go += 200
            elif spaces_dict[current_space]['name'] == 'Community Chest (1)' or spaces_dict[current_space]['name'] == 'Community Chest (2)' or spaces_dict[current_space]['name'] == 'Community Chest (3)':
                comm_chest_lands += 1
                card_num = community_chest_chance()
                if community_chest[card_num] == 'Advance to Go (Collect $200)':
                    running_spaces += (40 - current_space)
                    money_from_go += 200
                    spaces_dict[running_spaces % 40]['times_landed_on'] += 1
                elif community_chest[card_num] == 'Bank error in your favor. Collect $200':
                    collected += 200
                elif community_chest[card_num] == "Doctor's fee. Pay $50":
                    taxes += 50
                elif community_chest[card_num] == 'From sale of stock you get $50':
                    collected += 50
                elif chance[card_num] == 'Get Out of Jail Free':
                    get_out_of_jail_free += 1
                elif chance[card_num] == 'Go to Jail. Go directly to jail, do not pass Go, do not collect $200':
                    in_jail = True
                elif community_chest[card_num] == 'Holiday fund matures. Receive $100':
                    collected += 100
                elif community_chest[card_num] == 'Income tax refund. Collect $20':
                    collected += 20
                elif community_chest[card_num] == 'It is your birthday. Collect $10 from every player':
                    pass
                elif community_chest[card_num] == 'Pay hospital fees of $100':
                    taxes += 100
                elif community_chest[card_num] == 'Pay school fees of $50':
                    taxes += 100
                elif community_chest[card_num] == 'Receive $25 consultancy fee':
                    collected += 25
                elif community_chest[card_num] == 'You are assessed for street repair. $40 per house. $115 per hotel':
                    pass
                elif community_chest[card_num] == 'You have won second prize in a beauty contest. Collect $10':
                    collected += 10
                elif community_chest[card_num] == 'You inherit $100':
                    collected += 100

            elif spaces_dict[current_space]['name'] == 'Chance (1)' or spaces_dict[current_space]['name'] == 'Chance (2)' or spaces_dict[current_space]['name'] == 'Chance (3)':
                chance_lands += 1
                card_num = community_chest_chance()
                if chance[card_num] == 'Advance to Boardwalk':
                    running_spaces += (39 - current_space)
                    spaces_dict[39]['times_landed_on'] += 1
                elif chance[card_num] == 'Advance to Go (Collect $200)':
                    running_spaces += (40 - current_space)
                    money_from_go += 200
                    spaces_dict[0]['times_landed_on'] += 1
                elif chance[card_num] == 'Advance to Illinois Avenue. If you pass Go, collect $200':
                    if (current_space > 24):
                        running_spaces += (40 - current_space) + 24
                        money_from_go += 200
                    else:
                        running_spaces += (24 - current_space)
                    spaces_dict[24]['times_landed_on'] += 1
                elif chance[card_num] == 'Advance to St. Charles Place. If you pass Go, collect $200':
                    if (current_space > 11):
                        running_spaces += (40 - current_space) + 11
                        money_from_go += 200
                    else:
                        running_spaces += (11 - current_space)
                    spaces_dict[running_spaces % 40]['times_landed_on'] += 1
                elif chance[card_num] == 'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled':
                    if (current_space < 5):
                        running_spaces += (5 - current_space)
                    elif (current_space < 15 and current_space > 5):
                        running_spaces += (15 - current_space)
                    elif (current_space < 25 and current_space > 15):
                        running_spaces += (25 - current_space)
                    elif (current_space < 35 and current_space > 25):
                        running_spaces += (35 - current_space)
                    elif (current_space > 35):
                        running_spaces += (40 - current_space) + 5
                        money_from_go += 200
                    spaces_dict[running_spaces % 40]['times_landed_on'] += 1
                elif chance[card_num] == 'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.':
                    if (current_space < 12):
                        running_spaces += (12 - current_space)
                    elif (current_space < 12 and current_space < 28):
                        running_spaces += (28 - current_space)
                    elif (current_space > 28):
                        running_spaces += (40 - current_space) + 12
                        money_from_go += 200
                    spaces_dict[running_spaces % 40]['times_landed_on'] += 1
                elif chance[card_num] == 'Bank pays you dividend of $50':
                    collected += 50
                elif chance[card_num] == 'Get Out of Jail Free':
                    get_out_of_jail_free += 1
                elif chance[card_num] == 'Go Back 3 Spaces':
                    running_spaces -= 3
                elif chance[card_num] == 'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200':
                    in_jail = True
                elif chance[card_num] == 'Make general repairs on all your property. For each house pay $25. For each hotel pay $100':
                    pass
                elif chance[card_num] == 'Speeding fine $15':
                    taxes += 15
                elif chance[card_num] == 'Take a trip to Reading Railroad. If you pass Go, collect $200':
                    if (current_space < 5):
                        running_spaces += (5 - current_space)
                    else:
                        running_spaces += (40 - current_space) + 5
                        money_from_go += 200
                    spaces_dict[5]['times_landed_on'] += 1
                elif chance[card_num] == 'You have been elected Chairman of the Board. Pay each player $50':
                    pass
                elif chance[card_num] == 'Your building loan matures. Collect $150':
                    collected += 150
            elif spaces_dict[current_space]['name'] == 'Income Tax':
                taxes += 200
            elif spaces_dict[current_space]['name'] == 'Luxury Tax':
                taxes += 100
            elif spaces_dict[current_space]['name'] == 'Go To Jail':
                in_jail = True

        while in_jail:
            rolls_tried = 0
            while rolls_tried < 3:
                roll1, roll2 = rolls()
                turns_taken_off_amount -= 1
                amount_in_jail += 1
                if roll1 == roll2:
                    in_jail = False
                    running_spaces += ((40 - current_space) + 10) + roll1 + roll2
                    break
                rolls_tried += 1
            if rolls_tried >= 3:
                in_jail = False
                paid_to_leave += 1
                turns_taken_off_amount -= 1
                running_spaces += ((40 - current_space) + 10) + roll1 + roll2


    for space in range(len(spaces_dict)):
        spaces_dict[space]['chance_of_this_space'] = spaces_dict[space]['times_landed_on'] / inputed_turns_taken_off_amount

# This functino is from Harvard's CS50x online course based off problem set nine (Finanace)
@app.template_filter()
def prac_num(value):
    #Format value as practical num.
    return f"{value:,.2f}"

# This functino is from Harvard's CS50x online course based off problem set nine (Finanace)
@app.template_filter()
def comma_num(value):
    #Format value as practical num.
    return f"{value:,.0f}"

@app.template_filter()
def percent_num(value):
    #Format value as practical num.
    return f"{value:,.6f}"

@app.route("/after", methods=["GET", "POST"])
def after():
    # Load the page
    if request.method == "GET":
        most_landed_1, most_landed_2, most_landed_3 = sort_landed_on()
        most_price_1, most_price_2, most_price_3, running_total_rent = sort_hotel()
        try:
            return render_template("after.html", spaces_dict=spaces, money_from_go=money_from_go, taxes=taxes, get_out_of_jail_free=get_out_of_jail_free, collected=collected, comm_chest_lands=comm_chest_lands, chance_lands=chance_lands, paid_to_leave=paid_to_leave, amount_in_jail=amount_in_jail, most_landed_1=most_landed_1, most_landed_2=most_landed_2, most_landed_3=most_landed_3, most_price_1=most_price_1, most_price_2=most_price_2, most_price_3=most_price_3, running_total_rent=running_total_rent, rolled_doubles=rolled_doubles, inputed_turns_taken_off_amount=inputed_turns_taken_off_amount)
        except:
            return redirect("/error")
    else:
        return redirect("/")

def sort_landed_on():
    current_top_1 = 0
    current_top_2 = 0
    current_top_3 = 0
    name_1 = ''
    name_2 = ''
    name_3 = ''
    space_1 = 0
    space_2 = 1
    space_3 = 2
    for space in range(len(spaces)):
        if spaces[space]['times_landed_on'] > current_top_1:
            current_top_1 = spaces[space]['times_landed_on']
            name_1 = spaces[space]['name']
            space_1 = space
    for space in range(len(spaces)):
        if spaces[space]['times_landed_on'] > current_top_2 and spaces[space]['name'] != name_1:
            current_top_2 = spaces[space]['times_landed_on']
            name_2 = spaces[space]['name']
            space_2 = space
    for space in range(len(spaces)):
        if spaces[space]['times_landed_on'] > current_top_3 and spaces[space]['name'] != name_1 and spaces[space]['name'] != name_2:
            current_top_3 = spaces[space]['times_landed_on']
            name_3 = spaces[space]['name']
            space_3 = space
    return space_1, space_2, space_3

def sort_hotel():
    current_top_1 = 0
    current_top_2 = 0
    current_top_3 = 0
    name_1 = ''
    name_2 = ''
    name_3 = ''
    space_1 = 0
    space_2 = 1
    space_3 = 2
    running_total_rent = 0
    for space in range(len(spaces)):
        if spaces[space]['rent_w_hotel'] != 0:
            running_total_rent += (spaces[space]['times_landed_on'] * spaces[space]['rent_w_hotel'])
        if (spaces[space]['times_landed_on'] * spaces[space]['rent_w_hotel']) > current_top_1 and spaces[space]['rent_w_hotel'] != 0:
            current_top_1 = (spaces[space]['times_landed_on'] * spaces[space]['rent_w_hotel'])
            name_1 = spaces[space]['name']
            space_1 = space
    for space in range(len(spaces)):
        if (spaces[space]['times_landed_on'] * spaces[space]['rent_w_hotel']) > current_top_2 and spaces[space]['name'] != name_1  and spaces[space]['rent_w_hotel'] != 0:
            current_top_2 = (spaces[space]['times_landed_on'] * spaces[space]['rent_w_hotel'])
            name_2 = spaces[space]['name']
            space_2 = space
    for space in range(len(spaces)):
        if (spaces[space]['times_landed_on'] * spaces[space]['rent_w_hotel']) > current_top_3 and spaces[space]['name'] != name_1 and spaces[space]['name'] != name_2  and spaces[space]['rent_w_hotel'] != 0:
            current_top_3 = (spaces[space]['times_landed_on'] * spaces[space]['rent_w_hotel'])
            name_3 = spaces[space]['name']
            space_3 = space
    return space_1, space_2, space_3, running_total_rent







"""
@app.route("/error", methods=["GET", "POST"])
def after():
    if request.method == "GET":
        return render_template("error.html")
"""

"""
elif request.method == "POST":
if not request.form.get("shares"):
    return render_template("missing_error.html")
return render_template("after.html")
"""
