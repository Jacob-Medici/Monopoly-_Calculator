import random

spaces = {
    0 : {
        'name' : 'GO!',
        'rent_w_hotel' : 0,
        'times_landed_on' : 1,
        'chance_of_this_space' : 0
    },

    1 : {
        'name' : 'Mediterranean Avenue',
        'rent_w_hotel' : 250,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    2 : {
        'name' : 'Community Chest (1)',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    3 : {
        'name' : 'Baltic Avenue',
        'rent_w_hotel' : 450,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    4 : {
        'name' : 'Income Tax',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    5 : {
        'name' : 'Reading Railroad',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    6 : {
        'name' : 'Oriental Avenue',
        'rent_w_hotel' : 550,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    7 : {
        'name' : 'Chance (1)',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    8 : {
        'name' : 'Vermont Avenue',
        'rent_w_hotel' : 550,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    9 : {
        'name' : 'Connecticut Avenue',
        'rent_w_hotel' : 600,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    10 : {
        'name' : 'Visiting Jail',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    11 : {
        'name' : 'St. Charles Place',
        'rent_w_hotel' : 750,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    12 : {
        'name' : 'Electric Company',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    13 : {
        'name' : 'States Avenue',
        'rent_w_hotel' : 750,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    14 : {
        'name' : 'Virginia Avenue',
        'rent_w_hotel' : 900,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    15 : {
        'name' : 'Pennsylvania Railroad',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    16 : {
        'name' : 'St. James Place',
        'rent_w_hotel' : 950,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    17 : {
        'name' : 'Community Chest (2)',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    18 : {
        'name' : 'Tennessee Avenue',
        'rent_w_hotel' : 950,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    19 : {
        'name' : 'New York Avenue',
        'rent_w_hotel' : 1000,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    20 : {
        'name' : 'Free Parking',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    21 : {
        'name' : 'Kentucky Avenue',
        'rent_w_hotel' : 1050,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    22 : {
        'name' : 'Chance (2)',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    23 : {
        'name' : 'Indiana Avenue',
        'rent_w_hotel' : 1050,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    24 : {
        'name' : 'Illinois Avenue',
        'rent_w_hotel' : 1100,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    25 : {
        'name' : 'B & O Railroad',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    26 : {
        'name' : 'Atlantic Avenue',
        'rent_w_hotel' : 1150,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    27 : {
        'name' : 'Ventnor Avenue',
        'rent_w_hotel' : 1150,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    28 : {
        'name' : 'Water Works',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    29 : {
        'name' : 'Marvin Gardens',
        'rent_w_hotel' : 1200,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    30 : {
        'name' : 'Go To Jail',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    31 : {
        'name' : 'Pacific Avenue',
        'rent_w_hotel' : 1275,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    32 : {
        'name' : 'North Carolina Avenue',
        'rent_w_hotel' : 1275,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    33 : {
        'name' : 'Community Chest (3)',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    34 : {
        'name' : 'Pennsylvania Avenue',
        'rent_w_hotel' : 1400,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    35 : {
        'name' : 'Short Line Railroad',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    36 : {
        'name' : 'Chance (3)',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    37 : {
        'name' : 'Park Place',
        'rent_w_hotel' : 1500,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    38 : {
        'name' : 'Luxury Tax',
        'rent_w_hotel' : 0,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    },

    39 : {
        'name' : 'Boardwalk',
        'rent_w_hotel' : 2000,
        'times_landed_on' : 0,
        'chance_of_this_space' : 0
    }
}

chance = {
    1 : 'Advance to Boardwalk',
    2 : 'Advance to Go (Collect $200)',
    3 : 'Advance to Illinois Avenue. If you pass Go, collect $200',
    4 : 'Advance to St. Charles Place. If you pass Go, collect $200',
    5 : 'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled',
    6 : 'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled',
    7 : 'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.',
    8 : 'Bank pays you dividend of $50',
    9 : 'Get Out of Jail Free',
    10 : 'Go Back 3 Spaces',
    11 : 'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200',
    12 : 'Make general repairs on all your property. For each house pay $25. For each hotel pay $100',
    13 : 'Speeding fine $15',
    14 : 'Take a trip to Reading Railroad. If you pass Go, collect $200',
    15 : 'You have been elected Chairman of the Board. Pay each player $50',
    16 : 'Your building loan matures. Collect $150',
}

community_chest = {
    1 : 'Advance to Go (Collect $200)',
    2 : 'Bank error in your favor. Collect $200',
    3 : "Doctor's fee. Pay $50",
    4 : 'From sale of stock you get $50',
    5 : 'Get Out of Jail Free',
    6 : 'Go to Jail. Go directly to jail, do not pass Go, do not collect $200',
    7 : 'Holiday fund matures. Receive $100',
    8 : 'Income tax refund. Collect $20',
    9 : 'It is your birthday. Collect $10 from every player',
    10 : 'Life insurance matures. Collect $100',
    11 : 'Pay hospital fees of $100',
    12 : 'Pay school fees of $50',
    13 : 'Receive $25 consultancy fee',
    14 : 'You are assessed for street repair. $40 per house. $115 per hotel',
    15 : 'You have won second prize in a beauty contest. Collect $10',
    16 : 'You inherit $100',
}

# When the player lands on community chest or chance
def community_chest_chance():
    MIN_CHOICE = 1
    MAX_CHOICE = 16
    card = random.randint(MIN_CHOICE, MAX_CHOICE)
    return card

# Separate rolls for the player
def rolls():
    # Check if the random is causing problems. It is set to ignore
    MIN_ROLL = 1
    MAX_ROLL = 6
    roll1 = random.randint(MIN_ROLL, MAX_ROLL)
    roll2 = random.randint(MIN_ROLL, MAX_ROLL)
    return roll1, roll2
