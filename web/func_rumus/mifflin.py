class mifflin():
    
    def __init__(self, bb, tb, usia, gender, aktivitas, stress):
        self.bb = bb
        self.tb = tb 
        self.usia = usia  
        self.gender = gender
        self.aktivitas = aktivitas
        self.stress = stress
        
        
        
        
    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return round(imt,2)



    def bbi(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100) 
        
        return round(bbi,2)
    
    
    
    
    def bee(self):
        
        if self.gender == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.gender == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
            
        return round(bmr,2)
    
    
    
    
    def tee(self):
        
        if self.gender == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.gender == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        return round(total_energi,2)
    
    
    
    def protein(self):
        
        if self.gender == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.gender == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        protein = (0.15 * total_energi)/4
        
        return round(protein,2)
    
    
    
    def lemak(self):
        
        if self.gender == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.gender == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        lemak = (0.20 * total_energi)/9
        
        return round(lemak,2)
    
    
    
    def karbohidrat(self):
        
        if self.gender == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.gender == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        karbohidrat = (0.60 * total_energi)/4
        
        return round(karbohidrat,2)
    
    

    
    