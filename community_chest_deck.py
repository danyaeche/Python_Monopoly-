import community_chest_card
import random


class community_chest_deck(object):
    def __init__(self):
        self.counter = 0
        contents = {
            1: community_chest_card(1,"Advance to Go (Collect $200)")
            2: community_chest_card(2,"Bank error in your favor—Collect $200")
            3: community_chest_card(3, "Doctor's fee—Pay $50")
            4: community_chest_card(4, "From sale of stock you get $50")
            5: community_chest_card(5, "Get Out of Jail Free")
            6: community_chest_card(6, "Go to Jail–Go directly to jail–Do not pass Go–Do not collect $200")
            7: community_chest_card(7, "Grand Opera Night—Collect $50 from every player for opening night seats")
            8: community_chest_card(8, "Holiday Fund matures—Receive $100")
            9: community_chest_card(9, "Income tax refund–Collect $20")
            10: community_chest_card(10, "It is your birthday—Collect $10")
            11: community_chest_card(11, "Life insurance matures–Collect $100")
            12: community_chest_card(12, "Pay hospital fees of $100")
            13: community_chest_card(13, "Pay school fees of $150")
            14: community_chest_card(14, "Receive $25 consultancy fee")
            15: community_chest_card(15, "You are assessed for street repairs–$40 per house–$115 per hotel")
            16: community_chest_card(16, "You have won second prize in a beauty contest–Collect $10")
            17 community_chest_card(17, "You inherit $100")


        def select_card(self):
            self.counter += 1
            if self.counter > 17:
                self.counter = 1
            vard = community_chest_deck(self.counter):
            return vard
        }

