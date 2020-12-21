import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def input_valid_answer(string_for_input, valid_answers):
        answer = (input(string_for_input)).lower()
        while True:
            if answer in valid_answers:
                return answer
            else:
                valid_answers_title = [answer.title() \
                                       for answer in valid_answers]
                answer = (input("Please enter a valid answer. The valid answers are {}".format(", ".join(valid_answers_title)))).lower()



class Window(Tk):		
    def __init__(self):
        super(Window, self).__init__()
        self.title("Euchre")
        self.geometry("1500x770+0-30")
        
        self.enter_name = ttk.LabelFrame(self)  
        self.enter_name.place(relx = .39, rely = .39)
    
        
    def titleframe_encase(self):
        labelFont = ("arial", 20, "bold")
        greeting_pt1 = ttk.Label(self.enter_name, text = "Hello, and Welcome to Euchre!\n")
        greeting_pt1.configure(font = labelFont)
        greeting_pt1.grid(column = 0, row = 0, sticky = N)
        greeting_pt2 = ttk.Label(self.enter_name, text = "Please enter your name").grid(column = 0, row = 1, sticky = N)
        self.player_name = StringVar()
        self.name_entry1 = Entry(self, width = 20, textvariable = self.player_name)
        self.name_entry1.grid(in_ = self.enter_name, column =0, row = 3, sticky = N)
        done_enter_names_button = ttk.Button(self.enter_name, text = "Done Entering Name", command = self.done_entering_names_command).grid(column = 0, row = 4, sticky = N)
    
    def delete_window_widgets(self):
            list = self.grid_slaves()
            for l in list:
                l.destroy()
            list2 = self.place_slaves()
            if list2:
                for l in list2:
                    l.destroy()
            print("deleting window widgets")
    
    def empty_column_label(self, column = 0, row = 0, num_column_spaces = 1):
        num_column_labels_list = list(range(num_column_spaces))
        for i in num_column_labels_list:
            column_label = Label(window, text = "                    ").grid(column = column + i, row = row)
          
    def done_entering_names_command(self):
        self.player_name = self.player_name.get()
        self.delete_window_widgets()   
        self.tell_teams = ttk.LabelFrame(self)  
        self.tell_teams.place(relx = .36, rely = .30)
        labelFont = ("arial", 17, "bold")
        entered_teams_label = ttk.Label(self.tell_teams, text = "The teams are:\n\nTeam 1 = {} and AI 3\nTeam 2 = AI 2 and AI 4\n".format(self.player_name))
        entered_teams_label.configure(font = labelFont)
        entered_teams_label.grid(column = 0, row = 0, sticky = W)
        self.now_beginning_label = ttk.Label(self.tell_teams, text = "Your Euchre game is about to begin")
        self.now_beginning_label.configure(font = labelFont)
        self.now_beginning_label.grid(column = 0, row = 1)
        self.after(2000, lambda:[self.delete_window_widgets(), game_1.euchre_greeting_2()])
    
        


window = Window()
	
 
class Card():
    nine_of_hearts_pic = ImageTk.PhotoImage(Image.open("9_of_hearts.png"))
    nine_of_diamonds_pic = ImageTk.PhotoImage(Image.open("9_of_diamonds.png"))
    nine_of_clubs_pic = ImageTk.PhotoImage(Image.open("9_of_clubs.png"))
    nine_of_spades_pic = ImageTk.PhotoImage(Image.open("9_of_spades.png"))
    ten_of_hearts_pic = ImageTk.PhotoImage(Image.open("10_of_hearts.png"))
    ten_of_diamonds_pic = ImageTk.PhotoImage(Image.open("10_of_diamonds.png"))
    ten_of_clubs_pic = ImageTk.PhotoImage(Image.open("10_of_clubs.png"))
    ten_of_spades_pic = ImageTk.PhotoImage(Image.open("10_of_spades.png"))
    jack_of_hearts_pic = ImageTk.PhotoImage(Image.open("jack_of_hearts.png"))
    jack_of_diamonds_pic = ImageTk.PhotoImage(Image.open("jack_of_diamonds.png"))
    jack_of_clubs_pic = ImageTk.PhotoImage(Image.open("jack_of_clubs.png"))
    jack_of_spades_pic = ImageTk.PhotoImage(Image.open("jack_of_spades.png"))
    queen_of_hearts_pic = ImageTk.PhotoImage(Image.open("queen_of_hearts.png"))
    queen_of_diamonds_pic = ImageTk.PhotoImage(Image.open("queen_of_diamonds.png"))
    queen_of_clubs_pic = ImageTk.PhotoImage(Image.open("queen_of_clubs.png"))
    queen_of_spades_pic = ImageTk.PhotoImage(Image.open("queen_of_spades.png"))
    king_of_hearts_pic = ImageTk.PhotoImage(Image.open("king_of_hearts.png"))
    king_of_diamonds_pic = ImageTk.PhotoImage(Image.open("king_of_diamonds.png"))
    king_of_clubs_pic = ImageTk.PhotoImage(Image.open("king_of_clubs.png"))
    king_of_spades_pic = ImageTk.PhotoImage(Image.open("king_of_spades.png"))
    ace_of_hearts_pic = ImageTk.PhotoImage(Image.open("ace_of_hearts.png"))
    ace_of_diamonds_pic = ImageTk.PhotoImage(Image.open("ace_of_diamonds.png"))
    ace_of_clubs_pic = ImageTk.PhotoImage(Image.open("ace_of_clubs.png"))
    ace_of_spades_pic = ImageTk.PhotoImage(Image.open("ace_of_spades.png"))
    
    nine_of_hearts_pic_small = (Image.open("9_of_hearts.png")).resize((110, 160))
    nine_of_hearts_pic_small = ImageTk.PhotoImage(nine_of_hearts_pic_small)
    nine_of_diamonds_pic_small = (Image.open("9_of_diamonds.png")).resize((110, 160))
    nine_of_diamonds_pic_small = ImageTk.PhotoImage(nine_of_diamonds_pic_small)
    nine_of_clubs_pic_small = (Image.open("9_of_clubs.png")).resize((110, 160))
    nine_of_clubs_pic_small = ImageTk.PhotoImage(nine_of_clubs_pic_small)
    nine_of_spades_pic_small = (Image.open("9_of_spades.png")).resize((110, 160))
    nine_of_spades_pic_small = ImageTk.PhotoImage(nine_of_spades_pic_small)
    
    
    ten_of_hearts_pic_small = (Image.open("10_of_hearts.png")).resize((110, 160))
    ten_of_hearts_pic_small = ImageTk.PhotoImage(ten_of_hearts_pic_small)
    ten_of_diamonds_pic_small = (Image.open("10_of_diamonds.png")).resize((110, 160))
    ten_of_diamonds_pic_small = ImageTk.PhotoImage(ten_of_diamonds_pic_small)
    ten_of_spades_pic_small = (Image.open("10_of_spades.png")).resize((110, 160))
    ten_of_spades_pic_small = ImageTk.PhotoImage(ten_of_spades_pic_small)
    ten_of_clubs_pic_small = (Image.open("10_of_clubs.png")).resize((110, 160))
    ten_of_clubs_pic_small = ImageTk.PhotoImage(ten_of_clubs_pic_small)
    
    jack_of_hearts_pic_small = (Image.open("jack_of_hearts.png")).resize((110, 160))
    jack_of_hearts_pic_small = ImageTk.PhotoImage(jack_of_hearts_pic_small)
    jack_of_diamonds_pic_small = (Image.open("jack_of_diamonds.png")).resize((110, 160))
    jack_of_diamonds_pic_small = ImageTk.PhotoImage(jack_of_diamonds_pic_small)
    jack_of_spades_pic_small = (Image.open("jack_of_spades.png")).resize((110, 160))
    jack_of_spades_pic_small = ImageTk.PhotoImage(jack_of_spades_pic_small)
    jack_of_clubs_pic_small = (Image.open("jack_of_clubs.png")).resize((110, 160))
    jack_of_clubs_pic_small = ImageTk.PhotoImage(jack_of_clubs_pic_small)
    
    queen_of_hearts_pic_small = (Image.open("queen_of_hearts.png")).resize((110, 160))
    queen_of_hearts_pic_small = ImageTk.PhotoImage(queen_of_hearts_pic_small)
    queen_of_diamonds_pic_small = (Image.open("queen_of_diamonds.png")).resize((110, 160))
    queen_of_diamonds_pic_small = ImageTk.PhotoImage(queen_of_diamonds_pic_small)
    queen_of_spades_pic_small = (Image.open("queen_of_spades.png")).resize((110, 160))
    queen_of_spades_pic_small = ImageTk.PhotoImage(queen_of_spades_pic_small)
    queen_of_clubs_pic_small = (Image.open("queen_of_clubs.png")).resize((110, 160))
    queen_of_clubs_pic_small = ImageTk.PhotoImage(queen_of_clubs_pic_small)
    
    king_of_hearts_pic_small = (Image.open("king_of_hearts.png")).resize((110, 160))
    king_of_hearts_pic_small = ImageTk.PhotoImage(king_of_hearts_pic_small)
    king_of_diamonds_pic_small = (Image.open("king_of_diamonds.png")).resize((110, 160))
    king_of_diamonds_pic_small = ImageTk.PhotoImage(king_of_diamonds_pic_small)
    king_of_spades_pic_small = (Image.open("king_of_spades.png")).resize((110, 160))
    king_of_spades_pic_small = ImageTk.PhotoImage(king_of_spades_pic_small)
    king_of_clubs_pic_small = (Image.open("king_of_clubs.png")).resize((110, 160))
    king_of_clubs_pic_small = ImageTk.PhotoImage(king_of_clubs_pic_small)
    
    ace_of_hearts_pic_small = (Image.open("ace_of_hearts.png")).resize((110, 160))
    ace_of_hearts_pic_small = ImageTk.PhotoImage(ace_of_hearts_pic_small)
    ace_of_diamonds_pic_small = (Image.open("ace_of_diamonds.png")).resize((110, 160))
    ace_of_diamonds_pic_small = ImageTk.PhotoImage(ace_of_diamonds_pic_small)
    ace_of_spades_pic_small = (Image.open("ace_of_spades.png")).resize((110, 160))
    ace_of_spades_pic_small = ImageTk.PhotoImage(ace_of_spades_pic_small)
    ace_of_clubs_pic_small = (Image.open("ace_of_clubs.png")).resize((110, 160))
    ace_of_clubs_pic_small = ImageTk.PhotoImage(ace_of_clubs_pic_small)
    
    
    
    def __init__(self, pic_large, pic_small, value, suit, card_name):
        self.pic = pic_large
        self.pic_small = pic_small
        self.value = value
        self.suit = suit
        self.card_name = card_name
    
    def __repr__(self):
        card_info = "{0} of {1}".format(self.card_name, self.suit)
        return card_info
        
    def get_pic(self):
        return self.pic
    
    def get_small_pic(self):
        return self.pic_small
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def get_card_name(self):
        return self.card_name

