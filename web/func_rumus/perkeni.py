class perkeni():
    
    def __init__(self, bb, tb, umur, gender, aktivitas):
        self.bb = bb
        self.tb = tb
        self.umur = umur
        self.gender = gender
        self.aktivitas = aktivitas
    
    
    
    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return round(imt,2)



    def bbi(self):
        bbi = 0.9 * (self.tb - 100) 
        return round(bbi,2)        
    
    
    
    def bmr(self):
        
        bbi = 0.9 * (self.tb - 100)
        
        if self.gender == 'pria'   :
            bmr = 30 * bbi
        
        elif self.gender == 'wanita':
            bmr = 25 * bbi
        
        return round(bmr,2)



    
    def energi(self):
        if self.umur < 41:
            faktor_usia = 0 

        elif self.umur < 60:
            faktor_usia = 0.05
            
        elif self.umur < 70:
            faktor_usia = 0.10
            
        elif self.umur > 69:
            faktor_usia = 0.15

        bbi = 0.9 * (self.tb - 100)
        
        if self.gender == 'pria'   :
            bmr = 30 * bbi
        
        elif self.gender == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + self.aktivitas) - faktor_usia
        
        return round(energi,2)
    
    
    
    
    
    def protein(self):
        if self.umur < 41:
            faktor_usia = 0 

        elif self.umur < 60:
            faktor_usia = 0.05
            
        elif self.umur < 70:
            faktor_usia = 0.10
            
        elif self.umur > 69:
            faktor_usia = 0.15
            
        bbi = 0.9 * (self.tb - 100)
        
        if self.gender == 'pria'   :
            bmr = 30 * bbi
        
        elif self.gender == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + self.aktivitas) - faktor_usia    
        
        protein = (0.15 * energi)/4
        
        return round(protein,2)
    
    
    
    
    
    def lemak(self):
        if self.umur < 41:
            faktor_usia = 0 

        elif self.umur < 60:
            faktor_usia = 0.05
            
        elif self.umur < 70:
            faktor_usia = 0.10
            
        elif self.umur > 69:
            faktor_usia = 0.15
            
        bbi = 0.9 * (self.tb - 100)
        
        if self.gender == 'pria'   :
            bmr = 30 * bbi
        
        elif self.gender == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + self.aktivitas) - faktor_usia
        
        lemak = (0.25 * energi)/9
        
        return round(lemak,2)
    
    
    
    
    def karbo(self):
        if self.umur < 41:
            faktor_usia = 0 

        elif self.umur < 60:
            faktor_usia = 0.05
            
        elif self.umur < 70:
            faktor_usia = 0.10
            
        elif self.umur > 69:
            faktor_usia = 0.15
            
        bbi = 0.9 * (self.tb - 100)
        
        if self.gender == 'pria'   :
            bmr = 30 * bbi
        
        elif self.gender == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + self.aktivitas) - faktor_usia
        
        karbohidrat = (0.60 * energi)/4
        
        return round(karbohidrat,2)

    