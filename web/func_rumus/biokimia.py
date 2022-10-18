class biokimia():
    
    def __init__(self, umur, gender):
        self.umur = umur 
        self.gender = gender 
        
    
    def albumin(self, albumin=0):
        if albumin < 4:
            albumin = 'dibawah normal'
        
        elif  albumin < 5.4 and albumin > 3.9 :
            albumin = 'normal'
        
        elif albumin > 5.4:
            albumin = 'diatas normal'
            
        rujukan = '4 - 5.3 g/dl'     
        
        data = {'albumin' : albumin, 'rujukan':rujukan}
        
        return data
    
    
    
    
    def sgpt(self, sgpt=0):
        pass 
    
    
    
    
    def sgot(self, sgot=0):
        pass
    
    
    
    
    def bun(self, bun=0):
        pass
    
    
    
    
    def hdl(self, hdl=0):
        if hdl > 55:
            hdl = 'normal'
        
        elif hdl < 55 and hdl > 40 :
            hdl = 'batas rendah'
            
        elif hdl < 40:
            hdl = 'dibawah normal'
            
        rujukan = '40 - 60 mg/dl'
        
        data = {'hdl' : hdl, 'rujukan' : rujukan}
        
        return data
    
    
    
    def ldl(self, ldl=0):
        if ldl < 130 :
            ldl = 'normal'
        
        elif ldl < 160 :
            ldl = 'batas tinggi'
            
        elif ldl > 159 :
            ldl = 'diatas normal'
            
        rujukan = '<130 mg/dl'
        
        data = {'ldl' : ldl, 'rujukan' : rujukan}
        
        return data
    
    
    
    
    def trigliserida(self, trigliserida=0):
        pass
    
    
    
    
    def kolesterol_total(self, kolesterol_total=0):
        if kolesterol_total < 200:
            kolesterol_total = 'normal'
        
        elif kolesterol_total < 240:
            kolesterol_total = 'batas tinggi'
            
        elif kolesterol_total > 239:
            kolesterol_total = 'diatas normal'
    
        rujukan = '<200 mg/dl'     
        
        data = {'kolesterol' : kolesterol_total, 'rujukan':rujukan}
    
        return data 
    
    
    
    
    def bilirubin_direk(self, bilirubin_direk=0):
        pass
    
    
    
    
    def bilirubin_total(self, bilirubin_total=0):
        pass 
    
    
    
    
    def bilirubin_indirek(self, bilirubin_indirek=0):
        pass 
    

al = biokimia(umur=12, gender='pria').kolesterol_total(222)

print(al)