class Card_deck():

    Ace_of_hearts = Card(Card.ace_of_hearts_pic, Card.ace_of_hearts_pic_small, 14, "hearts", "ace")
    Ace_of_diamonds = Card(Card.ace_of_diamonds_pic, Card.ace_of_diamonds_pic_small, 14, "diamonds", "ace")
    Ace_of_clubs = Card(Card.ace_of_clubs_pic, Card.ace_of_clubs_pic_small, 14, "clubs", "ace")
    Ace_of_spades = Card(Card.ace_of_spades_pic, Card.ace_of_spades_pic_small, 14, "spades", "ace")
    Nine_of_hearts = Card(Card.nine_of_hearts_pic, Card.nine_of_hearts_pic_small, 9, "hearts", "9")
    Nine_of_diamonds = Card(Card.nine_of_diamonds_pic, Card.nine_of_diamonds_pic_small, 9, "diamonds", "9")
    Nine_of_clubs = Card(Card.nine_of_clubs_pic, Card.nine_of_clubs_pic_small, 9, "clubs", "9")
    Nine_of_spades =  Card(Card.nine_of_spades_pic, Card.nine_of_spades_pic_small, 9, "spades", "9")
    Ten_of_hearts = Card(Card.ten_of_hearts_pic, Card.ten_of_hearts_pic_small, 10, "hearts", "10")
    Ten_of_diamonds = Card(Card.ten_of_diamonds_pic, Card.ten_of_diamonds_pic_small, 10, "diamonds", "10")
    Ten_of_clubs = Card(Card.ten_of_clubs_pic, Card.ten_of_clubs_pic_small, 10, "clubs", "10")
    Ten_of_spades = Card(Card.ten_of_spades_pic, Card.ten_of_spades_pic_small, 10, "spades", "10")
    Jack_of_hearts = Card(Card.jack_of_hearts_pic, Card.jack_of_hearts_pic_small, 11, "hearts", "jack")
    Jack_of_diamonds = Card(Card.jack_of_diamonds_pic, Card.jack_of_diamonds_pic_small, 11, "diamonds", "jack")
    Jack_of_clubs = Card(Card.jack_of_clubs_pic, Card.jack_of_clubs_pic_small, 11, "clubs", "jack")
    Jack_of_spades = Card(Card.jack_of_spades_pic, Card.jack_of_spades_pic_small, 11, "spades", "jack")
    Queen_of_hearts = Card(Card.queen_of_hearts_pic, Card.queen_of_hearts_pic_small, 12, "hearts", "queen")
    Queen_of_diamonds = Card(Card.queen_of_diamonds_pic, Card.queen_of_diamonds_pic_small, 12, "diamonds", "queen")
    Queen_of_clubs = Card(Card.queen_of_clubs_pic, Card.queen_of_clubs_pic_small, 12, "clubs", "queen")
    Queen_of_spades = Card(Card.queen_of_spades_pic, Card.queen_of_spades_pic_small, 12, "spades", "queen")
    King_of_hearts = Card(Card.king_of_hearts_pic, Card.king_of_hearts_pic_small, 13, "hearts", "king")
    King_of_diamonds = Card(Card.king_of_diamonds_pic, Card.king_of_diamonds_pic_small, 13, "diamonds", "king")
    King_of_clubs = Card(Card.king_of_clubs_pic, Card.king_of_clubs_pic_small, 13, "clubs", "king")
    King_of_spades = Card(Card.king_of_spades_pic, Card.king_of_spades_pic_small, 13, "spades", "king") 
    
    
    def __init__(self):
        pass
    
    def build(self):
        deck = [Card_deck.Nine_of_hearts, Card_deck.Ten_of_hearts, Card_deck.Jack_of_hearts, Card_deck.Queen_of_hearts, Card_deck.King_of_hearts, Card_deck.Ace_of_hearts, \
        Card_deck.Nine_of_diamonds, Card_deck.Ten_of_diamonds, Card_deck.Jack_of_diamonds, Card_deck.Queen_of_diamonds, Card_deck.King_of_diamonds, Card_deck.Ace_of_diamonds, \
        Card_deck.Nine_of_clubs, Card_deck.Ten_of_clubs, Card_deck.Jack_of_clubs, Card_deck.Queen_of_clubs, Card_deck.King_of_clubs, Card_deck.Ace_of_clubs, \
        Card_deck.Nine_of_spades, Card_deck.Ten_of_spades, Card_deck.Jack_of_spades, Card_deck.Queen_of_spades, Card_deck.King_of_spades, Card_deck.Ace_of_spades]
        
        return deck
    
    

class Card_game:

    def __init__(self):
        self.Deck = Card_deck()
        self.Built_deck = self.Deck.build()
    
    def set_aces_low(self):
        self.Built_deck = Card_deck.build()
    
    def sort_deck(self, unwanted_cards, unwanted_suits = None):
        for card in self.Built_deck:
            if card.get_card_name() in unwanted_cards: 
                self.Built_deck.remove(card)
            elif unwanted_suits and card.get_suit() in unwanted_suits:
                self.Built_deck.remove(card)
        
    def deal_deck(self, num_players, leftover, discard):
        dealing_deck = self.Built_deck.copy()
        player_1_deck, player_2_deck, player_3_deck, player_4_deck, player_5_deck, player_6_deck, player_7_deck, \
        player_8_deck, player_9_deck, player_10_deck = [], [], [], [], [], [], [], [], [], []
        potential_decks = [player_1_deck, player_2_deck, player_3_deck, player_4_deck, player_5_deck, player_6_deck, \
                           player_7_deck, player_8_deck, player_9_deck, player_10_deck]
        true_decks = potential_decks[:(num_players)]
        leftover_deck = []
        num_to_deal = len(dealing_deck) - discard
        cards_per_player = (num_to_deal - leftover)//num_players
        remainder = (num_to_deal - leftover)%num_players
        for i in range(num_to_deal):
            ran_card = random.choice(dealing_deck)
            dealing_deck.remove(ran_card)
            for num in list(range(1, (num_players+1))):
                if i < cards_per_player*num and i >= cards_per_player*(num-1):
                    deck_to_add = true_decks[num-1]
                    deck_to_add.append(ran_card)
            if i >= (num_players*cards_per_player) <= (num_to_deal - remainder):
                leftover_deck.append(ran_card)
        return true_decks, leftover_deck
            
    def tell_hand(self, deck, player = None, column = 0, row = 2):
        counter = 1
        if player != None:
            tell_hand_label = Label(text = "The cards in your hand are: \n").grid(column = column, row = row)
        cl1, cl2, cl3, cl4, cl5 = Label(window), Label(window), Label(window), Label(window), Label(window)
        self.card_labels_list = [cl1, cl2, cl3, cl4, cl5]
        for item in deck:
            n = deck.index(item)
            card_picture = item.get_pic()
            self.card_labels_list[n].configure(image = card_picture)
            self.card_labels_list[n].grid(column = counter, row = 4)
            counter += 1
            
