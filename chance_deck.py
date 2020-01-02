import chance_card
import random

class chance_deck(object):
    def __init__(self):
        contents = {
            1: chance_card(1, "Advance to Go (Collect $200)"),
            2: chance_card(2, "Advance to Illinois Ave—If you pass Go, collect $200"),
            3: chance_card(3, "Advance to St. Charles Place – If you pass Go, collect $200"),
            4: chance_card(4, "Advance token to nearest Utility. If unowned, you may buy it "
                              "from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown."),
            5: chance_card(5, "Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is"
                              " otherwise entitled. If Railroad is unowned, you may buy it from the Bank."),
            6: chance_card(6, "Bank pays you dividend of $50"),
            7: chance_card(7, "Get Out of Jail Free"),
            8: chance_card(8, "Go Back 3 Spaces"),
            9: chance_card(9, "Go to Jail–Go directly to Jail–Do not pass Go, do not collect $200"),
            10: chance_card(10, "Make general repairs on all your property–For each house pay $25–For each hotel $100"),
            11: chance_card(11, "Pay poor tax of $15")
            12: chance_card(12, "Take a trip to Reading Railroad–If you pass Go, collect $200"),
            13: chance_card(13, "Take a walk on the Boardwalk–Advance token to Boardwalk"),
            14: chance_card(14, "You have been elected Chairman of the Board–Pay each player $50"),
            15: chance_card(15, "Your building and loan matures—Collect $150"),
            16: chance_card(16, "You have won a crossword competition—Collect $100")
        }

    def select_card(self):
        if len(self.contents) == 0:
           self.reset_deck()
        val = random.randint(1, 16)
        if val in self.contents:
            card = self.contents[val]
            del[val]
            return card
        else:
            self.select_card()


    def reset_deck(self):
        self.contents = {
            1: chance_card(1, "Advance to Go (Collect $200)"),
            2: chance_card(2, "Advance to Illinois Ave—If you pass Go, collect $200"),
            3: chance_card(3, "Advance to St. Charles Place – If you pass Go, collect $200"),
            4: chance_card(4, "Advance token to nearest Utility. If unowned, you may buy it "
                              "from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown."),
            5: chance_card(5,
                           "Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is"
                           " otherwise entitled. If Railroad is unowned, you may buy it from the Bank."),
            6: chance_card(6, "Bank pays you dividend of $50"),
            7: chance_card(7, "Get Out of Jail Free"),
            8: chance_card(8, "Go Back 3 Spaces"),
            9: chance_card(9, "Go to Jail–Go directly to Jail–Do not pass Go, do not collect $200"),
            10: chance_card(10, "Make general repairs on all your property–For each house pay $25–For each hotel $100"),
            11: chance_card(11, "Pay poor tax of $15")
            12: chance_card(12, "Take a trip to Reading Railroad–If you pass Go, collect $200"),
            13: chance_card(13, "Take a walk on the Boardwalk–Advance token to Boardwalk"),
            14: chance_card(14, "You have been elected Chairman of the Board–Pay each player $50"),
            15: chance_card(15, "Your building and loan matures—Collect $150"),
            16: chance_card(16, "You have won a crossword competition—Collect $100")
        }

