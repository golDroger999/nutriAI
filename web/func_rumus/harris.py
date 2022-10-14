
class harris():
    
    def __init__(self, bb=None, tb=None, umur=None, gender=None, aktivitas=None, stress=None):
        self.bb = bb 
        self.tb = tb 
        self.umur = umur 
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
        
        if self.gender == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.umur)
        
        elif self.gender == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.umur)
                        
        return round(bmr,2) 
            
            
    
    def tee(self):
        
        if self.gender == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.umur)
        
        elif self.gender == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.umur)
        
        tee = bmr * self.aktivitas * self.stress 
        
        return round(tee,2)
    
    
    
    def protein(self):
        if self.gender == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.umur)
        
        elif self.gender == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.umur)
        
        tee = bmr * self.aktivitas * self.stress 
        
        protein = (0.15 * tee)/4
        
        return round(protein,2)



    def lemak(self):
        
       if self.gender == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.umur)
            
       elif self.gender == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.umur)
      
       tee = bmr * self.aktivitas * self.stress 
          
       lemak = (0.20 * tee)/9
        
       return round(lemak,2)
        


    def karbo(self):
        
        if self.gender == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.umur)
            
        elif self.gender == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.umur)
      
        tee = bmr * self.aktivitas * self.stress 
              
        karbohidrat  = (0.60 * tee)/4 
        
        return round(karbohidrat,2)
    
    def cairan(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        cairan = (bbi * 50)/1000
        
        return cairan
    
