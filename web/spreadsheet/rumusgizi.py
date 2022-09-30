class HitungGiziKelompok():
    def __init__(self, bb, tb, umur, gender):
        self.bb = bb
        self.tb = tb
        self.umur = umur 
        self.gender = gender
        
    def imt(self):
        imt = self.bb / (self.tb*100)**2
        return round(imt,2)