class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

couleur = ['Coeur', 'Pique', 'Carreau', 'Treffle']
deck = [Card(value, couleur) for value in range(1, 14) for i in couleur]
values = ['ace', '2','3','4','5','6','7','8','9','10',"Ace","Vallée","Dame","Roi"]
2,