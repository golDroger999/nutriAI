from flask import request

class Harris():
    def __init__(self):
        self.bb = float(request.form.get('bb'))
        self.tb = float(request.form.get('tb'))
        self.umur = int(request.form.get('umur'))
        self.gender = request.form.get('gender')
        self.stress = request.form.get('stress')
        self.aktivitas = request.form.get('aktivitas')
    
    
    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return round(imt,2)
    
    def bbi(self):
        bbi = 0.9 * (self.tb-100)
        return round(bbi,2)
    
    def bee(self):
        if self.gender == 'wanita':
            bee = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.gender == 'pria':
            bee = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia) 
            
        return round(bee,2)
            
            
    def tee(self):
        
        if self.jenis_kelamin == 'wanita':
            bee = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.jenis_kelamin == 'pria':
            bee = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bee * self.aktivitas * self.stress
        
        return round(tee,2)
        
        
    