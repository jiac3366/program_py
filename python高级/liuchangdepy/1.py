import collections

a = collections.namedtuple('Card', ['rank', 'suit'])  # 创建一个带rank、suit属性的Card类


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [a(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    beer_card = a('7', 'diamonds')  # 创建方块7对象
    deck = FrenchDeck()  # 可以debugger
    from random import choice
    print(choice(deck))
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    for car in sorted(deck, key=spades_high):
        print(car)
    pass

    #  本章知识：
    #  for i in x 实际是调用iter(x) --> __iter(x)__
    #  len(x)实际是调用 __len()__ 所以如果是你自己写的对象需要遍历 就要自己实现__len()__