class makan():
    def __init__(self, energi, protein, lemak, karbo):
        self.energi = energi
        self.protein = protein
        self.lemak = lemak
        self.karbo = karbo
    
    def makan(self):
        energi_pagi=round(0.35* self.energi, 2)
        protein_pagi=round(0.35*self.protein,2)
        lemak_pagi=round(0.35*self.lemak,2)
        karbo_pagi=round(0.35*self.karbo,2)
    
        energi_malam=round(0.30* self.energi, 2)
        protein_malam=round(0.30*self.protein,2)
        lemak_malam=round(0.30*self.lemak,2)
        karbo_malam=round(0.30*self.karbo,2)
        
        makan = {
            'energi_pagi' : energi_pagi, 'protein_pagi' : protein_pagi, 'lemak_pagi' : lemak_pagi, 'karbo_pagi' : karbo_pagi,
            'energi_malam' : energi_malam, 'protein_malam' : protein_malam, 'lemak_malam' : lemak_malam, 'karbo_malam' : karbo_malam,
        }
        
        return makan