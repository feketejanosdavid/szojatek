import random

class App:
    def __init__(self):
        self.szint = ''
    
    
    def kezdes(self):
        while self.szint != 'kilépés':
            self.szint = input('Válassz az alábbiak közül:\n kezdő       kilépés\n\nVálasztás: ')
            if self.szint == 'kezdő':
                from kezdo import Kezdo
            elif self.szint == 'kilépés':
                print('Köszönöm a játékot, további szép napot!')
                break
            else:
                print('Az alábbi opciók elérhetők: kezdő, kilépés')
                
           
app = App()
app.kezdes()