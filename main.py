import random

class App:
    def __init__(self):
        self.szint = ''
    
    
    def kezdes(self):
        while self.szint != 'kilépés':
            self.szint = input('Válassz szintet:\n kezdő\n közepes\n haladó\n profi\n kilépés\n\nVálasztás: ')
            if self.szint == 'kezdő':
                from kezdo import Kezdo
            elif self.szint == 'közepes':
                print('Fejlesztés alatt\n')
            elif self.szint == 'haladó':
                print('Fejlesztés alatt\n')
            elif self.szint == 'profi':
                print('Fejlesztés alatt\n')
            elif self.szint == 'kilépés':
                print('Köszönöm a játékot, további szép napot!')
                break
            else:
                print('Az alábbi opciók elérhetők: kezdő, közepes, haladó, profi, kilépés')
                
           
app = App()
app.kezdes()