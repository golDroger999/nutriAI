import pandas as pd
import numpy as np  


class dubois():

    def __init__(self, bb=None, tb=None, umur=None, gender=None, aktivitas=None, tidur=None):
        self.bb = bb 
        self.tb = tb 
        self.umur = umur 
        self.gender = gender
        self.aktivitas = aktivitas
        self.tidur = tidur



    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return round(imt,2)



    def bbi(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100) 
        
        return round(bbi,2)



    def bmr(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        if self.gender == 'pria'   :
            bmr = 1 * 24 * bbi
        
        elif self.gender == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        return round(bmr,2)




    def energi(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.gender == 'pria':
            bmr = 1 * 24 * bbi
        
        elif self.gender == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * self.tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = self.aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        return round(total_energi,2)



    def protein(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.gender == 'pria':
            bmr = 1 * 24 * bbi
        
        elif self.gender == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur= 0.1 * self.tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = self.aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        protein      = (0.15 * total_energi)/4
        
        return round(protein,2)



    def lemak(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
       
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100)
       
       
        if self.gender == 'pria':
            bmr = 1 * 24 * bbi
       
        elif self.gender == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * self.tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = self.aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        lemak        = (0.25 * total_energi)/9
        
        return round(lemak,2)
        


    def karbo(self):
        if self.gender == 'pria'    :
            bbi = 0.9 * (self.tb - 100)
        
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.gender == 'pria'    : 
            bmr = 1 * 24 * bbi
        
        elif self.gender == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur= 0.1 * self.tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = self.aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda        
        karbohidrat  = (0.65 * total_energi)/4 
        
        return round(karbohidrat,2)



    def cairan(self):
        if self.gender == 'pria':
            bbi = 0.9 * (self.tb - 100)
        elif self.gender == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        cairan = (bbi * 50)/1000
        
        return cairan
        

