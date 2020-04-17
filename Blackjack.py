import random
import time


class Blackjack:

    deck = ["club1", "club2", "club3", "club4", "club5", "club6", "club7", "club8", "club9", "club10", "spade1", "spade2", "spade3", "spade4", "spade5", "spade6", "spade7", "spade8", "spade9", "spade10", "diamond1", "diamond2", "diamond3", "diamond4", "diamond5", "diamond6", "diamond7", "diamond8", "diamond9", "diamond10", "heart1", "heart2", "heart3", "heart4", "heart5", "heart6", "heart7", "heart8", "heart9", "heart10", "clubjack", "clubqueen", "clubking", "spadejack", "spadequeen", "spadeking", "diamondjack", "diamondqueen", "diamondking", "heartjack", "heartqueen", "heartking"]

    value = {"club1": 1, "club2": 2, "club3": 3, "club4": 4, "club5": 5, "club6": 6, "club7": 7, "club8": 8, "club9": 9,
             "club10": 10, "clubjack": 10, "clubqueen": 10, "clubking": 10, "spade1": 1, "spade2": 2, "spade3": 3,
             "spade4": 4, "spade5": 5, "spade6": 6, "spade7": 7, "spade8": 8, "spade9": 9, "spade10": 10,
             "spadejack": 10,
             "spadequeen": 10, "spadeking": 10, "diamond1": 1, "diamond2": 2, "diamond3": 3, "diamond4": 4,
             "diamond5": 5,
             "diamond6": 6, "diamond7": 7, "diamond8": 8, "diamond9": 9, "diamond10": 10, "diamondjack": 10,
             "diamondqueen": 10, "diamondking": 10, "heart1": 1, "heart2": 2, "heart3": 3, "heart4": 4, "heart5": 5,
             "heart6": 6, "heart7": 7, "heart8": 8, "heart9": 9, "heart10": 10, "heartjack": 10, "heartqueen": 10,
             "heartking": 10}

    def __init__(self, player_name, bank_balance, bet):
        self.player_name = player_name
        self.bank_balance = bank_balance
        self.bet = bet

        '''
        cards_drawn is the list of cards drawn till now.
        This is needed to ensure that the same card doesnt get drawn twice
        '''
        self.cards_drawn = []

        '''
        dealer_cards_drawn is the list of cards drawn by the dealer
        This is needed display dealer's card in the end
        '''
        self.dealer_cards_drawn = []

        '''
        player_cards_drawn is the list of cards drawn by the player
        This is needed display the player's card in the end
        '''
        self.player_cards_drawn = []




    def card_assignment(self):
        self.k = random.randint(0,51)
        return (Blackjack.deck[self.k])


    def take_card_initial(self):

        '''
        cp = card of player
        cd = card of dealer

        :return:
        '''
        self.cp_1 = self.card_assignment()
        self.cards_drawn.append(self.cp_1)

        self.player_cards_drawn.append(self.cp_1)

        self.cp_2 = self.card_assignment()

        while(self.cp_2 in self.cards_drawn):
            self.cp_2 = self.card_assignment()
        self.cards_drawn.append(self.cp_2)

        self.player_cards_drawn.append(self.cp_2)



        self.cd_1 = self.card_assignment()

        while(self.cd_1 in self.cards_drawn):
            self.cd_1 = self.card_assignment()
        self.cards_drawn.append(self.cd_1)


        self.cd_2 = self.card_assignment()

        while(self.cd_2 == self.cards_drawn):
            self.cd_2 = self.card_assignment()
        self.cards_drawn.append(self.cd_2)


        '''
        tp is total value of player's cards
        td is total value of dealer's cards
        '''

        self.tp = self.value[self.cp_1] + self.value[self.cp_2]
        self.td = self.value[self.cd_1] + self.value[self.cd_2]



    def draw_card_while_playing(self):


        self.cp = self.card_assignment()

        '''
        Below logic ensures that the same card is not drawn twice
        '''

        while(self.cp in self.cards_drawn):
            self.cp = self.card_assignment()

        self.cards_drawn.append(self.cp)
        self.player_cards_drawn.append(self.cp)


    def dealer_draw_card_while_playing(self):

        self.cd = self.card_assignment()

        '''
        Below logic ensures that the same card is not drawn twice
        '''

        while(self.cd in self.cards_drawn):
            self.cd = self.card_assignment()

        self.cards_drawn.append(self.cd)
        self.dealer_cards_drawn.append(self.cd)



    def dealer_plays_the_game(self):

        '''
        Players will keep drawing the card till his card value is greater than or equal to 25

        :return:
        '''

        '''
        update dealer_cards_drawn with initial two cards
        '''
        self.dealer_cards_drawn.append(self.cd_1)
        self.dealer_cards_drawn.append(self.cd_2)



        while(self.td < 25):
            print("\n Drawing another card")

            time.sleep(8)

            self.dealer_draw_card_while_playing()
            self.td = self.td + self.value[self.cd]


        print("\n Dealer has declared")
        time.sleep(8)




    def begin_the_game(self):

        '''
        assign the cards and print players all card and dealers first card
        :return:
        '''

        self.take_card_initial()

        print("{}'s initial cards are: {} and {}".format(self.player_name, self.cp_1, self.cp_2))
        print("\nDealers' one of the cards is: {}".format(self.cd_1))
        print("\nYour initial card value is: {}".format(self.tp))




        self.go = 1

        while(self.go):
            self.response = input("You want to HIT : Y/N ")
            if(self.response == "Y"):

                '''
                Draws another card and updates the player's total card value
                '''

                self.draw_card_while_playing()

                print("\nCard drawn is {}".format(self.cp))

                self.tp = self.tp + self.value[self.cp]

                print("\nYour total card value is: {}".format(self.tp))

                if(self.tp > 35):
                    print("\nBUST : Your total card value exceeded 35")
                    break


            else:
                self.go = 0

        print("\nYour declared card value: {}".format(self.tp))
        #print("\nList of all the cards drawn {}".format(self.cards_drawn))

        if(self.tp <= 35):
            print("\n ########   NOW IT'S DEALER'S TURN    ########")


            self.dealer_plays_the_game()

            print("\n #####  RESULT TIME   #####")
            time.sleep(4)

            if(self.tp > self.td):
                print("\n {}'s cards are {} ".format(self.player_name, self.player_cards_drawn))
                time.sleep(4)
                print("\n {}'s total card value is: {}".format(self.player_name, self.tp))
                print("\n Dealers cards are {} ".format(self.dealer_cards_drawn))
                time.sleep(4)
                print("\n Dealer's total card value is: {}".format(self.td))
                time.sleep(4)
                print("\n {} has won the game".format(self.player_name))
                print("\n Bet placed was {}".format(self.bet))

                self.bank_balance += self.bet
                time.sleep(4)

                print("\n Hence, {}'s bank balance now is: {}".format(self.player_name, self.bank_balance))

            elif(self.tp < self.td):
                print("\n {}'s cards are {} ".format(self.player_name, self.player_cards_drawn))
                time.sleep(4)
                print("\n {}'s total card value is: {}".format(self.player_name, self.tp))
                print("\n Dealers cards are {} ".format(self.dealer_cards_drawn))
                time.sleep(4)
                print("\n Dealer's total card value is: {}".format(self.td))
                time.sleep(4)
                print("\n Dealer has won the game")
                print("\n Bet placed was {}".format(self.bet))

                self.bank_balance -= self.bet
                time.sleep(4)

                print("\n Hence, {}'s bank balance now is: {}".format(self.player_name, self.bank_balance))

            else:
                print("\n {}'s cards are {} ".format(self.player_name, self.player_cards_drawn))
                time.sleep(4)
                print("\n {}'s total card value is: {}".format(self.player_name, self.tp))
                print("\n Dealers cards are {} ".format(self.dealer_cards_drawn))
                time.sleep(4)
                print("\n Dealer's total card value is: {}".format(self.td))
                time.sleep(4)
                print("\n Game has Tied")
                print("\n Hence, {}'s bank balance remains the same i.e. {}".format(self.player_name, self.bank_balance))






bj = Blackjack("Varun", 100, 100)
bj.begin_the_game()




