import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


#_______________________________________________________________________________________________________________________________________________________________________________

#PLEASE NOTE:

#This is the first full coding project that I ever did, so it is not well organized! I have learned a lot about Object Oriented Programming since making this project, and 
#would definitely organize it differently if I was re-making this project now. 

#_______________________________________________________________________________________________________________________________________________________________________________

class Window(Tk):		
    def __init__(self):
        super(Window, self).__init__()
        self.title("Euchre")
        self._geom='200x200+0+0'
        self.geometry("{0}x{1}+0+0".format(
            self.winfo_screenwidth(), self.winfo_screenheight()))   
    
        
    def titleframe_encase(self):
        self.enter_name = ttk.LabelFrame(self)  
        self.enter_name.place(relx = .39, rely = .39)
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
    
    def empty_column_label(self, column = 0, row = 0, num_column_spaces = 1):
        num_column_labels_list = list(range(num_column_spaces))
        for i in num_column_labels_list:
            column_label = Label(window, text = "                    ").grid(column = column + i, row = row)
          
    def done_entering_names_command(self):
        self.player_name = self.player_name.get()
        self.delete_window_widgets()   
        self.tell_teams = ttk.LabelFrame(self)  
        self.tell_teams.place(relx = .41, rely = .39)
        labelFont = ("arial", 17, "bold")
        entered_teams_label = ttk.Label(self.tell_teams, text = "The teams are:\n\nTeam 1 = {} and AI 3\nTeam 2 = AI 2 and AI 4\n".format(self.player_name))
        entered_teams_label.configure(font = labelFont)
        entered_teams_label.grid(column = 0, row = 0, sticky = W)
        begin_game_button =  Button(self.tell_teams, text = "Begin Game", command = lambda:[self.delete_window_widgets(), game_1.euchre_greeting_2()])
        begin_game_button.grid(column = 0 , row = 1, sticky = N)
    
        


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
        self.team_2_score = 0
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
        suit_led = (cards_played_in_order[0]).get_suit()
        on_trump_card_values = {"9":9, "10":10, "queen":11, "king":12, "ace": 13, "jack_lft": 14, "jack": 15}
        led_card_values = {"9":9, "10":10, "jack":11, "queen":12, "king":13, "ace":14}

        card_suits = []
        card_names = []
        for card in cards_played_in_order:
            if card.get_card_name() == "jack" and card.get_suit() == Euchre.trump_suit_pairs[self.trump_suit]:
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

        return max_index
    
    def show_trump(self):
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
            trump_pic = spades_icon
        elif self.trump_info_list[2] == "clubs":
            trump_pic = clubs_icon
        elif self.trump_info_list[2] == "diamonds":
            trump_pic = diamonds_icon
        else:
            trump_pic = hearts_icon
        
        self.trump_suit_pic = Label(central_labelframe, image = trump_pic)
        self.trump_suit_pic.image = trump_pic
        self.trump_suit_pic.grid(column = 0, row = 1)
        
        picked_up_or_called = None
        player_called = self.trump_info_list[1]
        picked_up_or_called = "Called for pickup" if self.trump_info_list[0] == "yes" else "Called"
        
        self.now_beginning_label = ttk.Label(central_labelframe, text = "\n{0} by {1}".format(picked_up_or_called, player_called.name))
        self.now_beginning_label.configure(font = labelFont)
        self.now_beginning_label.grid(column = 0, row = 2)
        
        if self.trump_info_list[3] != "no":
            loner_label = ttk.Label(central_labelframe, text = "\n{} has decided to go alone".format(self.trump_info_list[3].name))
            loner_label.configure(font = labelFont)
            loner_label.grid(column = 0, row = 3)
        empty_label = Label(central_labelframe, text = "")
        empty_label.grid(column = 0, row = 4)
        begin_hand_button =  Button(central_labelframe, text = "    Next    ", command = lambda: self.euchre_round_set_vars())
        begin_hand_button.grid(column = 0, row = 5, sticky = N)
      
    def euchre_round_set_vars(self):
    
        window.delete_window_widgets()

        self.dealer_pickup_yn, self.player_picked_up, self.trump_suit, self.loner_player = self.trump_info_list[0], self.trump_info_list[1], \
        self.trump_info_list[2], self.trump_info_list[3]
        self.team_picked_up = self.team_1 if self.player_picked_up in self.team_1 else self.team_2
        self.team_1_hands_won, self.team_2_hands_won = 0, 0
        self.total_hands = (self.team_1_hands_won + self.team_2_hands_won)
        self.winning_player = "" 
        
        self.human_player_index = self.player_order.index(self.human_player)
        self.euchre_round_set_scene_pt_1()
    
    def euchre_round_set_scene_pt_1(self):
        
        spades_icon_small = ImageTk.PhotoImage(Image.open("spades_pic_small.jpg"))
        clubs_icon_small = ImageTk.PhotoImage(Image.open("clubs_image_small.png"))
        diamonds_icon_small = ImageTk.PhotoImage(Image.open("diamonds_image_small.png"))
        hearts_icon_small = ImageTk.PhotoImage(Image.open("hearts_image_small.jpg"))
        
        trump_image_dict = {"spades": spades_icon_small, "clubs": clubs_icon_small, "diamonds": diamonds_icon_small, "hearts": hearts_icon_small}
        self.empty_label = Label(window, text = "      \n\n\n\n")
        self.empty_label.grid(column =0, row = 0)
        
        cards_played_label = Label(window, text = "Cards played:\n")
        labelFont = ("arial", 14, "bold")
        cards_played_label.configure(font = labelFont)
        cards_played_label.place(relx = .4, rely = .05)
        
        empty_row_for_pbw = Label(window, text = "               ")
        empty_row_for_pbw.grid(column = 0, row = 1)
        AI_1_labelframe = LabelFrame(window, text = "AI 1")
        AI_1_labelframe.place(relx = 0, rely = .15)
        AI_1_icon = ttk.Label(AI_1_labelframe, image = Euchre.players[1].get_pic())
        AI_1_icon.grid(column = 0, row = 0)
        
        empty_label_2 = Label(window, text = "     ")
        empty_label_2.grid(column = 0 ,row = 3)
        
        AI_2_labelframe = LabelFrame(window, text = "AI 2")
        AI_2_labelframe.place(relx = 0, rely = .395)
        AI_2_icon = Label(AI_2_labelframe, image = Euchre.players[2].get_pic())
        AI_2_icon.grid(column = 0, row = 0)
        
        AI_3_labelframe = LabelFrame(window, text = "AI 3")
        AI_3_labelframe.place(relx = 0, rely = .64)
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
        t2_players_label.grid(column = 0, row = 3, sticky = W)
        team_picked_up_string = "Team 1" if self.team_picked_up == Euchre.team_1 else "Team 2"
        call_or_pickup_string = "Called" if self.dealer_pickup_yn == "no" else "Called for \npick-up"
        team_picked_up_label = Label(self.round_info_labelframe, text = "{0} by".format(call_or_pickup_string), borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_picked_up_label.grid(column =0, row = 4, sticky = E+W)
        team_picked_up_info_label = Label(self.round_info_labelframe, text = "{0}".format(self.player_picked_up.name))
        team_picked_up_info_label.grid(column =0, row = 5, sticky = W)
        dealer_label = Label(self.round_info_labelframe, text = "Dealer", borderwidth=2, relief="groove", fg = "white", bg = "black")
        dealer_label.grid(column =0, row = 6, sticky = E+W)
        dealer_info_label = Label(self.round_info_labelframe, text = self.dealer.name)
        dealer_info_label.grid(column =0, row = 7, sticky = W)
        current_trump_header= Label(self.round_info_labelframe, text = "Trump Suit", borderwidth=2, relief="groove", fg = "white", bg = "black")
        current_trump_header.grid(column =0, row = 8, sticky = E+W)
        current_trump_label = Label(self.round_info_labelframe, image = trump_image_dict[self.trump_suit])
        current_trump_label.image = trump_image_dict[self.trump_suit]
        current_trump_label.grid(column =0, row = 9, sticky = W)
        if self.loner_player != "no":
            team_1_label = Label(self.round_info_labelframe, text = "Loner Player", borderwidth=2, relief="groove", fg = "white", bg = "black")
            team_1_label.grid(column =0, row = 10, sticky = E+W)
            t1_players_label = Label(self.round_info_labelframe, text = self.loner_player.name)
            t1_players_label.grid(column =0, row = 11, sticky = W)
            
        
        team_points_labelframe = LabelFrame(window)
        team_points_labelframe.place(relx = .9, rely = .62)
        team_1_pt_label = Label(team_points_labelframe, text = " Team 1 Points ", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_1_pt_label.grid(column =0, row = 0, sticky = E+W)
        t1_pts_label = Label(team_points_labelframe, text = "{}".format(self.team_1_score))
        t1_pts_label.grid(column =0, row = 1, sticky = W)
        team_2_pt_label = Label(team_points_labelframe, text = " Team 2 Points ", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_2_pt_label.grid(column =0, row = 2, sticky = E+W)
        t1_pts_label = Label(team_points_labelframe, text = "{}".format(self.team_2_score))
        t1_pts_label.grid(column =0, row = 3, sticky = W)
            
        
        window.empty_column_label(column = 1, num_column_spaces = 3)
        
        self.euchre_round_set_scene_pt_2()
        window.update()
        self.euchre_full_hand()
    
    def euchre_round_set_scene_pt_2(self):
        self.human_player.card_play_lf, self.human_player.card_play_label, Euchre.Player_2.card_play_lf, Euchre.Player_2.card_play_label, Euchre.Player_3.card_play_lf, Euchre.Player_3.card_play_label, \
                                        Euchre.Player_4.card_play_lf, Euchre.Player_4.card_play_label = None, None, None, None, None, None, None, None
        counter = 5
        self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5 = Button(window), Button(window), Button(window), Button(window), Button(window)
        self.buttons_list = [self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5]
        if self.loner_player == Euchre.Player_3:
            self.buttons_list = self.buttons_list
        else:
            self.buttons_list = self.buttons_list[:((len(self.buttons_list)) - self.total_hands)]
        self.tell_hand_label = Label(text = "The cards in your hand are: \n")
        self.tell_hand_label.place(relx = .4, rely = .55)
        counter2 = 0
        for item in Euchre.deck_order_standard[0]:
            n = Euchre.deck_order_standard[0].index(item)
            card_picture = item.get_pic()
            self.buttons_list[n].configure(image = card_picture, state = "disabled", command = lambda n = n: Euchre.players[0].human_card_choice_check(n))
            self.buttons_list[n].place(relx = (.2 + (counter2*.095)), rely = .6)
            counter2 += 1
        text_font = ("arial", 12, "bold")
        self.team_tricks_won_label = Label(window, text = "\nTeam 1 tricks won: {0}                      Team 2 tricks won: {1}".format(self.team_1_hands_won, self.team_2_hands_won))
        self.team_tricks_won_label.configure(font = text_font)
        self.team_tricks_won_label.place(relx = .32, rely = .87)
        
    def euchre_trick(self, i = 0):

        if i > len(self.player_order)-1:
            self.show_highest()
        else:
            player = self.player_order[i]
            player_deck = self.deck_order[i]
            player.card_choice_question(i, player_deck)
        
    
    def show_highest(self):
        max_index = self.determine_highest(self.laid_down)
        max_card = self.laid_down[max_index]
        self.winning_player = self.player_order[max_index]
        
        window.update()
        window.after(1000)
        self.tell_hand_label.place_forget()
        for b in self.buttons_list:
            b.place_forget()

        self.winner_label = Label(window, text = "{} won the trick with the: \n".format(self.winning_player.name))
        labelFont = ("arial", 14, "bold")
        self.winner_label.configure(font = labelFont)
        self.winner_label.place(relx = .365, rely = .55)
        self.winning_card_label = Label(window, image = max_card.get_pic())
        self.winning_card_label.place(relx = .40, rely = .62)
        window.update()
        if self.winning_player in self.team_1:
            self.team_1_hands_won += 1
        else:
            self.team_2_hands_won += 1
        self.total_hands = self.team_1_hands_won + self.team_2_hands_won
        self.team_tricks_won_label.configure(text = "\nTeam 1 tricks won: {0}                      Team 2 tricks won: {1}".format(self.team_1_hands_won, self.team_2_hands_won))
        window.update()
        
        self.next_trick_button = Button(window, text = "Continue to next trick", command = self.clear_for_next_trick)
        self.next_trick_button.place(relx = .4, rely = .45)
        
    
    def clear_for_next_trick(self):
        self.laid_down = []
        self.round_players = []
        self.next_trick_button.destroy()
        self.winner_label.destroy()
        self.winning_card_label.destroy()
        
        cards_played_pic_list = [self.human_player.card_play_lf, self.human_player.card_play_label, Euchre.Player_2.card_play_lf, Euchre.Player_2.card_play_label, Euchre.Player_3.card_play_lf, Euchre.Player_3.card_play_label, \
                                        Euchre.Player_4.card_play_lf, Euchre.Player_4.card_play_label]
        for i in cards_played_pic_list:
            if i != None:
                i.destroy()
        
        self.euchre_full_hand()

    def euchre_full_hand(self, i = 0):
        self.player_order, self.deck_order = None, None
        if self.total_hands == 5:
            self.hand_winner_announcement()
        else:
            if self.total_hands >=1:
                self.euchre_round_set_scene_pt_2()
            self.set_starting_player()
            self.laid_down = []
            self.round_players = []
            self.euchre_trick()
    
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

    def round_winner_points(self):
        winning_team, hands_won = "", 0
        points_awarded = 0
        if self.team_1_hands_won > self.team_2_hands_won:
            winning_team, hands_won = Euchre.team_1, self.team_1_hands_won
        else:
            winning_team, hands_won = Euchre.team_2, self.team_2_hands_won
        if winning_team == self.team_picked_up and hands_won == 5:
            if self.loner_player != "no" and self.loner_player in self.team_picked_up:
                points_awarded = 4
            else:
                points_awarded = 2
        elif winning_team == self.team_picked_up and hands_won < 5:
            points_awarded = 1
        else:
            points_awarded = 2
        return winning_team, points_awarded
        
    def hand_winner_announcement(self):
        window.delete_window_widgets()
        winning_team, points_awarded = self.round_winner_points()
        winning_team_string = None
        if winning_team == Euchre.team_1:
            self.team_1_score += points_awarded
            winning_team_string = "Your Team"
        elif winning_team == Euchre.team_2:
            self.team_2_score += points_awarded
            winning_team_string = "The other team"
        hand_winner_frame = LabelFrame(window)
        hand_winner_frame.place(relx = .33, rely = .34)
        label_text = ("arial", 16, "bold")
        hand_winner_label = ttk.Label(hand_winner_frame, text = "\n\n{} won the hand for {} points\n\n".format(winning_team_string, points_awarded))
        hand_winner_label.configure(font = label_text)
        hand_winner_label.grid(column = 0, row = 0)
        self.clear_hand_info()
        
        self.next_trick_button = Button(window, text = "Continue to next hand", command = self.next_round_determination)
        self.next_trick_button.place(relx = .405, rely = .55)
        
    
    def clear_hand_info(self):
        self.trump_info_list = None
        self.dealer_pickup_yn, self.player_picked_up, self.trump_suit, self.loner_player = None, None, None, None
        self.team_picked_up = None
        self.team_1_hands_won, self.team_2_hands_won = 0, 0
        self.total_hands = (self.team_1_hands_won + self.team_2_hands_won)
        self.winning_player = "" 
        laid_down = []
        round_players = []
        
    def next_round_determination(self):
        window.delete_window_widgets()
        if self.team_1_score >= 10 or self.team_2_score >= 10:
            self.winner_announcement()
        else:
            self.euchre_shuffle()
            
    
    def winner_announcement(self):
        game_winner_frame = LabelFrame(window)
        game_winner_frame.place(relx = .32, rely = .34)
        label_text = ("arial", 24, "bold")
        
        if self.team_1_score >= 10:
            game_winner_label = ttk.Label(game_winner_frame, text = "\n\nCongratulations, you won the game!\n\n\n")
        else:
            game_winner_label = ttk.Label(game_winner_frame, text = "\n\nBummer, the other team won the game :(\n                Better luck next time!\n\n")
        game_winner_label.configure(font = label_text)
        game_winner_label.grid(column = 0, row = 0)
        
        game_1.counter = 0
        self.team_1_score = 0
        self.team_2_score = 0
        
        self.next_trick_button = Button(game_winner_frame, text = "Play again", command = lambda: [window.delete_window_widgets(), window.titleframe_encase()])
        self.next_trick_button.grid(column = 0, row = 0, sticky = N)

    def play_euchre(self):
        window.titleframe_encase()
        
    def euchre_shuffle(self):
        Euchre.true_decks, Euchre.leftover_deck = self.deal_deck(4, 4, 0)
        Euchre.deck_order_standard = Euchre.true_decks
        Euchre.player_1_deck, Euchre.player_2_deck, Euchre.player_3_deck, Euchre.player_4_deck = Euchre.deck_order_standard[0], Euchre.deck_order_standard[1], \
        Euchre.deck_order_standard[2], Euchre.deck_order_standard[3]
        Euchre.trump_suit_card = self.set_trump(Euchre.leftover_deck)
        
        self.set_dealer()
    
    def set_dealer(self):
        set_dealer_frame = LabelFrame(window)
        set_dealer_frame.place(relx = .32, rely = .39)
        label_text = ("arial", 16, "bold")
        self.counter += 1
        if self.counter == 1:
            self.dealer = Euchre.Player_1
        else:
            self.dealer = Euchre.players[0] if self.dealer == Euchre.players[3] else Euchre.players[self.dealer_index+1]
        round_number = [None, "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", \
                            "15th", "16th", "17th", "18th", "19th"]
        if self.dealer != self.human_player:
            dealing_label = ttk.Label(set_dealer_frame, text = "We are now beginning the {0} round of Euchre.\n\n\n {1} is dealing the cards...".format(round_number[self.counter], self.dealer.name))
        else: 
            dealing_label = ttk.Label(set_dealer_frame, text = "We are now beginning the {0} round of Euchre.\n\n\n You are dealing the cards...".format(round_number[self.counter]))
        dealing_label.configure(font = label_text)
        dealing_label.grid(column = 0, row = 0)
        self.dealer_index = Euchre.players.index(self.dealer)
        empty_label = Label(set_dealer_frame, text = "")
        empty_label.grid(column = 0, row = 1)
        next_button = Button(set_dealer_frame, text = "    Next    ", command = lambda: [window.delete_window_widgets(), self.set_orders()])
        next_button.grid(column = 0 , row =2, sticky = N)

    def set_orders(self):
        self.trump_suit, self.trump_card = Euchre.trump_suit_card.get_suit(), Euchre.trump_suit_card.get_card_name()
        if self.dealer_index == 4:
                first_caller = (Euchre.players[0]).name
        else:
            first_caller = Euchre.Player_1 if self.dealer == Euchre.Player_4 else Euchre.players[(self.dealer_index+1)]
        self.player_order, self.deck_order = self.euchre_player_order(first_caller)
        trump_info_list = self.pick_up_scene()     

    
    def space_label(self, column, row, num_space_labels = 1):
        num_space_labels_list = list(range(num_space_labels))
        for i in num_space_labels_list:
            space_label = Label(window, text = "               ").grid(column = column, row = row+i)
        

    def pick_up_scene(self):
        window.delete_window_widgets()
        self.human_player_index = self.player_order.index(self.human_player)
        label_font = ("arial", 14, "bold")
        game_1.instructions_label =  Label(window, text = "The other players are deciding if they will call for pick up")
        game_1.instructions_label.configure(font = label_font)
        game_1.instructions_label.place(relx=.18, rely=.8)
        self.empty_label = Label(window, text = "                                                      \n\n")
        self.empty_label.grid(column =0, row = 0)
        Card_game.tell_hand(self, self.deck_order[self.human_player_index], player = game_1.human_player)     
        self.pick_up_button = ttk.Button(window, text = "Pick up", state = "disabled", command = lambda: self.human_player.pick_up_decision(self.human_player_index, "no"))
        self.pick_up_button.grid(column = 2, row = 5)
        self.loner_button = ttk.Button(window, text = "Pick up and Go Alone", state = "disabled", command = lambda: self.human_player.pick_up_decision(self.human_player_index, self.human_player))
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
                if person == self.dealer:
                   self.dealer_labelframe = LabelFrame(window, text = "Dealer", fg = "red")
                   self.dealer_labelframe.grid(column = column_counter, row = 6)
                   player_pass_pickup_icon = Label(self.dealer_labelframe, image = person.get_pic()).grid(column = 0, row = 0)
                else:
                    player_pass_pickup_icon = Label(window, image = person.get_pic()).grid(column = column_counter, row = 6)
                if person.name == "AI 3":
                   player_pass_pickup_name = Label(window, text = "  " + str(person.name) + "\n(Teammate)", fg = "blue").grid(column=column_counter, row = 7)
                else:
                    player_pass_pickup_name = Label(window, text = person.name).grid(column=column_counter, row = 7)

                n = self.player_order.index(person)
                self.player_response_label_list[n].grid(column=column_counter, row = 8)
                column_counter += 1
        
        missing_AI_name = None
        if self.player_order[0] != self.human_player:
            missing_AI_name = self.player_order[0].name
        else:
            missing_AI_name = self.player_order[1].name
            
        if missing_AI_name == "AI 3":
           missing_AI_name =  "  " + str(missing_AI_name) + "\n(Teammate)"
            
        missingAI_pass_pickup_name = Label(window, text = missing_AI_name)
        if missing_AI_name == "AI 3":
            missingAI_pass_pickup_name.configure(fg = "blue")
        missingAI_pass_pickup_name.grid(column= 2, row = 7)    
        window.empty_column_label(row = 7, num_column_spaces = 3)
        self.potential_trump_frame = ttk.LabelFrame(window, text = "Potential trump")
        self.potential_trump_frame.grid(column=8, row =6)
        self.potential_trump_label = ttk.Label(self.potential_trump_frame, image = Euchre.trump_suit_card.get_pic())
        self.potential_trump_label.grid(column = 0, row = 0, columnspan = 3)
        teams_dealer_labelframe = LabelFrame(window)
        teams_dealer_labelframe.place(relx = .9, rely = .15)
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
        
        team_points_labelframe = LabelFrame(window)
        team_points_labelframe.place(relx = .9, rely = .62)
        team_1_pt_label = Label(team_points_labelframe, text = " Your Team Points ", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_1_pt_label.grid(column =0, row = 0, sticky = E+W)
        t1_pts_label = Label(team_points_labelframe, text = "{}".format(self.team_1_score))
        t1_pts_label.grid(column =0, row = 1, sticky = W)
        team_2_pt_label = Label(team_points_labelframe, text = " AI Team Points ", borderwidth=2, relief="groove", fg = "white", bg = "black")
        team_2_pt_label.grid(column =0, row = 2, sticky = E+W)
        t1_pts_label = Label(team_points_labelframe, text = "{}".format(self.team_2_score))
        t1_pts_label.grid(column =0, row = 3, sticky = W)
        game_1.instructions_label.lift()
        missingAI_pass_pickup_name.lift()
        window.update()
        self.pick_up_decide()

    def pick_up_decide(self, i = 0):
        if i >= 4:
            self.call_it()
        else:
            window.update()
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
        label_font = ("arial", 14, "bold")
        player = self.player_order[i]
        self.instructions_label.destroy()
        Card_game.tell_hand(self, self.deck_order[self.human_player_index], player = game_1.human_player)     
        self.call_it_button = ttk.Button(window, text = "call a suit", state = "disabled", command = lambda: game_1.human_player.call_it_decision_1(self.human_player_index, "no"))
        self.call_it_button.grid(column = 2, row = 5)
        self.loner_button = ttk.Button(window, text = "call a suit \nAND go alone", state = "disabled", command = lambda: game_1.human_player.call_it_decision_1(self.human_player_index, "yes"))
        self.loner_button.grid(column = 3, row = 5)
        self.pass_button = ttk.Button(window, text = "Pass", state = "disabled", command = lambda: game_1.human_player.pass_decision_callround(self.human_player_index))
        self.pass_button.grid(column = 4, row = 5)
        self.instructions_label = Label(window, text = "Other players are deciding if they will call it")
        self.instructions_label.configure(font = label_font)
        self.instructions_label.place(relx = .18, rely = .8)
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
        if i>= 4:
            return
        player = self.player_order[i]
        player_deck = self.deck_order[i]
        player.pick_up_questions_2(i, self.trump_card, self.trump_suit, self.dealer, self.dealer_index, player, \
                                                         player_deck)  

        
    def renege_check(self, player_deck, card_choice_number):
        if game_1.laid_down and game_1.total_hands != 4:
            led_suit = (game_1.laid_down[0]).get_suit()
            case_deck = player_deck.copy()
            suits_in_hand = [card.get_suit() for card in case_deck]
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
        label_font = ("arial", 14, "bold")
        if game_1.human_player == dealer:
            game_1.instructions_label.configure(text = " You are the dealer. Will you pick it up?".format(player.name), fg = "blue")
        else:
            game_1.instructions_label.configure(text = " {}, will you tell the dealer to pick it up?".format(player.name), fg = "blue")
        game_1.instructions_label.lift()
        game_1.pick_up_button.configure(state = "normal")
        game_1.loner_button.configure(state = "normal")
        game_1.pass_button.configure(state = "normal")
        window.update()
    
    def pick_up_decision(self, i, loner_decision):
        game_1.instructions_label.destroy()
        game_1.trump_info_list = ["yes", game_1.player_order[i], game_1.trump_suit, loner_decision]
        if game_1.player_order[i] == game_1.dealer:
            self.player_is_dealer(i, player_is_dealer = "yes")
        else:
            label_font = ("arial", 14, "bold")
            game_1.instructions_label = Label(window, text = "You have told {} to pick up trump.".format(game_1.dealer.name))
            game_1.instructions_label.configure(font = label_font, fg = "black")
            game_1.instructions_label.place(relx=.18, rely=(.8))
            game_1.pick_up_button.configure(state = "disabled")
            game_1.loner_button.configure(state = "disabled")
            game_1.pass_button.configure(state = "disabled")
            window.update()
            game_1.dealer_removal_assign()
    
    def pass_decision(self, i):
        game_1.instructions_label.destroy()
        game_1.pick_up_button.configure(state = "disabled")
        game_1.loner_button.configure(state = "disabled")
        game_1.pass_button.configure(state = "disabled")
        window.update()
        game_1.pick_up_decide(i = i+1)
    
    def player_is_dealer(self, i, player_is_dealer = "no"):
        player = game_1.dealer
        deck = Euchre.deck_order_standard[game_1.dealer_index]
        label_font = ("arial", 14, "bold")
        if player_is_dealer == "yes":
            game_1.instructions_label =  Label(window, text = "You are the dealer. Please click on the card from your hand that your would like to remove.")
            game_1.instructions_label.configure(font = label_font)
            game_1.instructions_label.place(relx=.18, rely=.8)
        else:
            game_1.instructions_label =  Label(window, text = "{} has told you to pick it up. Please click on the card from your hand that your would like to remove.".format(game_1.trump_info_list[1].name))
            game_1.instructions_label.configure(font = label_font)
            game_1.instructions_label.place(relx=.10, rely=.8)
        deletes_list = [game_1.pick_up_button, game_1.pass_button, game_1.loner_button]
        for item in deletes_list:
            item.destroy()
        for item in game_1.card_labels_list:
            if item:
                item.destroy()
        for item in game_1.player_response_label_list:
            item.destroy()
        #AI2_pass_pickup_name = Label(window, text = "AI 2").grid(column=2, row = 7)
        column, row = 0, 2
        counter = 1
        self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5 = Button(window), Button(window), Button(window), Button(window), Button(window)
        self.buttons_list = [self.clb_1, self.clb_2, self.clb_3, self.clb_4, self.clb_5]
        tell_hand_label = Label(text = "The cards in your hand are: \n").grid(column = column, row = row)
        for item in deck:
            n = deck.index(item)
            card_picture = item.get_pic()
            self.buttons_list[n].configure(image = card_picture, command = lambda n = n, counter = counter: self.dealer_removal_replace(n, counter))
            self.buttons_list[n].grid(column = counter, row = 4)
            counter += 1
        empty_row = Label(window, text= "")
        empty_row.grid(column = 4, row = 5)

    
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
        game_1.potential_trump_label.destroy()
        Euchre.deck_order_standard[game_1.dealer_index].pop(card_choice_index)
        Euchre.deck_order_standard[game_1.dealer_index].append(Euchre.trump_suit_card)
        window.after(1000, lambda: game_1.show_trump())
        
            

    def pick_up_questions_2(self, i, trump_card, trump_suit, dealer, dealer_index, player, player_deck):
        label_font = ("arial", 14, "bold")
        label_font = ("arial", 14, "bold")
        game_1.instructions_label.configure(text = "{}, would you like to call a suit as trump?\n\n".format(player.name), fg = "blue")
        game_1.instructions_label.configure(font = label_font)
        game_1.instructions_label.place(relx=.18, rely=(.8))
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
            call_spades_button = ttk.Button(window, text = "call spades", command = lambda: self.call_it_decision_2(i, game_1.human_player, "spades")).grid(column = 2, row = 5)
            call_clubs_button = ttk.Button(window, text = "call clubs", command = lambda: self.call_it_decision_2(i, game_1.human_player, "clubs")).grid(column = 3, row = 5)
            call_diamonds_button = ttk.Button(window, text = "call diamonds", command = lambda: self.call_it_decision_2(i, game_1.human_player, "diamonds")).grid(column = 4, row = 5)
            call_hearts_button = ttk.Button(window, text = "call hearts", command = lambda: self.call_it_decision_2(i, game_1.human_player, "hearts")).grid(column = 5, row = 5)
        else:
            call_spades_button = ttk.Button(window, text = "call spades", command = lambda: self.call_it_decision_2(i, "no", "spades")).grid(column = 2, row = 5)
            call_clubs_button = ttk.Button(window, text = "call clubs", command = lambda: self.call_it_decision_2(i, "no", "clubs")).grid(column = 3, row = 5)
            call_diamonds_button = ttk.Button(window, text = "call diamonds", command = lambda: self.call_it_decision_2(i, "no", "diamonds")).grid(column = 4, row = 5)
            call_hearts_button = ttk.Button(window, text = "call hearts", command = lambda: self.call_it_decision_2(i, "no", "hearts")).grid(column = 5, row = 5)

    
    def call_it_decision_2(self, i, loner_player, suit):
        game_1.instructions_label.destroy()
        window.update()
        game_1.trump_info_list = ["no", game_1.player_order[i], suit, loner_player]
        game_1.trump_suit = suit
        game_1.trump_card = None
        window.after(1000, lambda: game_1.show_trump())
        
    
    def pass_decision_callround(self, i):
        game_1.instructions_label.place_forget()
        game_1.call_it_decide(i = i+1)

            
    def card_choice_question(self, i, player_deck):
        if i != 0:
            window.after(1000)
        self.instructions_label = Label(window, text = "\nIt's your turn. Click on the card you would like to play")
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
        
        renege_pass_fail = game_1.renege_check(player_deck, n)
        if renege_pass_fail == "all clear":
            game_1.buttons_list[n].destroy()
            game_1.buttons_list.pop(n)
            
            
            for button in game_1.buttons_list:
                button.configure(state = "disabled")
                
            game_1.laid_down.append(card_choice)
            game_1.round_players.append(game_1.player_order[i])
            labelframe_text = "You" if game_1.human_player.name == "" else game_1.human_player.name
            self.card_play_lf = LabelFrame(window, text = labelframe_text)
            self.card_play_lf.place(relx = (.25 + (i * .09)), rely = .2)
            self.card_play_label = Label(self.card_play_lf, image = card_choice.get_small_pic())
            self.card_play_label.grid(column = 0, row = 0)
            game_1.deck_order[i].remove(card_choice)
            game_1.euchre_trick(i = i+1)
        else:
            self.renege_failed()
    
    def renege_failed(self):
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
        unique_offsuits_num = 0
        dec_num = random.random()
        dealer_on_team = "yes" if ((player in Euchre.team_1 and dealer in Euchre.team_1) or \
                                   (player in Euchre.team_2 and dealer in Euchre.team_2)) else "no"

        left_bower = Euchre.left_bowers[trump_suit]
        for card in player_deck_c:
            if card == left_bower:
                trumpst_card_names.append("jack_lft")
            elif card.get_suit() == trump_suit:
                trumpst_card_names.append(card.get_card_name())
            else:
                off_trump_suits.append(card.get_suit()) 
                if card.get_suit() not in off_trump_suits:
                    unique_offsuits_num += 1
                off_trump_card_names.append(card.get_card_name())
        if player == dealer:
            loner_player, pick_up_decision = AI.player_is_dealer(self, trumpst_card_names, dec_num, trump_card, off_trump_card_names)
        elif len(trumpst_card_names) == 4:
            loner_player, pick_up_decision = AI.four_cards_trump(self, trumpst_card_names, unique_offsuits_num, off_trump_card_names, dec_num)
        elif len(trumpst_card_names) == 3:
            loner_player, pick_up_decision = AI.three_cards_trump(self, trumpst_card_names, unique_offsuits_num, off_trump_card_names, \
                                                               dealer_on_team, trump_card, dec_num)
        elif len(trumpst_card_names) == 2:
            loner_player, pick_up_decision = AI.two_cards_trump(self, trumpst_card_names, unique_offsuits_num, off_trump_card_names, \
                                                               dealer_on_team, trump_card, dec_num)
        if pick_up_decision == "yes":
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
                label_font = ("arial", 14, "bold")
                if player == dealer:
                    game_1.instructions_label = Label(window, text = "{0} has picked up trump.".format(game_1.player_order[i].name, game_1.dealer.name))
                else:
                    game_1.instructions_label = Label(window, text = "{0} has told {1} to pick up trump.".format(game_1.player_order[i].name, game_1.dealer.name))
                game_1.instructions_label.configure(font = label_font)
                game_1.instructions_label.place(relx=.25, rely=(.8))
                game_1.dealer_removal_assign()
            
        else:
            self.pass_decision(i)
    
    def pass_decision(self, i):
        window.after(1000, game_1.player_response_label_list[i].configure(text = "pass"))
        window.update()
        game_1.pick_up_decide(i = i+1)
        
    def player_is_dealer(self, trumpst_card_names, dec_num, trump_card, offtrump_card_names):
        loner_player = "no"
        pick_up_decision = "no"
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        trumpst_card_names.append(trump_card)
        trump_cards_num = len(trumpst_card_names) if trumpst_card_names else None
        if trump_cards_num >= 5:
            comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["9" , "10"]])
            loner_player, pick_up_decision = ("yes", "yes") if comp_deck_ct_1 != 2 else ("no", "yes")
        elif trump_cards_num == 4:
            comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["9" , "10"]])
            loner_player, pick_up_decision = ("yes", "yes") if ((not comp_deck_ct_1 == 2) and ("ace" in offtrump_card_names)) else ("no", "yes")
        elif trump_cards_num == 3:
            comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["9", "10"]])
            comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["queen", "king"]])
            pick_up_decision = "yes" if comp_deck_ct_1 != 2 and comp_deck_ct_2 == 1 else ("yes" if dec_num <.15 else "no")
        elif trump_cards_num == 2:
            comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft"]])
            comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
            comp_deck_ct_3 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace", "king"]])
            comp_deck_ct_4 = len([i for i in trumpst_card_names if i in ["9", "10", "queen", "king"]])
            if (comp_deck_ct_1 == 2) or (comp_deck_ct_2 == 2 and dec_num < .75) or (comp_deck_ct_3 ==2 and dec_num < .33)\
                or (comp_deck_ct_4 == 1 and dec_num < .2) or (comp_deck_ct_2 == 1 and dec_num < .1):
                pick_up_decision = "yes"
            else:
                pick_up_decision = "no"
        return loner_player, pick_up_decision     
                
        
    def four_cards_trump(self, trumpst_card_names, unique_offsuits_num, off_trump_card_names, dec_num):
        loner_player = "no"
        pick_up_decision = "no"
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4 = 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
        comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["king", "queen"]])
        if "ace" in off_trump_card_names:
            comp_deck_ct_3 = 2
        elif "king" in off_trump_card_names:
            comp_deck_ct_3 = 1
        loner_player, pick_up_decision = ("yes", "yes") if (comp_deck_ct_1 == 3 and "ace" in off_trump_card_names) else ("no", "yes")
                
        return loner_player, pick_up_decision
        
        
    def three_cards_trump(self, trumpst_card_names, unique_offsuits_num, off_trump_card_names, dealer_on_team, trump_card, dec_num):
        loner_player = "no"
        pick_up_decision = "no"
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
        comp_deck_ct_2 = off_trump_card_names.count("ace")
        comp_deck_ct_3 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft"]])
        comp_deck_ct_4 = len([i for i in trumpst_card_names if i in ["9", "10", "queen"]])
        comp_deck_ct_5 = len([i for i in trumpst_card_names if i in ["9", "10"]])
        comp_deck_ct_6 = len([i for i in trumpst_card_names if i in ["king", "ace", "jack", "jack_lft"]])
        if (comp_deck_ct_1 == 3):
            loner_player, pick_up_decision = "no", "yes"
        elif comp_deck_ct_3 == 1:
            pick_up_decision = "yes"
        elif comp_deck_ct_1 == 2 and (comp_deck_ct_3 >= 2 or (comp_deck_ct_3 >=1 and comp_deck_ct_4>=1)):
            pick_up_decision = "yes" 
        elif comp_deck_ct_1 == 2:
            pick_up_decision = "yes"
        elif comp_deck_ct_4 == 3:
            loner_player, pick_up_decision = ("no", "yes") if (dealer_on_team == "yes") else (("no", "no") if (unique_offsuits_num != 1 and ("ace" not in off_trump_card_names)) else ("no", "no"))
        elif comp_deck_ct_5 == 2 and comp_deck_ct_6 >=1:
            if comp_deck_ct_3 >= 1 or comp_deck_ct_2 >= 1 or unique_offsuits_num == 1:
                pick_up_decision == "yes"
            loner_player, pick_up_decision = ("no", "yes") if dealer_on_team == "yes" else (("no", "no") if dec_num < .2 else ("no", "yes"))
        elif comp_deck_ct_6 >= 2:
            pick_up_decision == "yes"
        elif "jack_lft" in trumpst_card_names and dealer_on_team == "yes" and trump_card in ["jack", "ace"]:
            pick_up_decision = "yes" 
        else:
            loner_player, pick_up_decision = ("no", "yes") if dealer_on_team == "yes" else \
            (("no", "no") if ((trump_card == "jack" or trump_card == "jack_lft") and dec_num < .5) else \
            (("no", "yes") if dec_num < .85 else ("no", "no")))
        return loner_player, pick_up_decision
    
    
    def two_cards_trump(self, trumpst_card_names, unique_offsuits_num, off_trump_card_names, dealer_on_team, trump_card, dec_num):
        loner_player = "no"
        pick_up_decision = "no"
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft"]])
        comp_deck_ct_2 = len([i for i in trumpst_card_names if i in ["jack", "jack_lft", "ace"]])
        comp_deck_ct_3 = len([i for i in trumpst_card_names if i in ["9", "10"]])
        comp_deck_ct_4 = len([i for i in trumpst_card_names if i in ["jack", "king"]])
        
        
        if comp_deck_ct_1 == 2:
            pick_up_decision = "yes" 
        elif comp_deck_ct_2 == 2:
            if dealer_on_team == "yes":
                if unique_offsuits_num == 1 or "ace" in off_trump_card_names:
                    pick_up_decision = "yes"
                else:
                    pick_up_decision = "yes" if dec_num < .5 else "no"
            if dealer_on_team == "no":
                if unique_offsuits_num == 1 and "ace" in off_trump_card_names:
                    pick_up_decision = "yes" if dec_num < .3 else "no"
                else:
                    pick_up_decision = "yes" if (trump_card not in ["jack", "jack_lft"] and unique_offsuits_num != 3 and dec_num < .3) else "no"
        elif comp_deck_ct_3 == 2:
            if dealer_on_team == "yes" and trump_card == "jack":
                if unique_offsuits_num == 1 or "ace" in off_trump_card_names:
                    pick_up_decision = "yes"
                else:
                    pick_up_decision = "yes" if dec_num < .85 else "no"
            elif dealer_on_team == "yes" and trump_card in ["jack_lft", "ace"]:
                pick_up_decision = "yes" if dec_num < .15 else "no"
            else:
                pick_up_decision = "no"
        
        elif "jack_lft" in trumpst_card_names and dealer_on_team == "yes" and trump_card in ["jack", "ace"]:
            if dec_num < .9:
                pick_up_decision = "yes" 
                
        elif comp_deck_ct_4 == 2:
            if dealer_on_team == "yes":
                pick_up_decision = "yes"
            else:
                if unique_offsuits_num == 1:
                    pick_up_decision = "yes"
                elif unique_offsuits_num == 2:
                    if "ace" in off_trump_card_names:
                        pick_up_decision = "yes"
                    else:
                        pick_up_decision = "yes" if dec_num < .4 else "no"
                else:
                    if off_trump_card_names.count("ace") >= 2:
                        pick_up_decision = "yes"
                    elif "ace" in off_trump_card_names:
                        pick_up_decision = "yes" if dec_num < .4 else "no"
                    else:
                        pick_up_decision = "yes" if dec_num < .15 else "no"
                    
                    
                
        else:
            if dealer_on_team == "yes":
                if "jack" in trumpst_card_names:
                    if trump_card not in ["9", "10", "queen"]:
                        if dec_num < .65:
                            pick_up_decision = "yes"
                    else:
                        if comp_deck_ct_3 == 1:
                            if off_trump_card_names.count("ace") >= 2:
                                pick_up_decision = "yes"
                            elif unique_offsuits_num == 1:
                                pick_up_decision = "yes" if dec_num < .8 else "no"
                            elif unique_offsuits_num != 3 or off_trump_card_names.count("ace"):
                                pick_up_decision = "yes" if dec_num < .5 else "no"     
                            else:
                                pick_up_decision = "yes" if dec_num < .15 else "no"    
                        else:
                            pick_up_decision = "yes" if dec_num < .5 else "no" 
                            
                if trump_card == "jack":
                    pick_up_decision = "yes"
                if comp_deck_ct_2 == 1:
                    if comp_deck_ct_3 == 0:
                        pick_up_decision = "yes" if dec_num < .55 else "no"
                    else:
                        pick_up_decision = "yes" if dec_num < .2 else "no"
                else:
                    pick_up_decision = "no"
            if dealer_on_team == "no":
                    pick_up_decision = "no"    
        return loner_player, pick_up_decision
    
    def dealer_removal_choice(self, player_deck, trump_suit, trump_card, dealer_index):
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
        trump_list = trump_list_matchup[trump_suit]
        all_suits_nested_list.remove(trump_list)
        for list1 in all_suits_nested_list:
            if len(list1) <1:
                all_suits_nested_list.remove(list1)
        removal_list = None
        for list in all_suits_nested_list:
            if len(list) < 1:
                all_suits_nested_list.remove(list)
        if len(trump_list) == 6:
            removal_list = trump_list
        elif len(trump_list) == 5 or len(all_suits_nested_list) == 1:
            removal_list = all_suits_nested_list[0]
        elif len(trump_list) >= 2 and len(all_suits_nested_list) >= 2:
            shortest_suit = min(all_suits_nested_list, key=len)
            min_length = len(shortest_suit)
            min_card_value = 15
            min_card_list = None
            for list2 in all_suits_nested_list:
                if len(list2) == min_length:
                    for card in list2:
                        card_value = Euchre.card_values_nontrump[card.get_card_name()]
                        if card_value < min_card_value:
                            min_card_value = card_value
                            min_card_list = list2
            removal_list = min_card_list
            
            
        
        else:
            all_off_suits_list = []
            for item in all_suits_nested_list:
                for card in item:
                    all_off_suits_list.append(card)
            removal_list = all_off_suits_list
                
        removal_list_values = [Euchre.card_values_trump[card.get_card_name()] for card in removal_list] if removal_list == trump_list else \
                               [Euchre.card_values_nontrump[card.get_card_name()] for card in removal_list]
    
        removal_card_index = removal_list_values.index(min(removal_list_values))
        removal_card = removal_list[removal_card_index]
        Euchre.deck_order_standard[dealer_index].remove((removal_card))
        
        Euchre.deck_order_standard[dealer_index].append(Euchre.trump_suit_card)
        
        game_1.player_response_label_list[3].configure(text = "removing card \n   from deck", fg = "red")
        window.update()
        window.after(1000)
        game_1.player_response_label_list[3].configure(text = "card removed", fg = "red")
        window.update()
        window.after(1000, lambda: game_1.show_trump())
        

        
                                

    def pick_up_questions_2(self, i, trump_card, trump_suit, dealer, dealer_index, player, player_deck):
        
        loner_player = "no"
        called_suit = None
        dec_num = random.random()
        loner_dec_num = dec_num
        if player in Euchre.team_1:
            dec_num -=.25
        player_deck_c = player_deck.copy()
        clubs_list, spades_list, diamonds_list, hearts_list = ["clubs"], ["spades"], ["diamonds"], ["hearts"]
        all_suits_nested_list = [clubs_list, spades_list, diamonds_list, hearts_list]
        trump_list_matchup = {"clubs": clubs_list, "spades": spades_list, "diamonds": diamonds_list, "hearts": hearts_list} 
        for card in player_deck_c:
            if card.get_suit() == "spades":
                spades_list.append(card.get_card_name())
            elif card.get_suit() == "clubs":
                clubs_list.append(card.get_card_name())
            elif card.get_suit() == "hearts":
                hearts_list.append(card.get_card_name())
            elif card.get_suit() == "diamonds":
                diamonds_list.append(card.get_card_name())
        for list in all_suits_nested_list:
            if len(list) == 1:
                all_suits_nested_list.remove(list)

        for list in all_suits_nested_list:
            other_suits_in_deck = 0
            other_cards_in_deck = []
            list_suit = list[0]
            list_suit_pair = Euchre.trump_suit_pairs[list_suit]
            partner_list = None
            for list2 in all_suits_nested_list:
                if list2[0] == list_suit_pair:
                    partner_list = list2
            if partner_list:
                if "jack" in partner_list:
                    list.append("jack_lft")
            other_suits_in_deck = len(all_suits_nested_list) - 1
            other_cards_in_deck = []
            for list3 in all_suits_nested_list:
                if list3 != list:
                    other_cards_in_deck.extend(list3[1:])
            if len(list) - 1 == 5:
                called_suit = list[0]
                loner_player = player   
            elif len(list)-1 == 4:
                loner_player, called_suit = AI.call_suit_4_card(self, list, other_suits_in_deck, other_cards_in_deck, dec_num, loner_dec_num)
            elif len(list)-1 == 3:
                loner_player, called_suit = AI.call_suit_3_card(self, list, other_suits_in_deck, other_cards_in_deck, dec_num, loner_dec_num)
            elif len(list)-1 ==2:
                called_suit = AI.call_suit_2_card(self, list, other_suits_in_deck, other_cards_in_deck, dec_num)
            if called_suit != None:
                window.after(1000, game_1.player_response_label_list[i].configure(text = "calling {}".format(called_suit), fg = "red"))
                window.update()
                if loner_player != "no":
                    game_1.trump_info_list = ["no", game_1.player_order[i], called_suit, game_1.player_order[i]]
                    window.after(1000, lambda: game_1.show_trump())
                else:
                    game_1.trump_info_list = ["no", game_1.player_order[i], called_suit, "no"]
                game_1.trump_suit = called_suit
                game_1.trump_card = None
                window.after(1000, lambda: game_1.show_trump())
                return
        if i == 3:
            called_suit = self.caller_force_choose(all_suits_nested_list)
            window.after(1000, game_1.player_response_label_list[i].configure(text = "calling {}".format(called_suit), fg = "red"))
            window.update()
            if loner_player != "no":
                game_1.trump_info_list = ["no", game_1.player_order[i], called_suit, game_1.player_order[i]]
                window.after(1000, lambda: game_1.show_trump())
            else:
                game_1.trump_info_list = ["no", game_1.player_order[i], called_suit, "no"]
            game_1.trump_suit = called_suit
            game_1.trump_card = None
            window.after(1000, lambda: game_1.show_trump())
        
        
        else:
            self.pass_decision_callround(i)
    
    def pass_decision_callround(self, i):
        window.after(1000, game_1.player_response_label_list[i].configure(text = "pass"))
        window.update()
        game_1.call_it_decide(i = i+1)

                                
    def call_suit_4_card(self, list, other_suits_in_deck, other_cards_in_deck, dec_num, loner_dec_num):
        loner_player = "no"
        called_suit = None
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in list if i in ["9", "10", "queen", "king"]])
        comp_deck_ct_2 = len([i for i in list if i in ["ace", "jack", "jack_lft"]])
        comp_deck_ct_3 = len([i for i in list if i in ["9", "10"]])  
        comp_deck_ct_4 = len([i for i in other_cards_in_deck if i in ["9", "10", "jack", "queen"]])  
        comp_deck_ct_5 = len([i for i in list if i in ["ace", "jack", "jack_lft", "king"]])
        
        if comp_deck_ct_5 == 4:
            if comp_deck_ct_5 == 0:
                loner_player, called_suit = "yes", list[0] if ("ace" in other_cards_in_deck and comp_deck_ct_3 != 2) else "no", list[0]
            else:
                loner_player, called_suit = "no", list[0]
        elif comp_deck_ct_2 == 3:
            if comp_deck_ct_4 == 1:
                loner_player, called_suit = "no", list[0]
            else:
                loner_player, called_suit = "yes", list[0] if "ace" in other_cards_in_deck else "no", list[0]
                
        else:
            called_suit = list[0]
        return loner_player, called_suit
    
    def call_suit_3_card(self, list, other_suits_in_deck, offsuit_cards_in_deck, dec_num, loner_dec_num):
        loner_player = "no"
        called_suit = None
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in list if i in ["ace", "jack_lft", "jack"]])
        comp_deck_ct_2 = len([i for i in list if i in ["king", "ace", "jack_lft", "jack"]])
        comp_deck_ct_3 = len([i for i in list if i in ["queen", "king", "ace", "jack_lft", "jack"]])
        comp_deck_ct_4 = len([i for i in list if i in ["9", "10"]])
        comp_deck_ct_5 = len([i for i in list if i in ["jack_lft", "jack"]])
        comp_deck_ct_6 = len([i for i in offsuit_cards_in_deck if i in ["9", "10", "jack", "queen"]]) 
        if comp_deck_ct_1 == 3:
            loner_player, called_suit = "no", list[0]
        elif (comp_deck_ct_1 == 2 and other_suits_in_deck == 1) or comp_deck_ct_5 == 2:
            called_suit = list[0]
        elif comp_deck_ct_2 == 3 and (other_suits_in_deck == 1 or "ace" in offsuit_cards_in_deck):
            loner_player, called_suit = "no", list[0]
        elif comp_deck_ct_3 == 3:
            called_suit = list[0]
        elif comp_deck_ct_5 == 2:
            called_suit = list[0]
        elif comp_deck_ct_2 == 2:
            if comp_deck_ct_4 == 0 or "ace" in offsuit_cards_in_deck or other_suits_in_deck == 1:
                called_suit = list[0]
            else:
                called_suit = list[0] if dec_num <.8 else None
                
        elif comp_deck_ct_4 == 2:
            if comp_deck_ct_5 == 1 and other_suits_in_deck == 1:
                called_suit = list[0] if dec_num < .05 else None
            elif comp_deck_ct_5 == 1 and other_suits_in_deck > 1:
                called_suit = list[0] if dec_num < .5 else None
            elif comp_deck_ct_1 == 1 and other_suits_in_deck == 1:
                called_suit = list[0] if dec_num < .85 else None
            else:
                called_suit = list[0] if ((other_suits_in_deck == 1 or "ace" in offsuit_cards_in_deck) and dec_num < .65) or dec_num < .33 else None
        else:
            called_suit = list[0] if dec_num < .5 else None       
        
        return loner_player, called_suit
    
    def call_suit_2_card(self, list, other_suits_in_deck, offsuit_cards_in_deck, dec_num):
        called_suit = None 
        comp_deck_ct_1, comp_deck_ct_2, comp_deck_ct_3, comp_deck_ct_4, comp_deck_ct_5, comp_deck_ct_6 = 0, 0, 0, 0, 0, 0
        comp_deck_ct_1 = len([i for i in list if i in ["jack_lft", "jack"]])
        comp_deck_ct_2 = len([i for i in list if i in ["ace", "jack_lft", "jack"]])
        comp_deck_ct_3 = len([i for i in list if i in ["king", "jack"]])                      
        comp_deck_ct_4 = len([i for i in list if i in ["queen", "jack"]])   
        comp_deck_ct_5 = len([i for i in list if i in ["9", "10", "queen"]]) 
        comp_deck_ct_6 = len([i for i in list if i in ["ace", "jack_lft", "jack", "king"]])
        
        if comp_deck_ct_1 == 2:
            called_suit = list[0]
        
        elif offsuit_cards_in_deck.count("ace") >= 2 and comp_deck_ct_5 != 2:
            called_suit = list[0]
            
        elif other_suits_in_deck == 1:
            if "ace" in offsuit_cards_in_deck:
                called_suit = list[0] if comp_deck_ct_2 == 2 else \
                            (list[0] if (comp_deck_ct_3 == 2 or comp_deck_ct_6 ==2 or comp_deck_ct_4 == 2 and dec_num < .9) else (list[0] if dec_num < .45 else None))
            elif "king" in offsuit_cards_in_deck:
                called_suit = list[0] if comp_deck_ct_2 == 2 and dec_num < .75 else \
                               (list[0] if (comp_deck_ct_3 == 2 and dec_num < .25) else None)
            elif comp_deck_ct_2 == 2:
                called_suit = list[0] if dec_num < .5 else None
            elif comp_deck_ct_3 == 2:
                called_suit = list[0] if dec_num < .4 else None
        elif other_suits_in_deck == 2:
            if "ace" in offsuit_cards_in_deck:
                called_suit = list[0] if comp_deck_ct_2 == 2 and dec_num < .4 else (list[0] if comp_deck_ct_6 == 2 or "jack" in list and dec_num < .25 else None)
            elif comp_deck_ct_3 ==  2:
                called_suit == list[0] if dec_num < .15 else None
        elif other_suits_in_deck == 3:
            if comp_deck_ct_3 == 2:
                called_suit = list[0] if (dec_num < .15 and "ace" in off_suit_cards_in_deck) else \
                               (list[0] if dec_num < .5 else None)
        return called_suit
    
    def caller_force_choose(self, all_suits_nested_list):
        strongcard_suit_list = []
        longcard_suit_list = []
        longcard_suit_list_length = 3
        suits_2_or_more = []
        called_suit = None
        for list in all_suits_nested_list:
            if "jack" in list and ("jack_lft" in list or "ace" in list or "king" in list or "queen" in list):
                strongcard_suit_list = list
            elif "jack_lft" in list and "ace" in list:
                strong_card_suit_list = list
            if len(list) > longcard_suit_list_length:
                longcard_suit_list_length, longcard_suit_list = len(list), list
            if len(list) >= 3:
                suits_2_or_more.append(list)

        if longcard_suit_list_length >= 5:
            called_suit = longcard_suit_list[0]
        else:
            if strongcard_suit_list:
                if longcard_suit_list_length == 4:
                    if len([i for i in long_card_suit_list if i in ["jack_lft", "jack", "ace"]]) == 0:
                        called_suit == strongcard_suit_list[0]
                    else:
                        called_suit = longcard_suit_list[0]
                else:
                    called_suit = strongcard_suit_list[0]
            elif longcard_suit_list_length <= 3:
                if len(suits_2_or_more) == 1:
                    called_suit = (suits_2_or_more[0])[0]
                elif len(suits_2_or_more) == 2:
                    max_strength = 0
                    max_suit = ""
                    card_strength_dict = {"9":9, "10":10, "queen":11, "king":12, "ace":13, "jack_lft":14, "jack":15}
                    for list in suits_2_or_more:
                        list_strength = 0
                        for card in list[1:]:
                            list_strength += card_strength_dict[card]
                        if list_strength > max_strength:
                            max_strength, max_suit = list_strength, list[0]
                    called_suit = max_suit 
        if called_suit == None:
            called_suit = all_suits_nested_list[0][1]
        return called_suit
    
    def first_chooser_card_choice(self, i, player_deck):
        player = game_1.player_order[i]
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
        if offtrump_card_names:
            if len([i for i in offtrump_card_names if i in ["queen", "king", "ace"]]) == 0 and len([i for i in trump_suit_cards if i in ["jack", "jack_lft", "ace"]]) >=1:
                card_values = [Euchre.card_values_trump[card] for card in trump_suit_cards]
                max_card_index = card_values.index(max(card_values))
                card_to_play_name = trump_suit_cards[max_card_index]
                card_to_play_suit = Euchre.trump_suit_pairs[game_1.trump_suit] if card_to_play_name == "jack_lft" else game_1.trump_suit
            else:
                card_to_play_name = offtrump_card_names[max_card_index]
                card_to_play_suit = offtrump_card_suites[max_card_index]
        else:
            card_to_play_name = trump_suit_cards[max_card_index]
            card_to_play_suit = Euchre.trump_suit_pairs[game_1.trump_suit] if card_to_play_name == "jack_lft" else game_1.trump_suit
                
        if card_to_play_name == "jack_lft":
            card_to_play_name = "jack"
        card_to_play = None
        for card in player_deck:
            if card.get_card_name() == card_to_play_name and card.get_suit() == card_to_play_suit:
                card_to_play = card
        
        game_1.laid_down.append(card_to_play)
        game_1.round_players.append(game_1.player_order[i])
        window.after(1000, lambda: [self.visual_play_card(i, player, card_to_play), game_1.euchre_trick(i=i+1)])
       
    def visual_play_card(self, i, player, card_to_play):
        self.card_play_lf = LabelFrame(window, text = player.name)
        if game_1.player_order[i].name == "AI 3":
            self.card_play_lf.configure(text = "AI 3 (Teammate)", bg = "#ADD8E6")
        self.card_play_lf.place(relx = (.25 + (i * .09)), rely = .2)
        self.card_play_label = Label(self.card_play_lf, image = card_to_play.get_small_pic())
        self.card_play_label.grid(column = 0, row = 0)
        game_1.deck_order[i].remove(card_to_play)
        window.update()
            
        
            
    def card_choice_question(self, i, player_deck):
        if i == 0:
            self.first_chooser_card_choice(i, player_deck)
        else:
            self.normal_card_choice_question(i, player_deck)
    
    def normal_card_choice_question(self, i, player_deck):
        left_bower = Euchre.left_bowers[game_1.trump_suit]
        player = game_1.player_order[i]
        led_suit = (game_1.laid_down[0]).get_suit()
        if game_1.laid_down[0] == left_bower:
            led_suit = game_1.trump_suit
        current_winning_card = None
        current_winning_player = None
        led_suit_in_hand = []
        trump_suit_in_hand = []
        other_suits_in_hand_suits = []
        other_suits_in_hand_card = []
        choosing_deck = None
        choosing_deck_values = []
        card_to_play_index = None
        
        current_winner_index = game_1.determine_highest(game_1.laid_down)
        current_winning_player = game_1.player_order[current_winner_index]
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
            choosing_deck = led_suit_in_hand
            if led_suit == game_1.trump_suit:
                choosing_deck_values = [Euchre.card_values_trump[card] for card in choosing_deck]
            else:
                choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
            if Euchre.player_opposites[player] in game_1.round_players and current_winning_player == Euchre.player_opposites[player]:
                card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                min_choosing_deck = min(choosing_deck_values)

            else:
                potential_laid_down = game_1.laid_down.copy()
                lowest_card_index = choosing_deck_values.index(min(choosing_deck_values))
                highest_card_index = choosing_deck_values.index(max(choosing_deck_values))
                potential_card = None
                max_or_min = lowest_card_index
                while True:
                    if choosing_deck[max_or_min] == "jack_lft":
                        for card in player_deck:
                            if card == left_bower:
                                potential_card = card
                    for card in player_deck:
                        if card.get_card_name() == choosing_deck[max_or_min] and card.get_suit() == led_suit:
                            potential_card = card
                    potential_laid_down.append(potential_card)
                    potential_winner_index = game_1.determine_highest(potential_laid_down)
                    if potential_laid_down[potential_winner_index] == potential_card:
                        card_to_play_index = max_or_min
                        break
                    else:
                        if max_or_min == lowest_card_index and lowest_card_index != highest_card_index:
                            max_or_min = highest_card_index
                        else:
                            break
            
                if card_to_play_index == None:
                    card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                    min_choosing_deck = min(choosing_deck_values)
                
                potential_laid_down.remove(potential_card)
                
                    
        elif len(trump_suit_in_hand) >= 1:
            choosing_deck = trump_suit_in_hand
            choosing_deck_values = [Euchre.card_values_trump[card] for card in choosing_deck]
            if current_winning_player == Euchre.player_opposites[player]:
                if i == (len(game_1.player_order) - 1):
                    if other_suits_in_hand_card:
                        choosing_deck = other_suits_in_hand_card
                        choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
                        card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                    else:
                        card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))

                else:
                    potential_laid_down = game_1.laid_down.copy()
                    lowest_card_index = choosing_deck_values.index(min(choosing_deck_values))
                    highest_card_index = choosing_deck_values.index(max(choosing_deck_values))
                    potential_card = None
                    max_or_min = lowest_card_index
                    while True:
                        if choosing_deck[max_or_min] == "jack_lft":
                            for card in player_deck:
                                if card == left_bower:
                                    potential_card = card
                        for card in player_deck:
                            if card.get_card_name() == choosing_deck[max_or_min] and card.get_suit() == game_1.trump_suit:
                                potential_card = card
                        potential_laid_down.append(potential_card)
                        potential_winner_index = game_1.determine_highest(potential_laid_down)
                        if potential_laid_down[potential_winner_index] == potential_card:
                            dec_num = random.random()
                            if current_winning_card.get_value() <= 10:
                                if dec_num < .85:
                                    if other_suits_in_hand_card:
                                        choosing_deck = other_suits_in_hand_card
                                        choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
                                    card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                                    break
                                else:
                                    card_to_play_index = max_or_min
                                    break
                            else:   
                                if other_suits_in_hand_card:
                                    choosing_deck = other_suits_in_hand_card
                                    choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
                                card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                                break
                        else:
                            if max_or_min == lowest_card_index and lowest_card_index != highest_card_index:
                                max_or_min = highest_card_index
                            else:
                                break
                    potential_laid_down.remove(potential_card)   
                    if card_to_play_index == None:
                        if other_suits_in_hand_card:
                            choosing_deck = other_suits_in_hand_card
                            choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
                        card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
        
            else:
                potential_laid_down = game_1.laid_down.copy()
                lowest_card_index = choosing_deck_values.index(min(choosing_deck_values))
                highest_card_index = choosing_deck_values.index(max(choosing_deck_values))
                potential_card = None
                max_or_min = lowest_card_index
                while True:
                    if choosing_deck[max_or_min] == "jack_lft":
                        for card in player_deck:
                            if card == left_bower:
                                potential_card = card
                    for card in player_deck:
                        if card.get_card_name() == choosing_deck[max_or_min] and card.get_suit() == game_1.trump_suit:
                            potential_card = card
                    potential_laid_down.append(potential_card)
                    potential_winner_index = game_1.determine_highest(potential_laid_down)
                    if potential_laid_down[potential_winner_index] == potential_card:
                        card_to_play_index = max_or_min
                        break
                    else:
                        if max_or_min == lowest_card_index and lowest_card_index != highest_card_index:
                            max_or_min = highest_card_index
                        else:
                            break
                potential_laid_down.remove(potential_card)            
                if card_to_play_index == None:
                    if other_suits_in_hand_card:
                        choosing_deck = other_suits_in_hand_card
                        choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
                    card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))
                
        
        else:
            choosing_deck = other_suits_in_hand_card
            choosing_deck_values = choosing_deck_values = [Euchre.card_values_nontrump[card] for card in choosing_deck]
            card_to_play_index = choosing_deck_values.index(min(choosing_deck_values))

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

        
        game_1.laid_down.append(card_to_play_total)
        game_1.round_players.append(game_1.player_order[i])
        window.after(1000, lambda: [self.visual_play_card(i, player, card_to_play_total), game_1.euchre_trick(i=i+1)])

        
        
game_1 = Euchre()
game_1.play_euchre()



window.mainloop()

