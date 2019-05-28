import random

#Assignment 3, by Deniz Sevinc (8628899)
#HW3_game_8628899
# Read and understand the docstrings of all of the functions in detail.


def make_deck(num):   
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''
    strange_deck = []
    for i in range(num):
        hearts = 101 + i
        spades = 201 + i
        diamonds = 301 + i
        clubs = 401 + i
        strange_deck.append(hearts)
        strange_deck.append(spades)
        strange_deck.append(diamonds)
        strange_deck.append(clubs)
        hearts = 0 
        spades = 0
        diamonds = 0
        clubs = 0
    return strange_deck
    

def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    
    random.shuffle(deck)
    return(deck)


def deal_cards_start(deck):
    '''(list of int)-> list of int

     Returns a list representing the player's starting hand.
     It is  obtained by dealing the first 7 cards from the top of the deck.
     Precondition: len(dec)>=7
    '''
    card_count = 0
    starting_hand = []
    if len(deck) >= 7:
        while(len(starting_hand) != 7):
            draw = deck[len(deck) - (card_count + 1)]
            starting_hand.append(draw)
            deck.remove(draw)
            card_count += 1
    return starting_hand


def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If  the number  of cards in the deck is less than num then then all the remaining cards are from the deck.
    Precondition: 1<=num<=6l deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []        

    '''
    if len(deck) < num:
        deck.reverse()
        player = player + deck
    else:
        append_deck = deck[-num:]
        append_deck.reverse()
        player += append_deck    

    return player


def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    sort_SR = hand 
    sort_SR.sort() # sort by suit and then by rank

    sort_rank = sort_SR
    sorted_hearts = []
    sorted_spades = []
    sorted_diamonds = []
    sorted_clubs = []
    for i in range(len(sort_rank)):
        if (sort_rank[i]//100) == 1:
            sorted_hearts.append(sort_rank[i])
        elif (sort_rank[i] - 200) < 14 and (sort_rank[i] - 200) > 0:
            sorted_spades.append(sort_rank[i])
        elif (sort_rank[i] - 300) < 14 and (sort_rank[i] - 300) > 0:
            sorted_diamonds.append(sort_rank[i])
        elif (sort_rank[i]//400) == 1:
            sorted_clubs.append(sort_rank[i])
    sorted_hearts.sort()
    sorted_spades.sort()
    sorted_diamonds.sort()
    sorted_clubs.sort() 

    max_hearts = 0
    max_spades = 0
    max_diamonds = 0
    max_clubs = 0
    '''long_list = [sorted_hearts,sorted_spades,sorted_diamonds,sorted_clubs]
    max_ranked = max(long_list, key=len) # return longest '''
    if not sorted_hearts: #if list is empty
        pass
    else:
        max_hearts = max(sorted_hearts)
    if not sorted_spades:
        pass
    else:
        max_spades = max(sorted_spades)
    if not sorted_diamonds:
        pass
    else:
        max_diamonds = max(sorted_diamonds)
    if not sorted_clubs:
        pass
    else:
        max_clubs = max(sorted_clubs)
    max_list = [max_hearts,max_spades,max_diamonds,max_clubs]
  
    max_rank = [0,0,0,0]

    #print(max_list)
    for m in range(len(max_list)):  
        rank = max_list[m]
        for j in range(1,14):
            if (rank - 100 == j) or (rank - 200 == j) or  (rank - 300 == j) or (rank - 400 == j):
                max_rank[m] = j
    #print(max_rank)
    
    ranked_hand = []
    for r in range(max(max_rank)):
        for z in range(0, len(hand)):
            if ((hand[z])- (r+1)) % 100 == 0:
                ranked_hand.append(hand[z])

    #print("Here is your hand printed in two ways \n", sort_SR, '\n', sort_rank, '\n', sorted_hearts, '\n', sorted_spades, '\n', sorted_diamonds, '\n', sorted_clubs)
    
    #print(ranked_hand)
    #print("Here is your hand printed in two ways: \n")
    space_ctr = 0
    while(space_ctr < (len(sort_SR))):
        print(sort_SR[space_ctr], end = ' ')
        space_ctr +=1
    print('\n')
    space_ctr2 = 0
    while(space_ctr2 < (len(ranked_hand))):
        print(ranked_hand[space_ctr2], end = ' ')
        space_ctr2 +=1
    print('\n')

    return hand


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    pass
    num_valid = 0
    num_invalid = 0
    
    for i in range(len(cards)):
        if cards[i] in player:
            num_valid += 1
        else:
            false = i
            num_invalid +=1
            print(cards[false], " not in your hand. Invalid input")
    if num_invalid != 0:
        return False
    else:
        return True


def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot convert elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    
    cards_copy = cards
    cards_copy.sort()
    #print(cards_copy)
    rank_list = []
    num_eq = 0

    for i in range(len(cards_copy)):
        if(((cards_copy[i] - 100 )< 14) and ((cards_copy[i] - 100 ) > 0)):
            rank_list.append(cards_copy[i] - 100)
        elif(((cards_copy[i] - 200 )< 14) and ((cards_copy[i] - 200 ) > 0)):
            rank_list.append(cards_copy[i] - 200)
        elif(((cards_copy[i] - 300 ) < 14) and ((cards_copy[i] - 300 ) > 0)):
            rank_list.append(cards_copy[i] - 300)
        elif(((cards_copy[i] - 400 )< 14) and ((cards_copy[i] - 400 ) > 0)):
            rank_list.append(cards_copy[i] - 400)
    #print(rank_list)
    
    if len(cards) < 2:
        #print("Invalid input. Discardable set needs to have at least 2 cards.")
        return False
    else:
        return rank_list[1:] == rank_list[:-1]


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    cards_cpy = cards
    cards_cpy.sort()

    num_seq = 0
    #print(cards_cpy)
    if len(cards_cpy) < 3:
        #print("Invalid input. Discardable set needs to have at least 3 cards.")
        return False
    else:
        for i in range(0,(len(cards_cpy) - 1)):
            if(cards_cpy[i+1] - cards_cpy[i]) == 1:
                num_seq+=1
            else:
                #print("Invalid sequence. Cards are not of same suit.")
                return False
        if(num_seq == len(cards_cpy) - 1):
            return True


