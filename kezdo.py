import random
class Kezdo:
    def __init__(self):
        self.szavak_harom = 'harom_betus.txt'
        self.harom_betus = []
        self.nem_talalt = []
        self.pont = 0
        self.opcio = ''
        self.valtozo =''
        self.aktual_pont = 0
        
    def fajl_beolvas(self):
        fp = open(self.szavak_harom, 'r', encoding='utf-8')
        lines = fp.readlines()
        fp.close()
        
        for line in lines:
            line = line.rstrip()
            self.harom_betus.append(line)
        
    def szo_valasztas(self):
        self.szo = random.choice(self.harom_betus)
    
    def kieso_szavak(self):
        if self.valtozo != self.szo:
            if self.valtozo != 'szabad' and self.valtozo != 'elso' and self.valtozo != 'masodik' and self.valtozo != 'harmadik' and len(self.valtozo) == 3:
                self.nem_talalt.append(self.valtozo)
                print('Nem megfelelő szavak:\n', self.nem_talalt)
            elif self.valtozo == 'elso' or self.valtozo == 'masodik' or self.valtozo == 'harmadik':
                self.aktual_pont += -10
            elif self.valtozo == 'szabad':
                self.aktual_pont += -80   

    def talalat(self):
        while self.valtozo != self.szo:
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
                elif self.valtozo == self.szo:
                    print('Gratulálok, eltaláltad!')
                    
            elif self.valtozo == 'szabad':
                print(self.szo)   
            elif self.valtozo == 'elso':
                print(self.szo[0])
            elif self.valtozo == 'masodik':
                print(self.szo[1])
            elif self.valtozo == 'harmadik':
                print(self.szo[2])
            else:
                print('Három betűs szavakat adj meg!')
            app.kieso_szavak()
                    
    def pont_szamito(self):
        if self.valtozo == self.szo:
            self.pont += 100
            self.levonas = len(self.nem_talalt)*1
            self.pont = self.pont - self.levonas
            self.pont += self.aktual_pont
                
    def kor(self):
        self.valtozo = ''
        print('Ha szabad a gazda, akkor írd be, hogy: szabad')
        print('Ha nem tudsz egy szót, írd be, hogy: elso vagy masodik vagy harmadik')
        app.szo_valasztas()
        app.talalat()
        app.pont_szamito()
        print('Pontszám:', self.pont)
        self.nem_talalt.clear()
    
    def futtatas(self):
        while self.opcio != 'vége':
            if self.pont == 0:
                print('\n\nVálassz opciót:\n Játék elkezdése (kezdés)\n Aktuális pontszám(pontszám)\n Kilépés(kilépés)')   
                self.opcio = input('\nVálasztott opció: ')
                if self.opcio == 'kezdés':
                    app.kor()
                elif self.opcio == 'pontszám':
                    print('Aktuális pontszám:', self.pont)
                elif self.opcio == 'kilépés':
                    print('Játék vége!\nElért pontszám:', self.pont)
                    break
                else:
                    print('Alábbi parancsokat írd be: kezdés pontszám vége.')
                    
                    
            elif self.pont > 0:
                print('\n\nVálassz opciót:\n Játék folytatása (folytatás)\n Aktuális pontszám(pontszám)\n Kilépés(kilépés)')   
                self.opcio = input('\nVálasztott opció: ')
                if self.opcio == 'folytatás' or self.opcio == 'folytat':
                    app.kor()
                elif self.opcio == 'pontszám' or self.opcio == 'pont' or self.opcio == 'pontok':
                    print('Aktuális pontszám:', self.pont)
                elif self.opcio == 'vége' or self.opcio == 'kilépés':
                    print('Játék vége!\nElért pontszám:', self.pont)
                    break
                else:
                    print('Alábbi parancsokat írd be: kezdés pontszám vége.')                                  
app = Kezdo()
app.fajl_beolvas()
app.futtatas()
