import card as c
import hands as h
from commonGameFunctions import *
class War_Card(c.Pos_card):
    ACE_VALUE = 14
    KING_VALUE = 13
    QUEEN_VALUE = 12
    JACK_VALUE = 11
    @property
    def value(self):
        if self.faceUp:
            v = War_Card.RANK.index(self.rank)+1
        else:
            v = None
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

class War_Player(War_Hand):
    pass
class War_Game(object):
    def __init__(self,names):
        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.deck.deal(self.players,26)
    def play(self):
        self.table = War_Hand()
        for player in self.players:
            player.give(player.cards[0],self.table)
        if self.table.cards[0] > self.table.cards[1]:
            for card in self.table:
                self.table.give(card)