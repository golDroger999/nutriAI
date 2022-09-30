import numpy as np


class HitungGiziKelompok():
    def __init__(self, bb, tb, umur, gender):
        self.bb = bb
        self.tb = tb
        self.umur = umur 
        self.gender = gender
        
        
    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return imt
    
    
    
    
    def statusgizi(self):
        imt = self.bb / (self.tb/100)**2
        
        data = [
                (imt <  18.5),
                (imt > 18.5 ) & (imt < 25),
                (imt > 25 ) & (imt < 30),
                (imt > 29 ) 
                ]
        
        value = ['kurus', 'ideal', 'gemuk', 'obesitas']
        
        status = np.select(data, value)
        return status
    
    
    
    
    def energi(self, tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb-100)
        bmr_pria    = 1 * 24 * self.bb
        bmr_wanita  = 0.90 * 24 * self.bb
        
        bmr_coice   = [
            (self.gender == 'pria'),
            (self.gender == 'wanita')
            ]
        
        bmr = [bmr_pria, bmr_wanita]
        bmr = np.select(bmr_coice, bmr)
        
        koreksi_tidur   = 0.1 * tidur * self.bb
        c_kalori        = bmr - koreksi_tidur
        aktivitas       = aktivitas * c_kalori
        e_kalori        = c_kalori + aktivitas
        sda             = 0.1 * e_kalori
        energi          = e_kalori + sda 
        return (energi)
    
    
    
    
    def protein(self, tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb-100)
        bmr_pria    = 1 * 24 * self.bb
        bmr_wanita  = 0.90 * 24 * self.bb
        
        bmr_coice   = [
            (self.gender == 'pria'),
            (self.gender == 'wanita')
            ]
        
        bmr = [bmr_pria, bmr_wanita]
        bmr = np.select(bmr_coice, bmr)
        
        koreksi_tidur   = 0.1 * tidur * self.bb
        c_kalori        = bmr - koreksi_tidur
        aktivitas       = aktivitas * c_kalori
        e_kalori        = c_kalori + aktivitas
        sda             = 0.1 * e_kalori
        energi          = e_kalori + sda 
        protein         = (0.15 * energi)/4
        return (protein)
    
    
    
    
    def lemak(self, tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb-100)
        bmr_pria    = 1 * 24 * self.bb
        bmr_wanita  = 0.90 * 24 * self.bb
        
        bmr_coice   = [
            (self.gender == 'pria'),
            (self.gender == 'wanita')
            ]
        
        bmr = [bmr_pria, bmr_wanita]
        bmr = np.select(bmr_coice, bmr)
        
        koreksi_tidur   = 0.1 * tidur * self.bb
        c_kalori        = bmr - koreksi_tidur
        aktivitas       = aktivitas * c_kalori
        e_kalori        = c_kalori + aktivitas
        sda             = 0.1 * e_kalori
        energi          = e_kalori + sda 
        lemak           = (0.25 * energi)/9
        return (lemak)
    
    
    
    
    def karbo(self, tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb-100)
        bmr_pria    = 1 * 24 * self.bb
        bmr_wanita  = 0.90 * 24 * self.bb
        
        bmr_coice   = [
            (self.gender == 'pria'),
            (self.gender == 'wanita')
            ]
        
        bmr = [bmr_pria, bmr_wanita]
        bmr = np.select(bmr_coice, bmr)
        
        koreksi_tidur   = 0.1 * tidur * self.bb
        c_kalori        = bmr - koreksi_tidur
        aktivitas       = aktivitas * c_kalori
        e_kalori        = c_kalori + aktivitas
        sda             = 0.1 * e_kalori
        energi          = e_kalori + sda 
        karbo = (0.65 * energi)/4 
        return (karbo)