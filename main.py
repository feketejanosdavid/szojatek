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
    
    def kitalalas(self):
        print(len(self.szo))
            
app = App()
app.fajl_beolvas()
app.szo_valasztas()
app.kitalalas()