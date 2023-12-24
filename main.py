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
        print('Ha szabad a gazda, akkor írd be, hogy: szabad')
        print('Ha nem tudsz egy szót, írd be, hogy: elso vagy masodik vagy harmadik')
        #különböző esetek
        while self.valtozo != self.szo:
            try:
                self.valtozo = input('Add meg a szavadat: ')
                if len(self.valtozo) ==3:
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
                        
                    #ha eltalálta    
                    elif self.valtozo == self.szo:
                        print('Gratulálok, eltaláltad!')
                      
                else:
                    #ha szabad a gazda
                    if self.valtozo == 'szabad':
                        print(self.szo)
                        break
                        
                    #ha segítséget kért
                    elif self.valtozo == 'elso':
                        print(self.szo[0])
                    elif self.valtozo == 'masodik':
                        print(self.szo[1])
                    elif self.valtozo == 'harmadik':
                        print(self.szo[2])
                    
            except IndexError:
                print('Három betűs szavakat adj meg!')
    #def jatek vége
            
                     
app = App()
app.fajl_beolvas()
app.szo_valasztas()
app.jatek()
