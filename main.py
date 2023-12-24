import random

class App:
    def __init__(self):
        self.szavak_harom = 'harom_betus.txt'
        self.harom_betus = []
        
    def fajl_beolvas(self):
        fp = open(self.szavak_harom, 'r', encoding='utf-8')
        lines = fp.readlines()
        fp.close()
        
        for line in lines:
            line = line.rstrip()
            self.harom_betus.append(line)
        
    def szo_valasztas(self):
        self.szo = random.choice(self.harom_betus)
    
    def jatek(self):
        self.valtozo = ''
        
        #különböző esetek
        while self.valtozo != self.szo:
            try:
                self.valtozo = input('Add meg a szavadat: ')
                if self.valtozo[0] == self.szo[0] and self.valtozo[1] != self.szo[1] and self.valtozo[2] != self.szo[2]:
                    print(f'{self.szo[0]} * *')
                elif self.valtozo[0] != self.szo[0] and self.valtozo[1] == self.szo[1] and self.valtozo[2] != self.szo[2]:
                    print(f'* {self.szo[1]} *')
                elif self.valtozo[0] != self.szo[0] and self.valtozo[1] != self.szo[1] and self.valtozo[2] == self.szo[2]:
                    print(f'* * {self.szo[2]}')
                elif self.valtozo[0] == self.szo[0] and self.valtozo[1] == self.szo[1] and self.valtozo[2] != self.szo[2]:
                    print(f'{self.szo[0]} {self.szo[1]} *')
                elif self.valtozo[0] != self.szo[0] and self.valtozo[1] == self.szo[1] and self.valtozo[2] == self.szo[2]:
                    print(f'* {self.szo[1]} {self.szo[2]}')
                elif self.valtozo[0] == self.szo[0] and self.valtozo[1] != self.szo[1] and self.valtozo[2] == self.szo[2]:
                    print(f'{self.szo[0]} * {self.szo[2]}')
                
                #ha szabad a gazda
                elif self.valtozo == 'szabad':
                    print(self.szo)
                    break
                    
                    #ha kitalálta
                elif self.valtozo == self.szo:
                    print('Gratulálok, eltaláltad!')
                    
            except IndexError:
                print('Három betűs szavakat adj meg!')
    #def jatek vége
            
                     
app = App()
app.fajl_beolvas()
app.szo_valasztas()
app.jatek()