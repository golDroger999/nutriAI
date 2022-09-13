class gizimikro():
    
    def __init__(self, umur, gender):
        self.umur = umur 
        self.gender = gender 
        
        
    def vitamin_a(self):
        if self.gender == 'pria' and self.umur < 13:
            vitamin_a = 600
        
        elif self.gender == 'pria' and self.umur < 16:
            vitamin_a = 600
            
        elif self.gender == 'pria' and self.umur < 19:
            vitamin_a = 700
            
        elif self.gender == 'pria' and self.umur < 30:
            vitamin_a = 650
            
        elif self.gender == 'pria' and self.umur < 50:
            vitamin_a = 650
            
        elif self.gender == 'pria' and self.umur < 65:
            vitamin_a = 650
            
        elif self.gender == 'pria' and self.umur < 81:
            vitamin_a = 650
            
        elif self.gender == 'pria' and self.umur > 80:
            vitamin_a = 650
        
        else:
            vitamin_a = 600
            
        return vitamin_a
    
    
    
    def vitamin_d(self):
        if self.gender == 'pria' and self.umur < 65:
            vitamin_d  = 15
            
        elif self.gender == 'pria' and self.umur > 64:
            vitamin_d = 20
            
        elif self.gender == 'wanita' and self.umur < 65:
            vitamin_d = 15
        
        elif self.gender == 'wanita' and self.umur > 64:
            vitamin_d = 20
        
        return vitamin_d 
    
    
    
    def vitamin_e(self):
        if self.gender == 'pria' and self.umur < 13:
            vitamin_e = 11
            
        elif self.gender =='pria' and self.umur > 12:
            vitamin_e = 15 
            
        elif self.gender == 'wanita' and self.umur < 65:
            vitamin_e = 15
        
        elif self.gender == 'wanita' and self.umur > 64:
            vitamin_e = 20

        return vitamin_e 
    
    
        
    def vitamin_k(self):
        if self.gender == 'pria' and self.umur < 13:
            vitamin_k = 35
            
        elif self.gender =='pria' and self.umur < 16:
            vitamin_k = 55
            
        elif self.gender =='pria' and self.umur < 19:
            vitamin_k = 55
            
        elif self.gender =='pria' and self.umur > 18:
            vitamin_k = 65
            
        elif self.gender == 'wanita' and self.umur < 13:
            vitamin_k = 35
            
        elif self.gender == 'wanita' and self.umur > 12:
            vitamin_k = 55
        
        return vitamin_k 
        
        
        
    def vitamin_b1(self):
        if self.gender =='pria' and self.umur < 13:
            vitamin_b1 = 1.1
            
        elif self.gender == 'pria' and self.umur > 12:
            vitamin_b1 = 1.2 
            
        elif self.gender =='wanita' and self.umur < 13:
            vitamin_b1 = 1.0
            
        elif self.gender == 'wanita' and self.umur > 12:
            vitamin_b1 = 1.1
        
        return vitamin_b1 
    
    
    
    
    def vitamin_b2(self):
        if self.gender =='pria' and self.umur > 9:
            vitamin_b2 = 1.3
            
        elif self.gender =='wanita' and self.umur < 19:
             vitamin_b2 = 1.0
        
        elif self.gender =='wanita' and self.umur > 18:
            vitamin_b2 = 1.1
            
        return vitamin_b2
    
    
    
    
    def vitamin_b3(self):
        if self.gender =='pria' and self.umur < 13:
            vitamin_b3 = 12
            
        elif self.gender =='pria' and self.umur > 12:
            vitamin_b3 = 16
            
        elif self.gender =='pria' and self.umur < 13:
            vitamin_b3 = 12
            
        elif self.gender =='pria' and self.umur > 12:
            vitamin_b3 = 14
        
        return vitamin_b3
    
    
    
    
    def vitamin_b5(self):
        if self.gender =='pria' and self.umur > 9:
            vitamin_b5 = 5.0
        
        else:
            vitamin_b5 = 5.0
        
        return vitamin_b5 
    
    
    
    
    def vitamin_b6(self):
        if self.gender =='pria' and self.umur < 50:
            vitamin_b6 = 1.3
            
        elif self.gender =='pria' and self.umur > 49:
            vitamin_b6 = 1.7 
        
        elif self.gender =='wanita' and self.umur < 19:
            vitamin_b6 = 1.2
            
        elif self.gender =='wanita' and self.umur < 50:
            vitamin_b6 = 1.3
            
        elif self.gender =='wanita' and self.umur > 49:
            vitamin_b6 = 1.5
            
        return vitamin_b6
    
    
    
    
    def vitamin_b12(self):
        if self.gender =='pria' and self.umur < 13:
            vitamin_b12 = 3.5
            
        elif self.gender =='pria' and self.umur > 12:
            vitamin_b12 = 4.0
            
        elif self.gender =='wanita' and self.umur < 13:
            vitamin_b12 = 3.5
            
        elif self.gender =='wanita' and self.umur > 12:
            vitamin_b12 = 4.0
        
        return vitamin_b12 
    
    
    
    
    def folat(self):
        folat = 400
        return folat 
    
    
    
    
    def biotin(self):
        pass 
    
    def kolin(self):
        pass 
    
    def vitamin_c(self):
        pass
    
    def kalsium(self):
        pass 
    
    def fosfor(self):
        pass 
    
    def magnesium(self):
        pass 
    
    def besi(self):
        pass 
    
    def iodium(self):
        pass 
    
    def seng(self):
        pass 
    
    def selenium(self):
        pass
    
    def mangan(self):
        pass 
    
    def fluor(self):
        pass 
    
    def kromium(self):
        pass 
    
    def kalium(self):
        pass 
    
    def natrium(self):
        pass 
    
    def klor(self):
        pass 
    
    def tembaga(self):
        pass