# Game Setup
import Deck, Player

player_one = Player.Player("One")
player_two = Player.Player("Two")

new_deck = Deck.Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on = True

# while game_on
round_no = 0
while game_on:
    round_no += 1
    print(f'Round {round_no}')

    if len(player_one.all_cards) == 0:
        print("Player One. Out of cards! Player Two wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two. Out of cards! Player One wins!")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    # while at_war
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("Player One. Unable to declare WAR!")
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two. Unable to declare WAR!")
                print("Player One Wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())