def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in the deck. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    card_in_deck = False
    while(card_in_deck == False):
        print("Discard any card of your choosing.")
        discard = int(input("Which card would you like to discard? "))
        if discard in player:
            card_in_deck = True
            player.remove(discard)
            #print("Here is your new hand printed in two ways: \n")
            #print_deck_twice(player)
        else:
            print("No such card in the deck. Try again.")


def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid meld: 11 is not equal to 12
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
    seq_or_kind = ''
    while(seq_or_kind != 'yes' or seq_or_kind != 'no'):
        seq_or_kind = input("Yes or no, do you  have a sequence of three or more cards of the same suit or two or more of a kind? ")
        if(seq_or_kind == 'yes'):
            card_selection = input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: ").strip().split()
            
            for s in range(len(card_selection)):
                card_selection[s] = int(card_selection[s])
            #print(len(card_selection))
            if is_valid(card_selection, player) == True:
                if((is_discardable_kind(card_selection) == True)):
                    #print("true")
                    for i in range(len(card_selection)):
                        player.remove(card_selection[i])
                    print("Here is your new hand printed in two ways: \n")
                    print_deck_twice(player)
                elif((is_discardable_seq(card_selection)==True)):
                    #print("true2")
                    for i in range(len(card_selection)):
                        player.remove(card_selection[i])
                    print("Here is your new hand printed in two ways: \n")
                    print_deck_twice(player)
                elif((is_discardable_kind(card_selection) == False) and (is_discardable_seq(card_selection) == False)):
                    cards_copy = card_selection
                    cards_copy.sort()
                    #print(cards_copy)
                    rank_list = []

                    for i in range(len(cards_copy)):
                        if(((cards_copy[i] - 100 )< 14) and ((cards_copy[i] - 100 ) > 0)):
                            rank_list.append(cards_copy[i] - 100)
                        elif(((cards_copy[i] - 200 )< 14) and ((cards_copy[i] - 200 ) > 0)):
                            rank_list.append(cards_copy[i] - 200)
                        elif(((cards_copy[i] - 300 ) < 14) and ((cards_copy[i] - 300 ) > 0)):
                            rank_list.append(cards_copy[i] - 300)
                        elif(((cards_copy[i] - 400 )< 14) and ((cards_copy[i] - 400 ) > 0)):
                            rank_list.append(cards_copy[i] - 400)
                    if len(rank_list) <3:
                        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
                    if (len(rank_list) > 1) and (rank_list[0] != rank_list[1]):
                        print("Invalid meld: ", rank_list[0], " not equal to ",rank_list[1])
                    seq_or_kind = ''
                else:
                    print("Invalid input.")
            
            else:
                seq_or_kind = ''
        
        elif(seq_or_kind == 'no'):
            break

def roll_dice():
    '''This function returns a random integer between 1 and 6, after rolling a standard six-sided die
    '''
    dice = random.randint(1,6)
    return dice

# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()
# YOUR CODE GOES HERE and in all of the above functions instead of keyword pass
round = 0
new_deck = []
if size_change == 'yes':
    rank = -1
    while(rank > 99 or rank <3):
        rank = int(input("Enter a number between 3 and 99, for the number of ranks: "))
        print("You are playing with a deck of ", rank*4, " cards")
        new_deck = shuffle_deck(make_deck(rank))
        
        hand = deal_cards_start(new_deck)
        
        print("Here is your starting hand printed in two ways: \n")
        print_deck_twice(hand)
    #print(new_deck)
else:
    new_deck = shuffle_deck(make_deck(13))
    #print(new_deck)
    hand = deal_cards_start(new_deck)
    print("Here is your starting hand printed in two ways: \n")
    print_deck_twice(hand)
    #del(new_deck[-7:])



while (len(hand) > 0):
    if len(new_deck)>0:
        print("\nPlease roll the dice.")
        dice = roll_dice()
        print("You rolled the dice and it shows: ", dice)
        if dice == 1:
            rolled_one_round(hand)
            print("Here is your new hand printed in two ways: \n" )
            print_deck_twice(hand)
            if len(hand) < 1:
                break
        
        elif dice != 1:
            print("Since you rolled ", dice, " the following: ", dice, " or ", len(new_deck), "\n(if the deck has less than ", dice, ", cards then ", len(new_deck), "cards will be added to your hand from the top of the deck.)\n")
            if dice < len(new_deck):
                deal_new_cards(new_deck, hand,dice)
                del(new_deck[-dice:])

                #print(new_deck)
                print("Here is your new hand printed in two ways: \n")
                print_deck_twice(hand)
                rolled_nonone_round(hand)
            else:
                for i in range(len(new_deck)):
                    hand.append(new_deck[i])
                new_deck = []
                print_deck_twice(hand)
                rolled_nonone_round(hand)
            #print(hand)
            print("Here is your new hand printed in two ways: \n")
            print_deck_twice(hand)

    else:
        print("The game is in empty deck phase.\nHere is your hand printed in two ways: \n" )
        print_deck_twice(hand)
        rolled_one_round(hand)
    round+=1
    print("Round ", round, " completed.")
    
print("Congratulations, you completed the game in ",round, " rounds.")

