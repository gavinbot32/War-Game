import card as c
import hands as h
from commonGameFunctions import *
class War_Card(c.Card):
    RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    @property
    def value(self):
        v = War_Card.RANK.index(self.rank)+2
        return v
class War_Deck(h.Deck):
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANK:
                card = War_Card(rank,suit)
                self.add(card)
class War_Hand(h.Hand):
    def __init__(self,name):
        super(War_Hand, self).__init__()
        self.name = name
    @property
    def playing(self):
        v = True
        if len(self.cards) <= 0:
            v = False
        return v




class War_Game(object):
    def __init__(self,names):
        self.players = []
        self.names = names
        for name in names:
            player = War_Hand(name)
            self.players.append(player)
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.deck.deal(self.players,26)
        for player in self.players:
            index = self.players.index(player)
            print(self.names[index],":",len(player.cards),"Cards")
    def war(self):
        pass
    def deck_length(self):
        for card in self.table.cards:
            index = self.table.cards.index(card)
            print(self.names[index],card)
    def check_table(self):
        self.deck_length()
        for player in self.players:
            player.give(player.cards[0], self.table)
        for card in self.table.cards:
            index = self.table.cards.index(card)
            print(self.names[index], card)
        input("Press enter to continue")
        if self.table.cards[0].value > self.table.cards[1].value:
            for card in self.table.cards:
                self.table.give(card, self.pot)
                self.winner = self.players[0]
        elif self.table.cards[1].value > self.table.cards[0].value:
            for card in self.table.cards:
                self.table.give(card, self.pot)
                self.winner = self.players[1]
        else:
            for card in self.table.cards:
                self.table.give(card, self.pot)
                self.war()
        for card in self.pot.cards:
            self.pot.give(card, self.winner)
    def play(self):
        self.table = h.Hand()
        self.pot = h.Hand()
        self.winner = None
        self.check_table()
        self.deck_length()
        input("Press enter to continue")
        while self.players[0].playing and self.players[1].playing:
            self.play()
        Gamewinner = None
        if self.players[0].playing:
            Gamewinner = self.names[0]
        else:
            Gamewinner = self.names[1]
        print(Gamewinner )