class Euchre(Card_game):
    
    trump_suit_pairs = {"spades": "clubs", "clubs": "spades", "diamonds":"hearts", "hearts": "diamonds"}
    left_bowers = {"spades": Card_deck.Jack_of_clubs, "clubs": Card_deck.Jack_of_spades, "hearts": Card_deck.Jack_of_diamonds, "diamonds": Card_deck.Jack_of_hearts}
    player_opposites = None    
    card_values_trump = {"9":9, "10":10, "queen":11, "king":12, "ace":13, "jack_lft":14, "jack":15}
    card_values_nontrump = {"9":9, "10":10, "jack":11, "queen":12, "king":13, "ace":14}
    players = None
    team_1 = None
    team_2 = None
    Player_1, Player_2, Player_3, Player_4 = None, None, None, None
    trump_suit_card = None
    true_decks, leftover_deck = None, None
    deck_order_standard = None
    player_1_deck, player_2_deck, player_3_deck, player_4_deck = None, None, None, None
    empty_potential_trump = ImageTk.PhotoImage(Image.open("empty_potential_trump.png"))
    
    def __init__(self):
        Card_game.__init__(self)
        self.euchre_sorted_deck = self.sort_deck(["2", "3", "4", "5", "6", "7", "8"])
        self.team_1_score = 0
        self.team_2_sore = 0
        self.dealer = None
        self.dealer_index = None
        self.counter = 0
        self.player_order = []
        self.deck_order = []
        self.trump_suit = None
        self.trump_card = None
        self.trump_info_list = []
        self.human_player = None


    def euchre_greeting_2(self):
        Euchre.Player_1 = Player(window.player_name, Player.player_1_icon)
        Euchre.Player_2 = AI("AI 2", AI.player_2_icon)
        Euchre.Player_3 = AI("AI 3", AI.player_3_icon)
        Euchre.Player_4 = AI("AI 4", AI.player_4_icon)
        
        Euchre.players = [Euchre.Player_1, Euchre.Player_2, Euchre.Player_3, Euchre.Player_4]
        Euchre.team_1 = [Euchre.Player_1, Euchre.Player_3]
        Euchre.team_2 = [Euchre.Player_2, Euchre.Player_4]
        Euchre.player_opposites = {Euchre.Player_1:Euchre.Player_3, Euchre.Player_3:Euchre.Player_1, \
                                  Euchre.Player_2:Euchre.Player_4, Euchre.Player_4:Euchre.Player_2}
        
        game_1.human_player = Euchre.Player_1
        
        for player in Euchre.players:
            if type(player) == Player:
                game_1.human_player = player
                
        self.euchre_shuffle()

    def set_trump(self, deck):
        Euchre.trump_suit_card = deck[random.randint(0, 3)]
        return Euchre.trump_suit_card
    
    def euchre_player_order(self, starting_player):
        sp_index = Euchre.players.index(starting_player)
        player_order = Euchre.players[sp_index:]
        player_order.extend(Euchre.players[:sp_index])
        deck_order = Euchre.deck_order_standard[sp_index:]
        deck_order.extend(Euchre.deck_order_standard[:sp_index])
        
        return player_order, deck_order

    def determine_highest(self, cards_played_in_order):
        #testprint
        print("cards_played_in_order = " + str(cards_played_in_order))
        suit_led = (cards_played_in_order[0]).get_suit()
        on_trump_card_values = {"9":9, "10":10, "queen":11, "king":12, "ace": 13, "jack_lft": 14, "jack": 15}
        led_card_values = {"9":9, "10":10, "jack":11, "queen":12, "king":13, "ace":14}

        card_suits = []
        card_names = []
        for card in cards_played_in_order:
            if card.get_card_name() == "jack" and card.get_suit() == Euchre.trump_suit_pairs[self.trump_suit]:
                #testprint
                print("left bower found in determine_highest")
                card_suits.append(self.trump_suit)
                card_names.append("jack_lft")
            else:
                card_suits.append(card.get_suit())
                card_names.append(card.get_card_name())

        trump_suit_indices = [[i, card_names[i]] for i,x in enumerate(card_suits) if x == self.trump_suit]
        led_card_indices = [[i, card_names[i]] for i,x in enumerate(card_suits) if x == suit_led]
        max_value = 0
        max_index = None
        if trump_suit_indices:
            for card in trump_suit_indices:
                card_index, card_name = card[0], card[1]
                card_value = on_trump_card_values[card_name]
                if card_value > max_value:
                    max_value = card_value
                    max_index = card_index
        else:
            for card in led_card_indices:
                card_index, card_name = card[0], card[1]
                card_value = led_card_values[card_name]
                if card_value > max_value:
                    max_value = card_value
                    max_index = card_index
        #max_card = card_names[max_index]
        #max_suit = card_suits[max_index]
        #if max_card == "jack_lft":
        #    max_card = "jack"
        #    max_suit = Euchre.trump_suit_pairs[trump_suit]

        return max_index
        #max_card, max_suit
    
    def show_trump(self):
        print("in show trump")
        print(self.trump_info_list[2])
        window.delete_window_widgets()
        
        spades_icon = ImageTk.PhotoImage(Image.open("spades_pic.jpg"))
        clubs_icon = ImageTk.PhotoImage(Image.open("clubs_image.png"))
        diamonds_icon = ImageTk.PhotoImage(Image.open("diamonds_image.png"))
        hearts_icon = ImageTk.PhotoImage(Image.open("hearts_image.png"))
        
        central_labelframe = LabelFrame(window)
        central_labelframe.place(relx = .36, rely = .30)
        labelFont = ("arial", 17, "bold")
        trump_is_label = ttk.Label(central_labelframe, text = "Trump is:\n")
        trump_is_label.configure(font = labelFont)
        trump_is_label.grid(column = 0, row = 0, sticky = W)
        
        trump_pic = None
        if self.trump_info_list[2] == "spades":
            print("in spades")
            trump_pic = spades_icon
        elif self.trump_info_list[2] == "clubs":
            print("in clubs")
            trump_pic = clubs_icon
        elif self.trump_info_list[2] == "diamonds":
            print("in diamonds")
            trump_pic = diamonds_icon
        else:
            print("in hearts")
            trump_pic = hearts_icon
        
        print("self.trump_info_list[2] second time = " + str(self.trump_info_list[2]))
        self.trump_suit_pic = Label(central_labelframe, image = trump_pic)
        self.trump_suit_pic.image = trump_pic
        self.trump_suit_pic.grid(column = 0, row = 1)
        
        
        picked_up_or_called = None
        player_called = self.trump_info_list[1]
        picked_up_or_called = "Called for pickup" if self.trump_info_list[0] == "yes" else "Called by"
        
        self.now_beginning_label = ttk.Label(central_labelframe, text = "\n{0} by {1}".format(picked_up_or_called, player_called.name))
        self.now_beginning_label.configure(font = labelFont)
        self.now_beginning_label.grid(column = 0, row = 2)
        
        if self.trump_info_list[3] != "no":
            loner_label = ttk.Label(central_labelframe, text = "\n{} has decided to go alone".format(self.trump_info_list[3].name))
            loner_label.configure(font = labelFont)
            loner_label.grid(column = 0, row = 3)
        
        
        
        window.after(2000, lambda: self.euchre_round_set_scene())
      
    def euchre_round_set_scene(self):
        spades_icon_small = ImageTk.PhotoImage(Image.open("spades_pic_small.jpg"))
        clubs_icon_small = ImageTk.PhotoImage(Image.open("clubs_image_small.png"))
        diamonds_icon_small = ImageTk.PhotoImage(Image.open("diamonds_image_small.png"))
        hearts_icon_small = ImageTk.PhotoImage(Image.open("hearts_image_small.jpg"))
        trump_image_dict = {"spades": spades_icon_small, "clubs": clubs_icon_small, "diamonds": diamonds_icon_small, "hearts": hearts_icon_small}
    
        print("in euchre round")
        window.delete_window_widgets()

        self.dealer_pickup_yn, self.player_picked_up, self.trump_suit, self.loner_player = self.trump_info_list[0], self.trump_info_list[1], \
        self.trump_info_list[2], self.trump_info_list[3]
        self.team_picked_up = self.team_1 if self.player_picked_up in self.team_1 else self.team_2
        self.team_1_hands_won, self.team_2_hands_won = 0, 0
        self.total_hands = (self.team_1_hands_won + self.team_2_hands_won)
        self.winning_player = "" 
        
        self.human_player_index = self.player_order.index(self.human_player)
        self.empty_label = Label(window, text = "      \n\n\n\n")
        self.empty_label.grid(column =0, row = 0)
        
        cards_played_label = Label(window, text = "Cards played:\n")
        labelFont = ("arial", 14, "bold")
        cards_played_label.configure(font = labelFont)
        cards_played_label.place(relx = .4, rely = .05)
        
        #pbw_1, pbw_2, pbw_3, pbw_4 = Label(window), Label(window), Label(window), Label(window)
        #played_by_who_label_list = [pbw_1, pbw_2, pbw_3, pbw_4]
        
        empty_row_for_pbw = Label(window, text = "               ")
        empty_row_for_pbw.grid(column = 0, row = 1)
        AI_1_labelframe = LabelFrame(window, text = "AI 1")
        AI_1_labelframe.grid(column =0, row = 2)
        AI_1_icon = ttk.Label(AI_1_labelframe, image = Euchre.players[1].get_pic())
        AI_1_icon.grid(column = 0, row = 0)
        
        empty_label_2 = Label(window, text = "     ")
        empty_label_2.grid(column = 0 ,row = 3)
        
        AI_2_labelframe = LabelFrame(window, text = "AI 2")
        AI_2_labelframe.grid(column = 0, row = 4)
        AI_2_icon = Label(AI_2_labelframe, image = Euchre.players[2].get_pic())
        AI_2_icon.grid(column = 0, row = 0)
        
        AI_3_labelframe = LabelFrame(window, text = "AI 3")
        AI_3_labelframe.grid(column = 0, row = 5)
        AI_3_icon = Label(AI_3_labelframe, image = Euchre.players[3].get_pic())
        AI_3_icon.grid(column = 0, row = 0)
        
        self.round_info_labelframe = LabelFrame(window)
        self.round_info_labelframe.place(relx = .9, rely = .15)
        team_1_label = Label(self.round_info_labelframe, text = "Team 1", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_1_label.grid(column =0, row = 0, sticky = E+W)
        t1_players_label = Label(self.round_info_labelframe, text = "{0} & {1}".format(Euchre.team_1[0].name, Euchre.team_1[1].name))
        t1_players_label.grid(column =0, row = 1, sticky = W)
        team_2_label = Label(self.round_info_labelframe, text = "Team 2", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_2_label.grid(column =0, row = 2, sticky = E+W)
        t2_players_label = Label(self.round_info_labelframe, text = "{0} & {1}".format(Euchre.team_2[0].name, Euchre.team_2[1].name))
        t2_players_label.grid(column =0, row = 3, sticky = W)
        current_trump_header= Label(self.round_info_labelframe, text = "Trump Suit", borderwidth=2, relief="groove", fg = "white", bg = "black")
        current_trump_header.grid(column =0, row = 4, sticky = E+W)
        current_trump_label = Label(self.round_info_labelframe, image = trump_image_dict[self.trump_suit])
        current_trump_label.image = trump_image_dict[self.trump_suit]
        current_trump_label.grid(column =0, row = 5, sticky = W)
        if self.loner_player != "no":
            team_1_label = Label(self.round_info_labelframe, text = "Loner Player", borderwidth=2, relief="groove", fg = "white", bg = "black")
            team_1_label.grid(column =0, row = 6, sticky = E+W)
            t1_players_label = Label(self.round_info_labelframe, text = self.loner_player.name)
            t1_players_label.grid(column =0, row = 7, sticky = W)
            
        
        window.empty_column_label(column = 1, num_column_spaces = 3)
        
        counter = 5
        self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5 = Button(window), Button(window), Button(window), Button(window), Button(window)
        self.buttons_list = [self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5]
        self.tell_hand_label = Label(text = "The cards in your hand are: \n")
        self.tell_hand_label.place(relx = .4, rely = .55)
        for item in Euchre.deck_order_standard[0]:
            n = Euchre.deck_order_standard[0].index(item)
            card_picture = item.get_pic()
            print("self.buttons_list[n] = " + str(self.buttons_list[n]))
            self.buttons_list[n].configure(image = card_picture, state = "disabled", command = lambda n = n: Euchre.players[0].human_card_choice_check(n))
            self.buttons_list[n].grid(column = counter, row = 5)
            counter += 1
        self.team_tricks_won_label = Label(window, text = "\nTeam 1 tricks won: {0}                      Team 2 tricks won: {1}".format(self.team_1_hands_won, self.team_2_hands_won))
        self.team_tricks_won_label.place(relx = .35, rely = .9)
        
        self.euchre_full_hand()
    
    def euchre_trick(self, i = 0):

        if i > len(self.player_order)-1:
            print("reached i > 3 in euchre_trick")
            self.show_highest()
        else:
            player = self.player_order[i]
            player_deck = self.deck_order[i]
            player.card_choice_question(i, player_deck)
        
    
    def show_highest(self):
        print("in show highest")
        max_index = self.determine_highest(self.laid_down)
        max_card = self.laid_down[max_index]
        self.winning_player = self.player_order[max_index]
        
        window.update()
        window.after(1000)
        self.tell_hand_label.place_forget()
        for b in self.buttons_list:
            b.grid_forget()
        
        self.sfb_1, self.sfb_2, self.sfb_3, self.sfb_4, self.sfb_5 = Label(window, image = Euchre.empty_potential_trump), Label(window, image = Euchre.empty_potential_trump), Label(window, image = Euchre.empty_potential_trump), \
        Label(window, image = Euchre.empty_potential_trump), Label(window, image = Euchre.empty_potential_trump)
        self.space_filler_labels = [self.sfb_1, self.sfb_2, self.sfb_3, self.sfb_4, self.sfb_5]
        counter = 5
        for sf in self.space_filler_labels:
            sf.grid(column = counter + self.space_filler_labels.index(sf), row = 5)
            counter += 1

        self.winner_label = Label(window, text = "{} won the trick with the: ".format(self.winning_player.name))
        labelFont = ("arial", 14, "bold")
        self.winner_label.configure(font = labelFont)
        self.winner_label.place(relx = .38, rely = .55)
        self.winning_card_label = Label(window, image = max_card.get_pic())
        self.winning_card_label.grid(column = 7, row = 5)
        window.update()
        if self.winning_player in self.team_1:
            self.team_1_hands_won += 1
        else:
            self.team_2_hands_won += 1
        self.total_hands = self.team_1_hands_won + self.team_2_hands_won
        self.team_tricks_won_label.configure(text = "\nTeam 1 tricks won: {0}                      Team 2 tricks won: {1}".format(self.team_1_hands_won, self.team_2_hands_won))
        window.update()
        
        print("reached current end of show highest")
        return
        
        
        #have to set the winner as winning_player or whatever for set starting player
        

    def euchre_full_hand(self, i = 0):
        self.player_order, self.deck_order = None, None
        if self.total_hands > 5:
            return
        else:
            self.set_starting_player()
            self.laid_down = []
            self.round_players = []
            #sets self.player_order and self.deck_order
            self.euchre_trick()
        
            
        # else:
            # self.laid_down = []
            # self.round_players = []
            # self.card_choice_number, self.card_choice = 0, []
            
            
            ###
            #testprint
            # print("self.player_order, deck_order_c")
            # print(self.player_order)
            # print(deck_order_c)
            
            # for i in range(len(deck_order_c)):
                # player = self.player_order[i]
                # player_deck = deck_order_c[i]
                # card_choice = []
                # card_choice_number = 0
                # player.card_choice_questions(i)
                # if type(player) == Player:
                
                    # card_choice_number, card_choice = Player.card_choice_question(self, i, player, player_deck, self.player_order, deck_order_c, player_picked_up, \
                         # dealer_pickup_yn, self.dealer, trump_suit, trump_suit_card, laid_down, Euchre.players, winning_player, \
                         # team_picked_up, last_hand_winning_card, team_1_hands_won, team_2_hands_won, loner_player, round_players)
                    # player.card_choice_question(i)
                    ####
                    #testprint
                    # print("card_choice " + str(card_choice))
                    # while True:
                        # renege_pass_fail = self.renege_check(laid_down, total_hands, player_deck, trump_suit, card_choice_number)
                        # if renege_pass_fail == "all clear":
                            # break
                        # else:
                            # card_choice_number = renege_pass_fail
                            # card_choice = player_deck[card_choice_number - 1]
                # elif type(player) == AI:
                    # if laid_down:
                        # card_choice = AI.card_choice_question(self, i, player, self.player_order, player_picked_up, trump_suit, laid_down, round_players, \
                             # team_picked_up, loner_player,player_deck)
                        # player.card_choice_question(i)
                        ####
                        #testprint
                        # print("card_choice " + str(card_choice))
                        # print("{0} has chosen to play the {1} of {2}.".format(player.name, card_choice.get_card_name(), card_choice.get_suit()))
                    # else:
                        # card_choice = AI.first_chooser_card_choice(self, trump_suit, player_deck)
                        # card_choice = player.first_chooser_card_choice(i)
                        ####
                        #testprint
                        # print("card_choice " + str(card_choice))
                        # print("{0} has chosen to play the {1} of {2}.".format(player.name, card_choice.get_card_name(), card_choice.get_suit()))
                        # print("{0} has chosen to play the {1} of {2}.".format(player.name, card_choice.get_card_name(), card_choice.get_suit()))
                ####
                # print(testprint)
                # print("card_choice + suit and name")
                # print(card_choice)
                # print(card_choice.get_suit())
                # print(card_choice.get_card_name())
                # laid_down.append(card_choice)
                # round_players.append(player)
                # deck_order_c[i].remove(card_choice)
            # mc_player_index = self.determine_highest(laid_down)
            # last_hand_winning_card = laid_down[mc_player_index]
            # winning_player = self.player_order[mc_player_index]
            # self.hand_winning_player(winning_player, last_hand_winning_card)
            # if winning_player in Euchre.team_1:
                # team_1_hands_won += 1
            # if winning_player in Euchre.team_2:
                # team_2_hands_won += 1
            # total_hands = team_1_hands_won + team_2_hands_won

        # winning_team, points_awarded = self.round_winner_points(team_1_hands_won, team_2_hands_won, team_picked_up, loner_player)    
        # return winning_team, points_awarded, team_1_hands_won, team_2_hands_won
    
    def hand_to_next_player(self, player):
        self.print_spaces(7)
        print("Please hand the computer to {}".format(player.name))
        print("\nPress Enter if you are {} and you are ready to view your hand".format(player.name))
        self.print_spaces(7)
        input()
    
    def set_starting_player(self,):
        starting_player = self.winning_player
        loner_team_member = ""
        loner_team_member_index = None
        if self.total_hands == 0:
            starting_player_index = 0 if self.dealer == Euchre.players[-1] else ((Euchre.players.index(self.dealer)) + 1)
            starting_player = (Euchre.players[starting_player_index])
        self.player_order, self.deck_order = self.euchre_player_order(starting_player)
        if self.loner_player != "no":
            loner_team_member = Euchre.player_opposites[self.loner_player]
            loner_team_member_index = self.player_order.index(loner_team_member)
            self.player_order.pop(loner_team_member_index)
            self.deck_order.pop(loner_team_member_index)
    
        
    def hand_winning_player(self, winning_player, winning_card):
        self.print_spaces(5)
        print("{0} won this hand with the {1} of {2}.\n\n".format(winning_player.name, winning_card.get_card_name(), winning_card.get_suit()))
        print("Press enter when you are ready to start the next hand")
        self.print_spaces(5)
        input()

    def round_winner_points(self, team_1_hands_won, team_2_hands_won, team_picked_up, loner_player):
        winning_team, hands_won = "", 0
        points_awarded = 0
        if team_1_hands_won > team_2_hands_won:
            winning_team, hands_won = Euchre.team_1, team_1_hands_won
        else:
            winning_team, hands_won = Euchre.team_2, team_2_hands_won
        if winning_team == team_picked_up and hands_won == 5:
            if loner_player != "no" and loner_player in team_picked_up:
                points_awarded = 4
            else:
                points_awarded = 2
        elif winning_team == team_picked_up and hands_won < 5:
            points_awarded = 1
        else:
            points_awarded = 2
        return winning_team, points_awarded

    def print_spaces(self, num_spaces):
        print("\n\n---------------------------------------------------------------------------------------")
        for i in range(num_spaces):  
            print("---------------------------------------------------------------------------------------------")
        return

    def hand_winner_announcement(self, winning_team, team_1_hands_won, team_2_hands_won, team_1_score, team_2_score):
            self.print_spaces(4)
            print("{win_team_str} won this hand with {win_team_hands_won} tricks".format(win_team_str = "Team 1" if winning_team\
            == Euchre.team_1 else "Team 2", win_team_hands_won = team_1_hands_won if winning_team == Euchre.team_1 else team_2_hands_won))
            print("The scores are now: \nTeam 1: {} \nTeam 2: {}".format(self.team_1_score, self.team_2_score))
            self.print_spaces(4)
            if self.team_1_score + self.team_2_score <= 10:
                input("Press Enter when you are ready to begin the next hand.")


    def play_euchre(self):
        window.titleframe_encase()
        #counter = 0
        
    def euchre_shuffle(self):
        #while self.team_1_score < 10 and self.team_2_score < 10:
        Euchre.true_decks, Euchre.leftover_deck = self.deal_deck(4, 4, 0)
        Euchre.deck_order_standard = Euchre.true_decks
        Euchre.player_1_deck, Euchre.player_2_deck, Euchre.player_3_deck, Euchre.player_4_deck = Euchre.deck_order_standard[0], Euchre.deck_order_standard[1], \
        Euchre.deck_order_standard[2], Euchre.deck_order_standard[3]
        Euchre.trump_suit_card = self.set_trump(Euchre.leftover_deck)
        self.set_dealer()
    
    def set_dealer(self):
        print("Euchre players = " + str(Euchre.players))
        set_dealer_frame = LabelFrame(window)
        set_dealer_frame.place(relx = .34, rely = .34)
        label_text = ("arial", 16, "bold")
        self.counter += 1
        if self.counter == 1:
            self.dealer = Euchre.Player_2
        else:
            self.dealer = Euchre.players[0] if self.dealer == Euchre.players[3] else Euchre.players[self.dealer_index+1]
        print("self.counter = " + str(self.counter))
        print("self.dealer = " + str(self.dealer))
        round_number = [None, "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th" \
                            "15th", "16th", "17th", "18th", "19th"]
        dealing_label = ttk.Label(set_dealer_frame, text = "We are now beginning the {0} round of Euchre.\n\n\n {1} is dealing the cards...".format(round_number[self.counter], self.dealer.name))
        dealing_label.configure(font = label_text)
        dealing_label.grid(column = 0, row = 0)
        self.dealer_index = Euchre.players.index(self.dealer)
        print("dealer index = " + str(self.dealer_index))
        print("deck order standard = " + str(Euchre.deck_order_standard))
        window.after(1000, lambda: [window.delete_window_widgets(), self.set_orders()])
    
    def set_orders(self):
        self.trump_suit, self.trump_card = Euchre.trump_suit_card.get_suit(), Euchre.trump_suit_card.get_card_name()
        if self.dealer_index == 4:
                first_caller = (Euchre.players[0]).name
        else:
            first_caller = Euchre.Player_1 if self.dealer == Euchre.Player_4 else Euchre.players[(self.dealer_index+1)]
        self.player_order, self.deck_order = self.euchre_player_order(first_caller)
        print("self.player_order, self.deck_order = ")
        print(self.player_order)
        print(self.deck_order)
        print("\n\n")
        trump_info_list = self.pick_up_scene()     
        # winning_team, points_awarded, team_1_hands_won, team_2_hands_won = self.euchre_round(self.dealer, trump_info_list, trump_suit, trump_card)

            # if winning_team == Euchre.team_1:
                # team_1_score += points_awarded
            # elif winning_team == Euchre.team_2:
                # team_2_score += points_awarded
            # self.hand_winner_announcement(winning_team, team_1_hands_won, team_2_hands_won, team_1_score, team_2_score)
            # self.dealer_index = Euchre.players.index(self.dealer)
            # self.dealer = Euchre.players[0] if self.dealer == Euchre.players[3] else Euchre.players[self.dealer_index+1]
            # self.counter += 1
            # self.counter = self.counter

        # if team_1_score or team_2_score >= 10:
            # if team_1_score >= 10:
                # self.print_spaces(7)
                # print("Congratulations Team 1, you won!")
                # self.print_spaces(5)
                # return
            # if team_2_score >= 10:
                # self.print_spaces(7)
                # print("Congratulations Team 2, you won!")
                # self.print_spaces(5)
                # return
    
    def space_label(self, column, row, num_space_labels = 1):
        num_space_labels_list = list(range(num_space_labels))
        for i in num_space_labels_list:
            space_label = Label(window, text = "               ").grid(column = column, row = row+i)
        

    def pick_up_scene(self):
        window.delete_window_widgets()
        self.human_player_index = self.player_order.index(self.human_player)
        self.empty_label = Label(window, text = "                                                      \n\n")
        self.empty_label.grid(column =0, row = 0)
        Card_game.tell_hand(self, self.deck_order[self.human_player_index], player = game_1.human_player)     
        self.pick_up_button = ttk.Button(window, text = "Pick up", state = "disabled", command = lambda: self.human_player.pick_up_decision(self.human_player_index, "no"))
        self.pick_up_button.grid(column = 2, row = 5)
        self.loner_button = ttk.Button(window, text = "Pick up and Go Alone", state = "disabled", command = lambda: self.human_player.pick_up_decision(self.human_player_index, game_1.player_order[i]))
        self.loner_button.grid(column = 3, row = 5)
        self.pass_button = ttk.Button(window, text = "Pass", state = "disabled", command = lambda: self.human_player.pass_decision(self.human_player_index))
        self.pass_button.grid(column = 4, row = 5)
        column_counter = 2
        self.space_label(0, 6, 2)
        self.player_response_1 = Label(window, text = "Has not gone yet")
        self.player_response_2 = Label(window, text = "Has not gone yet")
        self.player_response_3 = Label(window, text = "Has not gone yet")
        self.player_response_4 = Label(window, text = "Has not gone yet")
        self.player_response_label_list = [self.player_response_1, self.player_response_2, self.player_response_3, self.player_response_4]
        for person in self.player_order:
            if person != game_1.human_player:
                player_pass_pickup_icon = Label(image = person.get_pic()).grid(column = column_counter, row = 6)
                player_pass_pickup_name = Label(window, text = person.name).grid(column=column_counter, row = 7)
                n = self.player_order.index(person)
                self.player_response_label_list[n].grid(column=column_counter, row = 8)
                column_counter += 1
        window.empty_column_label(row = 7, num_column_spaces = 3)
        self.potential_trump_frame = ttk.LabelFrame(window, text = "Potential trump")
        self.potential_trump_frame.grid(column=8, row =6)
        self.potential_trump_label = ttk.Label(self.potential_trump_frame, image = Euchre.trump_suit_card.get_pic())
        self.potential_trump_label.grid(column = 0, row = 0, columnspan = 3)
        teams_dealer_labelframe = LabelFrame(window)
        teams_dealer_labelframe.grid(column =10, row = 4)
        team_1_label = Label(teams_dealer_labelframe, text = "Team 1", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_1_label.grid(column =0, row = 0, sticky = E+W)
        t1_players_label = Label(teams_dealer_labelframe, text = "{0} & {1}".format(Euchre.team_1[0].name, Euchre.team_1[1].name))
        t1_players_label.grid(column =0, row = 1, sticky = W)
        team_2_label = Label(teams_dealer_labelframe, text = "Team 2", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_2_label.grid(column =0, row = 2, sticky = E+W)
        t2_players_label = Label(teams_dealer_labelframe, text = "{0} & {1}".format(Euchre.team_2[0].name, Euchre.team_2[1].name))
        t2_players_label.grid(column =0, row = 3, sticky = W)
        team_1_label = Label(teams_dealer_labelframe, text = "Dealer", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_1_label.grid(column =0, row = 4, sticky = E+W)
        dealer_label = Label(teams_dealer_labelframe, text = self.dealer.name)
        dealer_label.grid(column =0, row = 5, sticky = W)
        self.pick_up_decide()

    def pick_up_decide(self, i = 0):
        if i >= 4:
            print("identified i >=4")
            self.call_it()
            return
        player = self.player_order[i]
        player_deck = self.deck_order[i]
        player.pick_up_questions_1(i, self.trump_card, self.trump_suit, self.dealer, player, \
                                            self.dealer_index, player_deck)  
    
    def dealer_removal_assign(self):
        self.dealer.dealer_removal_choice(Euchre.deck_order_standard[self.dealer_index], self.trump_suit, self.trump_card, self.dealer_index)
        
    def call_it(self, i = 0):
        self.pick_up_button.destroy()
        self.pass_button.destroy()
        self.loner_button.destroy()
        player = self.player_order[i]
        Card_game.tell_hand(self, self.deck_order[self.human_player_index], player = game_1.human_player)     
        self.call_it_button = ttk.Button(window, text = "call a suit", state = "disabled", command = lambda: game_1.human_player.call_it_decision_1(self.human_player_index, "no"))
        self.call_it_button.grid(column = 2, row = 5)
        self.loner_button = ttk.Button(window, text = "call a suit \nAND go alone", state = "disabled", command = lambda: game_1.human_player.call_it_decision_1(self.human_player_index, "yes"))
        self.loner_button.grid(column = 3, row = 5)
        self.pass_button = ttk.Button(window, text = "Pass", state = "disabled", command = lambda: game_1.human_player.pass_decision_callround(self.human_player_index))
        self.pass_button.grid(column = 4, row = 5)
        column_counter = 2
        self.space_label(0, 6, 4)
        self.player_response_1.configure(text = "Has not gone yet")
        self.player_response_2.configure(text = "Has not gone yet")
        self.player_response_3.configure(text = "Has not gone yet")
        self.player_response_4.configure(text = "Has not gone yet")
        self.potential_trump_frame.destroy()
        self.potential_trump_label.destroy()
        self.potential_trump_label = Label(window, image = Euchre.empty_potential_trump)
        self.potential_trump_label.grid(column = 8, row = 6)
        window.update()
        self.call_it_decide()

        

    
    def call_it_decide(self, i = 0):
        print("in call it decide")
        print("i = " + str(i))
        if i>= 4:
            print("error - this should never get to i ==4")
            return
        player = self.player_order[i]
        player_deck = self.deck_order[i]
        player.pick_up_questions_2(i, self.trump_card, self.trump_suit, self.dealer, self.dealer_index, player, \
                                                         player_deck)  
                                           
    
    def trump_info_list_printer(self):
        window.delete_window_widgets()
        print(self.trump_info_list)
        
    def renege_check(self, player_deck, card_choice_number):
        if game_1.laid_down and game_1.total_hands != 4:
            led_suit = (game_1.laid_down[0]).get_suit()
            case_deck = player_deck.copy()
            suits_in_hand = [card.get_suit() for card in case_deck]
            #testprint
            #print("Euchre.trump_suit_pairs[game_1.trump_suit] = " + str(Euchre.trump_suit_pairs[game_1.trump_suit]))
            #print("left bower = " + str(left_bower))
            left_bower = Euchre.left_bowers[game_1.trump_suit]
            if game_1.laid_down[0] == left_bower:
                led_suit = game_1.trump_suit
            if left_bower in case_deck:
                left_bower_index = case_deck.index(left_bower)
                suits_in_hand[left_bower_index] = game_1.trump_suit
            card_choice_index = card_choice_number
            case_deck_card_choice = case_deck[card_choice_index]
            case_deck_suit = case_deck_card_choice.get_suit() if case_deck_card_choice != left_bower else game_1.trump_suit
            if case_deck_suit != led_suit:
                if led_suit in suits_in_hand:
                    return "not clear"
                elif led_suit not in suits_in_hand:
                    return "all clear" 
            else:
                return "all clear"
        else:
            return "all clear"   

        return
    
class Player:
    player_1_icon = ImageTk.PhotoImage(Image.open("Player_1_icon.png"))
    player_2_icon = ImageTk.PhotoImage(Image.open("player_2_icon.png"))
    player_3_icon = ImageTk.PhotoImage(Image.open("player_3_icon.png"))
    player_4_icon = ImageTk.PhotoImage(Image.open("player_4_icon.png"))

    def __init__(self, name, pic):
        self.name = name
        self.pic = pic
    
    def get_pic(self):
        return self.pic

    def pick_up_questions_1(self, i, trump_card, trump_suit, dealer, player, dealer_index, player_deck):
        game_1.instructions_label =  Label(window, text = "{}, will you tell the dealer to pick it up?\n\n".format(player.name))
        game_1.instructions_label.place(relx=0, rely=(0), anchor=NW)
        game_1.pick_up_button.configure(state = "normal")
        game_1.loner_button.configure(state = "normal")
        game_1.pass_button.configure(state = "normal")
    
    def pick_up_decision(self, i, loner_decision):
        game_1.instructions_label.place_forget()
        game_1.trump_info_list = ["yes", game_1.player_order[i], game_1.trump_suit, loner_decision]
        if game_1.player_order[i] == game_1.dealer:
            self.player_is_dealer(i, player_is_dealer = "yes")
        else:
            game_1.instructions_label = Label(window, text = "You have told {} to pick up trump.".format(game_1.dealer.name))
            game_1.instructions_label.place(relx=0, rely=(0), anchor=NW)
            game_1.pick_up_button.configure(state = "disabled")
            game_1.loner_button.configure(state = "disabled")
            game_1.pass_button.configure(state = "disabled")
            game_1.dealer_removal_assign()
    
    def pass_decision(self, i):
        game_1.instructions_label.place_forget()
        game_1.pick_up_button.configure(state = "disabled")
        game_1.loner_button.configure(state = "disabled")
        game_1.pass_button.configure(state = "disabled")
        game_1.pick_up_decide(i = i+1)
    
    def player_is_dealer(self, i, player_is_dealer = "no"):
        player = game_1.dealer
        deck = Euchre.deck_order_standard[game_1.dealer_index]
        if player_is_dealer == "yes":
            game_1.instructions_label =  Label(window, text = "You are the dealer. Please click on the card from your hand that your would like to remove.".format(player.name))
            game_1.instructions_label.place(relx=0, rely=0, anchor=NW)
        else:
            game_1.instructions_label =  Label(window, text = "{} has told you to pick it up. Please click on the card from your hand that your would like to remove.".format(game_1.trump_info_list[1].name))
            game_1.instructions_label.place(relx=0, rely=0, anchor=NW)
        deletes_list = [game_1.pick_up_button, game_1.pass_button, game_1.loner_button]
        for item in deletes_list:
            item.destroy()
        for item in game_1.card_labels_list:
            if item:
                item.destroy()
        for item in game_1.player_response_label_list:
            item.destroy()
        column, row = 0, 2
        counter = 1
        self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5 = Button(window), Button(window), Button(window), Button(window), Button(window)
        self.buttons_list = [self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5]
        tell_hand_label = Label(text = "The cards in your hand are: \n").grid(column = column, row = row)
        for item in deck:
            n = deck.index(item)
            print("n = " + str(n))
            card_picture = item.get_pic()
            print("self.buttons_list[n] = " + str(self.buttons_list[n]))
            self.buttons_list[n].configure(image = card_picture, command = lambda n = n, counter = counter: self.dealer_removal_replace(n, counter))
            self.buttons_list[n].grid(column = counter, row = 4)
            counter += 1
    
    def dealer_removal_replace(self, card_choice_index, counter):
        game_1.instructions_label.configure(text = " Your deck has been updated")
        self.clb_1.configure(state = 'disabled')
        self.clb_2.configure(state = 'disabled')
        self.clb_3.configure(state = 'disabled')
        self.clb_4.configure(state = 'disabled')
        self.clb_5.configure(state = 'disabled')
        self.buttons_list[card_choice_index].destroy()
        trump_card_in_label = Label(window, image = Euchre.trump_suit_card.get_pic())
        trump_card_in_label.grid(column = counter, row = 4)
        #window.update()
        game_1.potential_trump_label.destroy()
        Euchre.deck_order_standard[game_1.dealer_index].pop(card_choice_index)
        Euchre.deck_order_standard[game_1.dealer_index].append(Euchre.trump_suit_card)
        window.after(1000, lambda: game_1.show_trump())
        
            

    def pick_up_questions_2(self, i, trump_card, trump_suit, dealer, dealer_index, player, player_deck):
        game_1.instructions_label = Label(window, text = "{}, would you like to call a suit as trump?\n\n".format(player.name))
        game_1.instructions_label.place(relx=0, rely=(0), anchor=NW)
        game_1.call_it_button.configure(state = "normal")
        game_1.loner_button.configure(state = "normal")
        if i != 3:
            game_1.pass_button.configure(state = "normal")
        window.update()

    def call_it_decision_1(self, i,loner_decision):
        game_1.call_it_button.grid_forget()
        game_1.loner_button.grid_forget()
        game_1.pass_button.grid_forget()
        if loner_decision == "yes":
            call_spades_button = ttk.Button(window, text = "call spades", command = lambda: self.call_it_decision_2(i, player, "spades")).grid(column = 2, row = 5)
            call_clubs_button = ttk.Button(window, text = "call clubs", command = lambda: self.call_it_decision_2(i, player, "clubs")).grid(column = 3, row = 5)
            call_diamonds_button = ttk.Button(window, text = "call diamonds", command = lambda: self.call_it_decision_2(i, player, "diamonds")).grid(column = 4, row = 5)
            call_hearts_button = ttk.Button(window, text = "call hearts", command = lambda: self.call_it_decision_2(i, player, "hearts")).grid(column = 5, row = 5)
        else:
            call_spades_button = ttk.Button(window, text = "call spades", command = lambda: self.call_it_decision_2(i, "no", "spades")).grid(column = 2, row = 5)
            call_clubs_button = ttk.Button(window, text = "call clubs", command = lambda: self.call_it_decision_2(i, "no", "clubs")).grid(column = 3, row = 5)
            call_diamonds_button = ttk.Button(window, text = "call diamonds", command = lambda: self.call_it_decision_2(i, "no", "diamonds")).grid(column = 4, row = 5)
            call_hearts_button = ttk.Button(window, text = "call hearts", command = lambda: self.call_it_decision_2(i, "no", "hearts")).grid(column = 5, row = 5)

    
    def call_it_decision_2(self, i, loner_player, suit):
        game_1.instructions_label.place_forget()
        window.update()
        game_1.trump_info_list = ["no", game_1.player_order[i], suit, loner_player]
        game_1.trump_suit = suit
        game_1.trump_card = None
        window.after(1000, lambda: game_1.show_trump())
        
    
    def pass_decision_callround(self, i):
        game_1.instructions_label.place_forget()
        print(" i = " + str(i))
        game_1.call_it_decide(i = i+1)

            
    def card_choice_question(self, i, player_deck):
        self.instructions_label = Label(window, text = "\n It's your turn. Click on the card you would like to play")
        labelFont = ("arial", 16, "normal")
        self.instructions_label.configure(font = labelFont)
        self.instructions_label.place(relx = .28, rely = .47)
        for button in game_1.buttons_list:
            button.configure(state = "normal")

    def human_card_choice_check(self, n):
        
        self.instructions_label.configure(text = "")
        self.instructions_label.place(relx = .28, rely = .47)
        window.update()
        i = game_1.player_order.index(game_1.human_player)
        player_deck = game_1.deck_order[i]
        card_choice = (game_1.deck_order[i])[n]
        # self.tell_hand_buttons_list[n] = Label(window, image = Euchre.empty_potential_trump)
        # self.tell_hand_buttons_list[n].grid(column = 5+i, row = 5)
        
        renege_pass_fail = game_1.renege_check(player_deck, n)
        if renege_pass_fail == "all clear":
            print("renege pass fail passed")
            game_1.buttons_list[n].destroy()
            game_1.buttons_list.pop(n)
            
            
            for button in game_1.buttons_list:
                button.configure(state = "disabled")

            game_1.laid_down.append(card_choice)
            game_1.round_players.append(game_1.player_order[i])
            self.card_play_lf = LabelFrame(window, text = game_1.human_player.name)
            self.card_play_lf.grid(column = 5 + i, row = 2)
            self.card_play_label = Label(self.card_play_lf, image = card_choice.get_small_pic())
            self.card_play_label.grid(column = 0, row = 0)
            game_1.deck_order[i].remove(card_choice)
            game_1.euchre_trick(i = i+1)
        
        else:
            self.renege_failed()
    
    def renege_failed(self):
        print("in renege failed")
        self.instructions_label.configure(text = "It appears you are able to follow suit, so you must do so. Please choose a different card.", fg = "red")
        self.instructions_label.place(relx = .19, rely = .47)
        window.update()
        
        
        

        
class AI:
    player_1_icon = ImageTk.PhotoImage(Image.open("Player_1_icon.png"))
    player_2_icon = ImageTk.PhotoImage(Image.open("player_2_icon.png"))
    player_3_icon = ImageTk.PhotoImage(Image.open("player_3_icon.png"))
    player_4_icon = ImageTk.PhotoImage(Image.open("player_4_icon.png"))
    
    def __init__(self, name, pic):
        self.name = name
        self.pic = pic
    
    def get_pic(self):
        return self.pic

    def pick_up_questions_1(self, i, trump_card, trump_suit, dealer, player, dealer_index, player_deck):
        loner_player = "no"
        pick_up_decision = "no"
        player_deck_c = player_deck.copy()
        trumpst_card_names = []
        off_trump_suits = []
        off_trump_card_names = []
        dec_num = random.random()
        dealer_on_team = "yes" if ((player in Euchre.team_1 and dealer in Euchre.team_1) or \
                                   (player in Euchre.team_2 and dealer in Euchre.team_2)) else "no"
        #testprint
        #print("dec_num = " + str(dec_num))
        left_bower = Euchre.left_bowers[trump_suit]
        for card in player_deck_c:
            if card == left_bower:
                trumpst_card_names.append("jack_lft")
            elif card.get_suit() == trump_suit:
                trumpst_card_names.append(card.get_card_name())
            else:
                off_trump_suits.append(card.get_suit()) 
                off_trump_card_names.append(card.get_card_name())
        #testprint
        #print("off trump suits = " + str(off_trump_suits))
        #print("off trump card names = " + str(off_trump_card_names))
        #print("trumpst_card_names = " + str(trumpst_card_names))
        #print("dealer_on_team = " + str(dealer_on_team))
        if player == dealer:
            #print("went into player is dealer")
            loner_player, pick_up_decision = AI.player_is_dealer(self, trumpst_card_names, dec_num, trump_card)
        elif len(trumpst_card_names) == 4:
            #print("went into four_cards_trump")
            loner_player, pick_up_decision = AI.four_cards_trump(self, trumpst_card_names, off_trump_suits, off_trump_card_names, dec_num)
        elif len(trumpst_card_names) == 3:
            #print("went into 3 cards trump")
            loner_player, pick_up_decision = AI.three_cards_trump(self, trumpst_card_names, off_trump_suits, off_trump_card_names, \
                                                               dealer_on_team, trump_card, dec_num)
        elif len(trumpst_card_names) == 2:
            #print("went into 2 cards trump")
            loner_player, pick_up_decision = AI.two_cards_trump(self, trumpst_card_names, off_trump_suits, off_trump_card_names, \
                                                               dealer_on_team, trump_card, dec_num)
        if pick_up_decision == "yes":
            print("pick up decision == yes")
            window.update()
            window.after(1000, game_1.player_response_label_list[i].configure(text = "called pick up", fg = "red"))
            window.update()
            if loner_player != "no":
                game_1.trump_info_list = ["yes", game_1.player_order[i], game_1.trump_suit, game_1.player_order[i]]
            else:
                game_1.trump_info_list = ["yes", game_1.player_order[i], game_1.trump_suit, "no"]
            if game_1.dealer == game_1.human_player:
                window.after(1000, lambda: game_1.human_player.player_is_dealer(i))
            else:
                game_1.instructions_label = Label(window, text = "{0} has told {1} to pick up trump.".format(game_1.player_order[i].name, game_1.dealer.name))
                game_1.instructions_label.place(relx=0, rely=(0), anchor=NW)
                game_1.dealer_removal_assign()
            
        else:
            self.pass_decision(i)
    
    def pass_decision(self, i):
        print("in pass decision")
        window.update()
        window.after(1000, game_1.player_response_label_list[i].configure(text = "pass"))
        window.update()
        window.after(1000, game_1.pick_up_decide(i = i+1))
        
    def player_is_dealer(self, trumpst_card_names, dec_num, trump_card):
        #testprint
        #print("now in player is dealer")
        #print("trumpst card names" + str(trumpst_card_names))
        loner_player = "no"
        pick_up_decision = "no"
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        trumpst_card_names.append(trump_card)
        trump_cards_num = len(trumpst_card_names) if trumpst_card_names else None
        #print("trumpst_card_names after trump card added = " + str(trumpst_card_names))
        #print("trump_cards_num = " + str(trump_cards_num))
        if trump_cards_num >= 5:
            #print("1")
            loner_player, pick_up_decision = "yes", "yes"
        elif trump_cards_num == 4:
            #print("2")
            comp_deck_ct_1 = len([i for i in trumpst_card_names if i in [9,10]])
            loner_player, pick_up_decision = ("yes", "yes") if not comp_deck_ct_1 == 2 else ("no", "yes")
        elif trump_cards_num == 3:
            #print("3")
            comp_deck_ct_1 = len([i for i in trumpst_card_names if i in [9, 10]])
            comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["queen", "king"]])
            pick_up_decision = "yes" if comp_deck_ct_1 != 2 and comp_deck_ct_2 == 1 else ("yes" if dec_num <.15 else "no")
        elif trump_cards_num == 2:
            #print("4")
            comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft"]])
            comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
            comp_deck_ct_3 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace", "king"]])
            comp_deck_ct_4 = len([i for i in trumpst_card_names if i in ["9", "10", "queen", "king"]])
            if (comp_deck_ct_1 == 2) or (comp_deck_ct_2 == 2 and dec_num < .75) or (comp_deck_ct_3 ==2 and dec_num < .33)\
                or (comp_deck_ct_4 == 1 and dec_num < .2) or (comp_deck_ct_2 == 1 and dec_num < .1):
                pick_up_decision = "yes"
            else:
                pick_up_decision = "no"
        #print("comp decks")
        #print(comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6)
                
        #print("loner player, pick up decision = " + str(loner_player) + "," + str(pick_up_decision))
        ####
        return loner_player, pick_up_decision     
                
        
    def four_cards_trump(self, trumpst_card_names, off_trump_suits, off_trump_card_names, dec_num):
        #print("now in four cards trump")
        #print("trumpst card names" + str(trumpst_card_names))
        #print("off_trump_suits =" + str(off_trump_suits))
        #print("off_trump_card_names = " + str(off_trump_card_names))
        #print("dec_num = " + str(dec_num))
        loner_player = "no"
        pick_up_decision = "no"
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4 = 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
        comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["king", "queen"]])
        if "ace" in off_trump_card_names:
            #print("1")
            comp_deck_ct_3 = 2
        elif "king" in off_trump_card_names:
            #print("1")
            comp_deck_ct_3 = 1
        loner_player, pick_up_decision = ("yes", "yes") if (comp_deck_ct_1 == 3) or (comp_deck_ct_1 == 2 and comp_deck_ct_2 == 2) \
            or (comp_deck_ct_1 == 2 and comp_deck_ct_1 == 1 and comp_deck_ct_3 == 2 and dec_num < .9) \
            or (comp_deck_ct_1 == 2 and comp_deck_ct_1 == 1 and comp_deck_ct_3 == 1 and dec_num < .7) \
            or (comp_deck_ct_1 == 2 and comp_deck_ct_2 == 1 and dec_num < .4) else ("no", "yes")
        #print("comp decks")
        #print(comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6)
                
        #print("loner player, pick up decision = " + str(loner_player) + "," + str(pick_up_decision))
        return loner_player, pick_up_decision
        
        
    def three_cards_trump(self, trumpst_card_names, off_trump_suits, off_trump_card_names, dealer_on_team, trump_card, dec_num):
        #print("now in 3 cards trump")
        #print("trumpst card names" + str(trumpst_card_names))
        #print("off_trump_suits =" + str(off_trump_suits))
        #print("off_trump_card_names = " + str(off_trump_card_names))
        #print("dec_num = " + str(dec_num))
        #print("dealer on team = " + str(dealer_on_team))
        loner_player = "no"
        pick_up_decision = "no"
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
        comp_deck_ct_2 = off_trump_card_names.count("ace")
        comp_deck_ct_3 = off_trump_card_names.count("king")
        comp_deck_ct_4 = len([i for i in trumpst_card_names if i in [9, 10, "queen"]])
        comp_deck_ct_5 = len([i for i in trumpst_card_names if i in [9, 10]])
        comp_deck_ct_6 = len([i for i in trumpst_card_names if i in ["king", "ace", "jack", "jack_lft"]])
        if (comp_deck_ct_1 == 3):
            #print("1")
            loner_player, pick_up_decision = "yes", "yes"
        elif comp_deck_ct_1 == 2 and (comp_deck_ct_3 >= 2 or (comp_deck_ct_3 >=1 and comp_deck_ct_4>=1)):
            #print("2")
            loner_player, pick_up_decision = ("yes", "yes") if dec_num < .85 else ("no", "yes")  
        elif comp_deck_ct_4 == 3:
            #print("3")
            loner_player, pick_up_decision = ("no", "yes") if (dealer_on_team == "yes" and trump_card != "king") else ("no", "no")
        elif comp_deck_ct_5 == 2 and comp_deck_ct_6 >=1:
            #print("4")
            loner_player, pick_up_decision = ("no", "yes") if dealer_on_team == "yes" else (("no", "no") if dec_num < .9 else ("no", "yes"))
        else:
            #print("5")
            loner_player, pick_up_decision = ("no", "yes") if dealer_on_team == "yes" else \
            (("no", "yes") if (trump_card == "jack" or trump_card == "jack_lft") and dec_num < .5 else \
            (("no", "yes") if dec_num < 25 else ("no", "no")))
        #print("comp decks")
        #print(comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6)
                
        #print("loner player, pick up decision = " + str(loner_player) + "," + str(pick_up_decision))
        return loner_player, pick_up_decision
    
    
    def two_cards_trump(self, trumpst_card_names, off_trump_suits, off_trump_card_names, dealer_on_team, trump_card, dec_num):
        loner_player = "no"
        pick_up_decision = "no"
        #print("now in 2 cards trump")
        #print("trumpst card names" + str(trumpst_card_names))
        #print("off_trump_suits =" + str(off_trump_suits))
        #print("off_trump_card_names = " + str(off_trump_card_names))
        #print("dec_num = " + str(dec_num))
        #print("dealer on team = " + str(dealer_on_team))
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft"]])
        comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
        comp_deck_ct_3 = len([i for i in trumpst_card_names if i in [9, 10]])
        
        if comp_deck_ct_1 == 2:
            #print("1")
            pick_up_decision == "yes" 
        elif comp_deck_ct_2 == 2:
            #print("2")
            if dealer_on_team == "yes":
                pick_up_decision = "yes"
            if dealer_on_team == "no":
                pick_up_decision = "yes" if trump_card not in ["jack", "jack_lft", "ace", "king"]  else ("yes" if dec_num < .7 else "no")
        elif comp_deck_ct_3 == 2:
            #print("3")
            if dealer_on_team == "yes" and trump_card == "jack":
                pick_up_decision = "yes"
            elif dealer_on_team == "yes" and trump_card_in ["jack_lft", "ace"]:
                pick_up_decision = "yes" if dec_num < .15 else "no"
            else:
                pick_up_decision == "no"
        else:
           # print("4")
            if dealer_on_team == "yes":
                pick_up_decision = "yes" if dec_num < .5 else "no"
            if dealer_on_team == "no":
                pick_up_decision = "no"
        #print("comp decks")
        #print(comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6)
                
        #print("loner player, pick up decision = " + str(loner_player) + "," + str(pick_up_decision))
        return loner_player, pick_up_decision
    
    def dealer_removal_choice(self, player_deck, trump_suit, trump_card, dealer_index):
        print("deck_order_standard at dealer index = " + str(Euchre.deck_order_standard[game_1.dealer_index]))
        player_deck_c = player_deck.copy()
        player_deck_c.append(Euchre.trump_suit_card)
        left_bower = Euchre.left_bowers[trump_suit]
        clubs_list, spades_list, diamonds_list, hearts_list = [], [], [], []
        all_suits_nested_list = [clubs_list, spades_list, diamonds_list, hearts_list]
        trump_list_matchup = {"clubs": clubs_list, "spades": spades_list, "diamonds": diamonds_list, "hearts": hearts_list} 
        for card in player_deck_c:
            if card == left_bower:
                trump_list_matchup[trump_suit].append(card)
            elif card.get_suit() == "spades":
                spades_list.append(card)
            elif card.get_suit() == "clubs":
                clubs_list.append(card)
            elif card.get_suit() == "hearts":
                hearts_list.append(card)
            elif card.get_suit() == "diamonds":
                diamonds_list.append(card)
        #testprint
        #print("player_deck_c = " + str(player_deck_c))
        #print("trump_suit = " + str(trump_suit))
        #print("all suits nestes list" + str(all_suits_nested_list))
        #print("individual lists" + str(clubs_list) + str(spades_list) + str(diamonds_list) + str(hearts_list))
        trump_list = trump_list_matchup[trump_suit]
        #print("trump_list = " + str(trump_list))
        all_suits_nested_list.remove(trump_list)
        #print("all suits nested list after trump list removed" + str(all_suits_nested_list))
        removal_list = None
        #testprints within here
        for list in all_suits_nested_list:
            if len(list) < 1:
                all_suits_nested_list.remove(list)
        if len(trump_list) == 6:
           # print("found trump_list length == 6")
            removal_list = trump_list
        elif len(trump_list) == 5 or len(all_suits_nested_list) == 1:
           # print("found len(trump_list) == 5 or len(all_suits_nested_list) == 1")
            removal_list = all_suits_nested_list[0]
        elif len(trump_list) >= 2 and len(all_suits_nested_list) >= 2:
           # print("found len(trump_list) >= 2 and len(all_suits_nested_list) >= 2")
            shortest_suit = min(all_suits_nested_list, key=len)
            removal_list = shortest_suit
        
        else:
            #print("found that there are less than 4 trump cards and the scenario where there are multiple trump cards and \
            #2 or more off suits is not met. list will be flattened and chosen from all offsuit cards")
            all_off_suits_list = []
            for item in all_suits_nested_list:
                for card in item:
                    all_off_suits_list.append(card)
            #testprint
            #print(all_off_suits_list)
            removal_list = all_off_suits_list
                
        #testprint
        #print("all suits nested list after empty lists removed = " + str(all_suits_nested_list))
        #print("removal_list = " + str(removal_list))
        removal_list_values = [Euchre.card_values_trump[card.get_card_name()] for card in removal_list] if removal_list == trump_list else \
                               [Euchre.card_values_nontrump[card.get_card_name()] for card in removal_list]
    
        removal_card_index = removal_list_values.index(min(removal_list_values))
        removal_card = removal_list[removal_card_index]
        #testprint
        #print("removal_list_values = " + str(removal_list_values))
        #print("removal_card_index = " + str(removal_card_index))
        #print("removal_card = " + str(removal_card))
        
        #testprint
        #print("Euchre.deck_order_standard = " + str(Euchre.deck_order_standard))
        #print("dealer_index =" + str(dealer_index))
        #print("Euchre.deck_order_standard[dealer_index] = " + str(Euchre.deck_order_standard[dealer_index]))
        Euchre.deck_order_standard[dealer_index].remove((removal_card))
        
        Euchre.deck_order_standard[dealer_index].append(Euchre.trump_suit_card)
        #print("Euchre.deck_order_standard[dealer_index] after removal = " + str(Euchre.deck_order_standard[dealer_index]))
        
        print("deck_order_standard at dealer index = " + str(Euchre.deck_order_standard[game_1.dealer_index]))
        
        #need to disable your cards so you can't choose anything and then write at the top. You have told {dealer} to pick it up. 
        #in red under the dealer AI player - "choosing card to remove". Wait 1 second and then move on to the next thing
        game_1.player_response_label_list[3].configure(text = "removing card \n   from deck", fg = "red")
        window.update()
        window.after(1000)
        game_1.player_response_label_list[3].configure(text = "card removed", fg = "red")
        window.update()
        window.after(1000, lambda: game_1.show_trump())
        

        
                                

    def pick_up_questions_2(self, i, trump_card, trump_suit, dealer, dealer_index, player, player_deck):
        print("in pick_up_questions_2 for AI")
        #testprint
        #print("player_deck coming in to pick up questions 2 = " + str(player_deck))
        #print("trump_suit = " + str(trump_suit))
        loner_player = "no"
        called_suit = None
        dec_num = random.random()
        player_deck_c = player_deck.copy()
        left_bower = Euchre.left_bowers[trump_suit]
        clubs_list, spades_list, diamonds_list, hearts_list = ["clubs"], ["spades"], ["diamonds"], ["hearts"]
        all_suits_nested_list = [clubs_list, spades_list, diamonds_list, hearts_list]
        trump_list_matchup = {"clubs": clubs_list, "spades": spades_list, "diamonds": diamonds_list, "hearts": hearts_list} 
        for card in player_deck_c:
            if card == left_bower:
                trump_list_matchup[trump_suit].append("jack_lft")
            elif card.get_suit() == "spades":
                spades_list.append(card.get_card_name())
            elif card.get_suit() == "clubs":
                clubs_list.append(card.get_card_name())
            elif card.get_suit() == "hearts":
                hearts_list.append(card.get_card_name())
            elif card.get_suit() == "diamonds":
                diamonds_list.append(card.get_card_name())
        #testprints all throughout below
        #print("all suits nested list in pick_up_questions 2 = " + str(all_suits_nested_list))
        other_suits_in_deck = 0
        other_cards_in_deck = []
        trump_suit_list = []
        for list in all_suits_nested_list:
            #print("in trump_suit list/ other lists builder pick up qs 2, list  = " + str(list))
            #print("list[0] = " + str(list[0]))
            if list[0] == trump_suit:
                #print("found that list[0] == trump_suit")
                trump_suit_list = list
                #print("trump_suit_list after finding this and supposedly changing = " + str(trump_suit_list))
            elif len(list) > 1:
                other_suits_in_deck += 1
                for card in list[1:]:
                    other_cards_in_deck.append(card)
        if len(trump_suit_list)-1 == 5:
            #print("found len(list)-1 == 5")
            called_suit = list[0]
        elif len(trump_suit_list)-1 == 4:
            #print("found len(list)-1 == 4")
            loner_player, called_suit = AI.call_suit_4_card(self, trump_suit_list, dec_num)
        elif len(trump_suit_list)-1 == 3:
           # print("found len(list)-1 == 3")
            loner_player, called_suit = AI.call_suit_3_card(self, trump_suit_list, other_suits_in_deck, other_cards_in_deck, dec_num)
        elif (len(trump_suit_list)-1 ==2) and (("jack" in trump_suit_list and "jack_lft" in trump_suit_list) or \
                                               ("jack" in trump_suit_list and "king" in trump_suit_list) or \
                                    ("jack" in trump_suit_list and "queen" in trump_suit_list) or \
                                    (len([i for i in trump_suit_list if i in ["jack", "jack_lft", "ace"]]) == 2)):
            #print("found those other weird exception cases")
            called_suit = AI.call_suit_2_card(self, trump_suit_list, other_suits_in_deck, other_cards_in_deck, dec_num)
        #testprint
        #print("other suits in deck = " + str(other_suits_in_deck))
        #print("other_cards_in_deck = " + str(other_cards_in_deck))
        #print("trump_suit_list = " + str(trump_suit_list))
        
        if i == 3:
            called_suit = self.caller_force_choose(player_deck_c, trump_suit)
        
        if called_suit != None:
            window.after(1000, game_1.player_response_label_list[i].configure(text = "calling {}".format(called_suit), fg = "red"))
            window.update()
            if loner_player != "no":
                game_1.trump_info_list = ["no", game_1.player_order[i], called_suit, game_1.player_order[i]]
                window.after(1000, lambda: game_1.show_trump())
            else:
                game_1.trump_info_list = ["yes", game_1.player_order[i], called_suit, "no"]
            game_1.trump_suit = called_suit
            game_1.trump_card = None
            window.after(1000, lambda: game_1.show_trump())
        else:
            self.pass_decision_callround(i)
    
    def pass_decision_callround(self, i):
        window.after(1000, game_1.player_response_label_list[i].configure(text = "pass"))
        window.update()
        game_1.call_it_decide(i = i+1)

                                
    def call_suit_4_card(self, list, dec_num):
        #testprint
        #print("initiating call_suit_4_card")
        #print("list = " + str(list))
        loner_player = "no"
        called_suit = None
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in list if i in [9, 10, "queen", "king"]])
        comp_deck_ct_2 = len([i for i in list if i in ["ace", "jack", "jack_lft"]])
        comp_deck_ct_3 = len([i for i in list if i in [9, 10]])  
        #print("comp_deck_counts = ")
        #print(comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6)
        if comp_deck_ct_1 == 4:
            #print("1")
            loner_player, called_suit = ("no", list[0]) if dec_num <.9 else ("no", None)
        elif comp_deck_ct_2 == 3:
            #print("2")
            loner_player, called_suit = "yes", list[0]
        elif comp_deck_ct_2 == 2:
            #print("3")
            loner_player, called_suit = ("no", list[0]) if comp_deck_ct_3 == 2 else \
                               (("yes", list[0]) if dec_num < .75 else ("no", list[0]))
        else: 
            called_suit = list[0]     
        #testprint
        #print("loner_player, called_suit = " + str(loner_player) + ", " + str(called_suit))
        return loner_player, called_suit
    
    def call_suit_3_card(self, list, other_suits_in_deck, offsuit_cards_in_deck, dec_num):
        loner_player = "no"
        called_suit = None
        #testprint (all throughout)
        #print("initiating call_suit_4_card")
        #print("list = " + str(list))
        #print("other suits in deck = " + str(other_suits_in_deck))
        #print("offsuit_cards_in_deck = " + str(offsuit_cards_in_deck))
        #print("dec_num = " + str(dec_num))
        #testprint (these are all throughout here)
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in list if i in ["ace", "jack_lft", "jack"]])
        comp_deck_ct_2 = len([i for i in list if i in ["king", "ace", "jack_lft", "jack"]])
        comp_deck_ct_3 = len([i for i in list if i in ["queen", "king", "ace", "jack_lft", "jack"]])
        comp_deck_ct_4 = len([i for i in list if i in [9, 10]])
        comp_deck_ct_5 = len([i for i in list if i in ["jack_lft", "jack"]])
        #testprints
        #print("comp_deck_counts = ")
        #print(comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6)
        if comp_deck_ct_1 == 3:
            #print("1")
            loner_player, called_suit = "yes", list[0]
        elif (comp_deck_ct_1 == 2 and other_suits_in_deck == 1) or comp_deck_ct_5 == 2:
            #print("2")
            called_suit = list[0]
        elif comp_deck_ct_2 == 3 and other_suits_in_deck == 1:
            #print("3")
            if dec_num < .25:
                loner_player, called_suit = "yes", list[0]
            else:
                called_suit = list[0]
        elif comp_deck_ct_3 == 3:
            #print("4")
            called_suit = list[0]
        elif comp_deck_ct_4 == 2:
            print("5")
            if comp_deck_ct_5 == 1 and other_suits_in_deck == 1:
                called_suit = list[0] if dec_num > .9 else None
            elif comp_deck_ct_5 == 1 and other_suits_in_deck > 1:
                called_suit = list[0] if dec_num < .5 else None
            elif comp_deck_ct_1 == 1 and other_suits_in_deck == 1:
                called_suit = list[0] if dec_num < .65 else None
            else:
                called_suit = None
        else:
            #print("6")
            called_suit = list[0] if dec_num < .5 else None       
        print("loner_player, called_suit = " + str(loner_player) + str(called_suit))
        
        return loner_player, called_suit
    
    def call_suit_2_card(self, list, other_suits_in_deck, offsuit_cards_in_deck, dec_num):
        called_suit = None 
        #testprint (all throughout)
        #print("initiating call_suit_4_card")
        #print("list = " + str(list))
        #print("other suits in deck = " + str(other_suits_in_deck))
        #print("offsuit_cards_in_deck = " + str(offsuit_cards_in_deck))
        #print("dec_num = " + str(dec_num))
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in list if i in ["jack_lft", "jack"]])
        comp_deck_ct_2 = len([i for i in list if i in ["ace", "jack_lft", "jack"]])
        comp_deck_ct_3 = len([i for i in list if i in ["king", "jack"]])                      
        comp_deck_ct_4 = len([i for i in list if i in ["queen", "jack"]])   
        #testprints
        #print("comp_deck_counts = ")
        #print(comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6)
        if comp_deck_ct_1 == 2:
            #print("1")
            called_suit = list[0]
        
        elif other_suits_in_deck == 1:
            #print("2")
            if "ace" in offsuit_cards_in_deck:
                #print("2-1")
                called_suit = list[0] if comp_deck_ct_2 == 2 else \
                            (list[0] if ((comp_deck_ct_3 == 2 and dec_num < .9) or \
                                        (comp_deck_ct_4 == 2 and dec_num < .4)) else None)
            elif "king" in offsuit_cards_in_deck:
                #print("2-2")
                called_suit = list[0] if comp_deck_ct_2 == 2 and dec_num < .8 else \
                               (list[0] if (comp_deck_ct_4 == 2 and dec_num < .10) else None)
            elif comp_deck_ct_2 == 2:
                #print("2-3")
                called_suit = list[0] if dec_num < .5 else None
            elif comp_deck_ct_3 == 2:
                #print("2-4")
                called_suit = list[0] if dec_num < .4 else None
        elif other_suits_in_deck == 2:
            #print("3")
            if "ace" in offsuit_cards_in_deck:
                #print("3-1")
                called_suit = list[0] if comp_deck_ct_2 == 2 and dec_num < .4 else None
            elif comp_deck_ct_3 ==  2:
                #print("3-2")
                called_suit == list[0] if dec_num < .15 else None
        elif other_suits_in_deck == 3:
            #print("4")
            if comp_deck_ct_3 == 2:
                #print("4-1")
                called_suit = list[0] if (dec_num < .15 and "ace" in off_suit_cards_in_deck) else \
                               (list[0] if dec_num < .5 else None)
        #print("called_suit = " + str(called_suit))
        return called_suit
    
    def caller_force_choose(self, player_deck_c, trump_suit):
        #testprint
        #rint("trump_suit in caller_force_choose = " + str(trump_suit))
        #called_suit = None
        left_bower = Euchre.left_bowers[trump_suit]
        clubs_list, spades_list, diamonds_list, hearts_list = ["clubs"], ["spades"], ["diamonds"], ["hearts"]
        all_suits_nested_list = [clubs_list, spades_list, diamonds_list, hearts_list]
        trump_list_matchup = {"clubs": clubs_list, "spades": spades_list, "diamonds": diamonds_list, "hearts": hearts_list}       
        for card in player_deck_c:
            if card == left_bower:
                trump_list_matchup[trump_suit].append("jack_lft")
            elif card.get_suit() == "spades":
                spades_list.append(card.get_card_name())
            elif card.get_suit() == "clubs":
                clubs_list.append(card.get_card_name())
            elif card.get_suit() == "hearts":
                hearts_list.append(card.get_card_name())
            elif card.get_suit() == "diamonds":
                diamonds_list.append(card.get_card_name())
        #testprint
        #print("all suits nested list in caller_force_choose = " + str(all_suits_nested_list))
        #print("individual lists in caller_force_choose =" + str(clubs_list) + str(spades_list) + str(diamonds_list) + str(hearts_list))
        strongcard_suit_list = None
        longcard_suit_list = None
        longcard_suit_list_length = 3
        suits_2_or_more = []
        for list in all_suits_nested_list:
            #testprint
            #print("list = " + str(list))
            if "jack" in list and ("jack_lft" in list or "ace" in list or "king" in list or "queen" in list):
                strongcard_suit_list = list
            elif "jack_lft" in list and "ace" in list:
                strong_card_suit_list = list
            if len(list) > longcard_suit_list_length:
                longcard_suit_list_length, longcard_suit_list = len(list), list
            if len(list) >= 3:
                suits_2_or_more.append(list)
        #testprint
        #print("all below in caller force choose")
        #print("strongcard suit list = " + str(strongcard_suit_list))
        #print("longcard_suit_list = " + str(longcard_suit_list))
        #print("longcard_suit_list_length =" + str(longcard_suit_list_length))
        #print("suits_2_or_more = " + str(suits_2_or_more))
        if longcard_suit_list_length >= 4:
            #print("longcard_suit_list_length >= 4")
            called_suit = longcard_suit_list[0]
        else:
            #testprint (all throughout here)
            if strongcard_suit_list:
                #print("strongcard suit list found")
                if longcard_suit_list_length == 4:
                    #print("longcard suit list length == 4")
                    if len([i for i in long_card_suit_list if i in ["jack_lft", "jack", "ace"]]) == 0:
                        #print("len([i for i in long_card_suit_list if i in [\"jack_lft\", \"jack\", \"ace\"]]) == 0")
                        called_suit == strongcard_suit_list[0]
                    else:
                        if longcard_suit_list:
                            called_suit = longcard_suit_list[0]
                else:
                    called_suit = strongcard_suit_list[0]
            elif longcard_suit_list_length >= 4:
                #print("longcard_suit_list_length == 4")
                called_suit = longcard_suit_list[0]
            elif longcard_suit_list_length <= 3:
                #print("longcard_suit_list_length <= 3")
                if len(suits_2_or_more) == 1:
                    #print("len(suits_2_or_more) == 1")
                    called_suit = (suits_2_or_more[0])[0]
                elif len(suits_2_or_more) == 2:
                    #print("len(suits_2_or_more) == 2")
                    max_strength = 0
                    max_suit = ""
                    card_strength_dict = {"9":9, "10":10, "queen":11, "king":12, "ace":13, "jack_lft":14, "jack":15}
                    for list in suits_2_or_more:
                        list_strength = 0
                        for card in list[1:]:
                            #print("card in suits 2 or more loop = " + str(card))
                            list_strength += card_strength_dict[card]
                        if list_strength > max_strength:
                            max_strength, max_suit = list_strength, list[0]
                        #print("max strength, max_suit = " + str(max_strength) + str(max_suit))
                    called_suit = max_suit 
                    #print("ending call_suit = " + str(called_suit))
        return called_suit
    
    def first_chooser_card_choice(self, i, player_deck):
        player = game_1.player_order[i]
        #testprint
        #print("started going through first chooser card choice")
        #print("first chooser card choice variables ; trump_suit, player_deck: " + str(trump_suit) + " " + str(player_deck))
        trump_suit_cards, offtrump_card_names, offtrump_card_suites = [], [], []
        card_values = []
        left_bower = Euchre.left_bowers[game_1.trump_suit]
        for card in player_deck:
            if card == left_bower:
                trump_suit_cards.append("jack_lft")
            if card.get_suit() == game_1.trump_suit:
                trump_suit_cards.append(card.get_card_name())
            else:
                offtrump_card_names.append(card.get_card_name())
                offtrump_card_suites.append(card.get_suit())
        card_values = [Euchre.card_values_nontrump[card] for card in offtrump_card_names] if offtrump_card_names else \
        [Euchre.card_values_trump[card] for card in trump_suit_cards]
        max_card_index = card_values.index(max(card_values))
        card_to_play_name = offtrump_card_names[max_card_index] if offtrump_card_names else trump_suit_cards[max_card_index]
        card_to_play_suit = offtrump_card_suites[max_card_index] if offtrump_card_names else (trump_suit_pairs[game_1.trump_suit]\
                        if card_to_play_name == "jack_lft" else game_1.trump_suit)
        if card_to_play_name == "jack_lft":
            card_to_play_name = "jack"
        card_to_play = None
        for card in player_deck:
            if card.get_card_name() == card_to_play_name and card.get_suit() == card_to_play_suit:
                card_to_play = card
        #testprint
        #print("card_to_play in first_chooser_card_choice in AI = " + str(card_to_play))
        
        game_1.laid_down.append(card_to_play)
        game_1.round_players.append(game_1.player_order[i])
        self.card_play_lf = LabelFrame(window, text = player.name)
        self.card_play_lf.grid(column = 5 + i, row = 2)
        self.card_play_label = Label(self.card_play_lf, image = card_to_play.get_small_pic())
        self.card_play_label.grid(column = 0, row = 0)
        game_1.deck_order[i].remove(card_to_play)
        game_1.euchre_trick(i = i+1)
        
            
    def card_choice_question(self, i, player_deck):
        if i == 0:
            self.first_chooser_card_choice(i, player_deck)
        else:
            self.normal_card_choice_question(i, player_deck)
    
    def normal_card_choice_question(self, i, player_deck):
        player = game_1.player_order[i]
        #testprint
        #print("player_deck_c in card_choice_questions AI = " + str(player_deck))
        led_suit = (game_1.laid_down[0]).get_suit()
        current_winning_card = None
        current_winning_player = None
        led_suit_in_hand = []
        trump_suit_in_hand = []
        other_suits_in_hand_suits = []
        other_suits_in_hand_card = []
        choosing_deck = None
        choosing_deck_values = []
        card_to_play_index = None
        
        left_bower = Euchre.left_bowers[game_1.trump_suit]
        current_winner_index = game_1.determine_highest(game_1.laid_down)
        current_winning_player = Euchre.players[current_winner_index]
        current_winning_card = game_1.laid_down[current_winner_index]
        for card in player_deck:
            if card.get_suit() == led_suit and card != left_bower:
                led_suit_in_hand.append(card.get_card_name()) 
            if card.get_suit() == game_1.trump_suit:
                trump_suit_in_hand.append(card.get_card_name())
            elif card == left_bower:
                trump_suit_in_hand.append("jack_lft")
            elif card.get_suit() != led_suit and card.get_suit() != game_1.trump_suit:
                other_suits_in_hand_suits.append(card.get_suit())
                other_suits_in_hand_card.append(card.get_card_name())
        
        if led_suit_in_hand:
            #testprint
            #print("made it to led suit in hand")
            choosing_deck = led_suit_in_hand
            choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
            if Euchre.player_opposites[player] in game_1.round_players and current_winning_player == Euchre.player_opposites[player]:
                card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                #testprint
                #testprint
                min_choosing_deck = min(choosing_deck_values)
                #print("min choosing deck = " + str(min_choosing_deck))
                #supp_ctpi = choosing_deck_values.index(min_choosing_deck)
                #print("supp_ctpi = " + str(supp_ctpi))
                #print("1, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                    # "\n" + str(card_to_play_index))
            else:
                potential_laid_down = game_1.laid_down.copy()
                highest_card_index = choosing_deck_values.index(max(choosing_deck_values))
                potential_card = None
                if choosing_deck[highest_card_index] == "jack_lft":
                    for card in player_deck:
                        if card == left_bower:
                            potential_card = card
                for card in player_deck:
                    if card.get_card_name() == choosing_deck[highest_card_index] and card.get_suit == led_suit:
                        potential_card = card
                potential_laid_down.append(potential_card)
                potential_winner_index = game_1.determine_highest(game_1.laid_down)
                if game_1.laid_down[potential_winner_index] == potential_card:
                    card_to_play_index = highest_card_index
                    #testprint
                    #min_choosing_deck = max(choosing_deck_values)
                    #print("min choosing deck = " + str(min_choosing_deck))
                    #print("2, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                        # "\n" + str(card_to_play_index))
            
                else:
                    card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                    #testprint
                    min_choosing_deck = min(choosing_deck_values)
                    #print("min choosing deck = " + str(min_choosing_deck))
                    #print("3, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                        # "\n" + str(card_to_play_index))
                
                potential_laid_down.remove(potential_card)
                    
        elif len(trump_suit_in_hand) >= 1:
            choosing_deck = trump_suit_in_hand
            choosing_deck_values = [Euchre.card_values_trump[card] for card in choosing_deck]
            if current_winning_player == Euchre.player_opposites[player]:
                if i == (len(player_order) - 1):
                    if other_suits_in_hand_card:
                        choosing_deck = other_suits_in_hand_card
                        choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
                        card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                        #testprint
                        #print("4, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                           #  "\n" + str(card_to_play_index))
                    else:
                        card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                        #testprint
                        #print("5, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                           #  "\n" + str(card_to_play_index))
                else:
                    potential_laid_down = game_1.laid_down.copy()
                    highest_card_index = choosing_deck_values.index(max(choosing_deck_values))
                    potential_card = None
                    if choosing_deck[highest_card_index] == "jack_lft":
                        for card in player_deck:
                            if card == left_bower:
                                potential_card = card
                    for card in player_deck:
                        if card.get_card_name() == choosing_deck[highest_card_index] and card.get_suit == game_1.trump_suit:
                            potential_card = card
                    potential_laid_down.append(potential_card)
                    potential_winner_index = game_1.determine_highest(game_1.laid_down)
                    if potential_laid_down[potential_winner_index] == potential_card:
                        card_to_play_index = highest_card_index

                        #testprint
                        #print("6, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                          #   "\n" + str(card_to_play_index))
                    else:
                        card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                        #testprint
                        #print("7, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                          #   "\n" + str(card_to_play_index))
                    potential_laid_down.remove(potential_card)
            else:
                potential_laid_down = game_1.laid_down.copy()
                highest_card_index = choosing_deck_values.index(max(choosing_deck_values))
                potential_card = None
                if choosing_deck[highest_card_index] == "jack_lft":
                    for card in player_deck:
                        if card == left_bower:
                            potential_card = card
                for card in player_deck:
                    if card.get_card_name() == choosing_deck[highest_card_index] and card.get_suit == game_1.trump_suit:
                        potential_card = card
                potential_laid_down.append(potential_card)
                potential_winner_index = game_1.determine_highest(game_1.laid_down)
                if potential_laid_down[potential_winner_index] == potential_card:
                    card_to_play_index = highest_card_index
                else:
                    card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                    #testprint
                    #print("9, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                     #    "\n" + str(card_to_play_index))
                potential_laid_down.remove(potential_card)

        
        else:
            choosing_deck = other_suits_in_hand_card
            #testprint
            #print("other_suits_in_hand_card = " + str(other_suits_in_hand_card))
            choosing_deck_values = choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
            card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
            #testprint
            #print("10, choosing deck, choosing deck_values, card_to_play_index = \n" + str(choosing_deck) + "\n" + str(choosing_deck_values) + 
                # "\n" + str(card_to_play_index))
            
        #print("other_suits_in_hand_suits "  + str(other_suits_in_hand_suits))

        card_to_play_card = choosing_deck[card_to_play_index]
        card_to_play_suit = None
        if card_to_play_card == "jack_lft":
            card_to_play_suit = Euchre.trump_suit_pairs[game_1.trump_suit]
            card_to_play_card = "jack"
        else: 
            card_to_play_suit = game_1.trump_suit if choosing_deck == trump_suit_in_hand else \
                               (led_suit if choosing_deck == led_suit_in_hand else other_suits_in_hand_suits[card_to_play_index])
        card_to_play_total = None
        for card in player_deck:
            if card.get_suit() == card_to_play_suit and card.get_card_name() == card_to_play_card:
                card_to_play_total = card
        #testprint
        #print("card to play total form card_choice_question function in AI" + str(card_to_play_total))
        
        game_1.laid_down.append(card_to_play_total)
        game_1.round_players.append(game_1.player_order[i])
        self.card_play_lf = LabelFrame(window, text = player.name)
        self.card_play_lf.grid(column = 5 + i, row = 2)
        self.card_play_label = Label(self.card_play_lf, image = card_to_play_total.get_small_pic())
        self.card_play_label.grid(column = 0, row = 0)
        game_1.deck_order[i].remove(card_to_play_total)
        game_1.euchre_trick(i = i+1)
        
        
game_1 = Euchre()
game_1.play_euchre()



window.mainloop()

