# GIZI MIKRO
class gizimikro():
    
    def __init__(self, umur=13, gender='pria'):
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
            
        elif self.gender =='wanita' and self.umur < 13:
            vitamin_b3 = 12
            
        elif self.gender =='wanita' and self.umur > 12:
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
        if self.gender =='pria' and self.umur < 13:
            biotin = 20
        
        elif self.gender =='pria' and self.umur < 16:
            biotin = 25
            
        elif self.gender =='pria' and self.umur > 15:
            biotin = 30
            
        elif  self.gender =='wanita' and self.umur < 13:
            biotin = 20
            
        elif self.gender =='wanita' and self.umur < 16:
            biotin = 25
            
        else:
            biotin = 30
            
        return biotin
        
        
        
        
    def kolin(self):
        if self.gender =='pria' and self.umur < 13:
            kolin = 375
            
        elif self.gender =='pria' and self.umur > 12:
            kolin = 550
            
        elif self.gender =='wanita' and self.umur < 13:
            kolin = 375
            
        elif self.gender =='wanita' and self.umur < 16:
            kolin = 400
            
        elif self.gender =='wanita' and self.umur > 15:
            kolin = 425
            
        return kolin 
    
    
    
    
    def vitamin_c(self):
        if self.gender =='pria' and self.umur < 13:
            vitamin_c = 50
            
        elif self.gender =='pria' and self.umur < 16:
            vitamin_c = 75
            
        elif self.gender =='pria' and self.umur > 15:
            vitamin_c = 90
            
        elif self.gender =='wanita' and self.umur < 12:
            vitamin_c = 50
            
        elif self.gender =='wanita' and self.umur < 16:
            vitamin_c = 65 
            
        elif self.gender =='wanita' and self.umur > 15:
            vitamin_c = 75
            
        return vitamin_c 
    
    
    
    
    def kalsium(self):
        if self.gender =='pria' and self.umur < 19:
            kalsium = 1200
            
        elif self.gender =='pria' and self.umur < 50:
            kalsium = 1000
            
        elif self.gender =='pria' and self.umur > 49:
            kalsium = 1200
            
        elif self.gender =='wanita' and self.umur < 19:
            kalsium = 1200
            
        elif self.gender =='wanita' and self.umur < 50:
            kalsium = 1000
            
        elif self.gender =='wanita' and self.umur > 49:
            kalsium = 1200
             
        return kalsium
    
    
    
    
    def fosfor(self):
        if self.gender =='pria' and self.umur < 19:
            fosfor = 1250
            
        elif self.gender =='pria' and self.umur > 18:
            fosfor = 700
            
        elif self.gender =='wanita' and self.umur < 19:
            fosfor = 1250
            
        elif self.gender =='wanita' and self.umur > 18:
            fosfor = 700
            
        return fosfor
    
    
    
    
    def magnesium(self):
        if self.gender =='pria' and self.umur < 13:
            magnesium = 160
            
        elif self.gender =='pria' and self.umur < 16:
            magnesium = 225
            
        elif self.gender =='pria' and self.umur < 19:
            magnesium = 270
            
        elif self.gender =='pria' and self.umur < 65:
            magnesium = 360
            
        elif self.gender =='pria' and self.umur > 64:
            magnesium = 350
            
        elif self.gender =='wanita' and self.umur < 13:
            magnesium = 170
            
        elif self.gender =='wanita' and self.umur < 16:
            magnesium =  220
            
        elif self.gender =='wanita' and self.umur < 19:
            magnesium = 230
            
        elif self.gender =='wanita' and self.umur < 30:
            magnesium = 330
            
        elif self.gender =='wanita' and self.umur < 65:
            magnesium = 340
            
        elif self.gender =='wanita' and self.umur > 64:
            magnesium = 320
        
        return magnesium
    
    
    
    
    def besi(self):
        if self.gender =='pria' and self.umur < 13:
            besi = 8
        
        elif self.gender =='pria' and self.umur < 19:
            besi = 11
            
        elif self.gender =='pria' and self.umur > 18:
            besi = 9 
            
        elif self.gender =='wanita' and self.umur < 13:
            besi = 8
            
        elif self.gender =='wanita' and self.umur < 19:
            besi = 15
            
        elif self.gender =='wanita' and self.umur < 50: 
            besi = 18
            
        elif self.gender =='wanita' and self.umur > 49:
            besi = 8
    
        return besi  
    
    
    
    
    def iodium(self):
        if self.gender =='pria' and self.umur < 13:
            iodium = 120
            
        elif self.gender =='pria' and self.umur > 12:
            iodium = 150
            
        elif self.gender =='wanita' and self.umur < 13:
            iodium = 120
            
        elif self.gender =='wanita' and self.umur > 12:
            iodium = 150
            
        return iodium 
    
    
    
    
    def seng(self):
        if self.gender =='pria' and self.umur < 13:
            seng = 8
            
        elif self.gender =='pria' and self.umur > 12:
            seng  = 11
            
        elif self.gender =='wanita' and self.umur < 13:
            seng = 8
            
        elif self.gender =='wanita' and self.umur < 19:
            seng = 9 
        
        elif self.gender =='wanita' and self.umur > 18:
            seng = 8
            
        return seng
    
    
    
    
    def selenium(self):
        if self.gender =='pria' and self.umur < 13:
            selenium = 22
            
        elif self.gender =='pria' and self.umur < 16:
            selenium = 30
            
        elif self.gender =='pria' and self.umur < 19:
            selenium = 36
            
        elif self.gender =='pria' and self.umur < 65:
            selenium = 30
            
        elif self.gender =='pria' and self.umur > 64:
            selenium = 29
            
        elif self.gender =='wanita' and self.umur < 13:
            selenium = 19
            
        elif self.gender =='wanita' and self.umur < 16:
            selenium = 24
            
        elif self.gender =='wanita' and self.umur < 19:
            selenium = 26
            
        elif self.gender == 'wanita' and self.umur < 30:
            selenium = 24
            
        elif self.gender =='wanita' and self.umur < 65:
            selenium = 25
            
        elif self.gender =='wanita' and self.umur > 64:
            selenium = 24 
            
        return selenium
    
    
    
    
    def mangan(self):
        if self.gender =='pria' and self.umur < 13:
            mangan = 1.9
            
        elif self.gender =='pria' and self.umur < 16:
            mangan = 2.2
        
        elif self.gender =='pria' and self.umur > 15:
            mangan = 2.3
            
        elif self.gender =='wanita' and self.umur < 16:
            mangan = 1.6
            
        elif self.gender =='wanita' and self.umur > 15:
            mangan = 1.8
            
        return mangan 
    
    
    
    
    def fluor(self):
        if self.gender =='pria' and self.umur < 13:
            fluor = 1.8
            
        elif self.gender =='pria' and self.umur < 16:
            fluor = 2.5
            
        elif self.gender =='pria' and self.umur > 15:
            fluor = 4.0
            
        elif self.gender =='wanita' and self.umur < 13:
            fluor = 1.9
            
        elif self.gender =='wanita' and self.umur < 16:
            fluor = 2.4
            
        elif self.gender =='wanita' and self.umur > 15:
            fluor = 3.0
            
        return fluor  
    
    
    
    
    def kromium(self):
        if self.gender =='pria' and self.umur < 13:
            kromium = 28
            
        elif self.gender =='pria' and self.umur < 16:
            kromium = 36
            
        elif self.gender =='pria' and self.umur < 19:
            kromium = 41
            
        elif self.gender == 'pria' and self.umur < 30:
            kromium = 36
            
        elif self.gender =='pria' and self.umur < 50:
            kromium = 34
            
        elif self.gender =='pria' and self.umur < 65:
            kromium = 29
            
        elif self.gender =='pria' and self.umur < 81:
            kromium = 24
            
        elif self.gender =='pria' and self.umur > 80:
            kromium = 21 
        
        if self.gender =='wanita' and self.umur < 13:
            kromium = 26
            
        elif self.gender =='wanita' and self.umur < 16:
            kromium = 27
            
        elif self.gender =='wanita' and self.umur < 19:
            kromium = 29
            
        elif self.gender == 'wanita' and self.umur < 30:
            kromium = 30
            
        elif self.gender =='wanita' and self.umur < 50:
            kromium = 29
            
        elif self.gender =='wanita' and self.umur < 65:
            kromium = 24
            
        elif self.gender =='wanita' and self.umur < 81:
            kromium = 21
            
        elif self.gender =='wanita' and self.umur > 80:
            kromium = 19 
               
        return kromium    
               
               
               
               
    def kalium(self):
        if self.gender =='pria' and self.umur < 13:
            kalium = 3900
            
        elif self.gender =='pria' and self.umur < 16:
            kalium = 4800
        
        elif self.gender =='pria' and self.umur < 19:
            kalium = 5300
            
        elif self.gender =='pria' and self.umur > 18:
            kalium = 4700
            
        elif self.gender =='wanita' and self.umur < 13:
            kalium = 4400
            
        elif self.gender =='wanita' and self.umur < 16:
            kalium = 4800
            
        elif self.gender =='wanita' and self.umur < 19:
            kalium = 5000
            
        elif self.gender =='wanita' and self.umur > 18:
            kalium = 4700
            
        return kalium
    
    
    
    
    def natrium(self):
        if self.gender =='pria' and self.umur < 13:
            natrium = 1300
            
        elif self.gender =='pria' and self.umur < 16:
            natrium = 1500
        
        elif self.gender =='pria' and self.umur < 19:
            natrium = 1700
            
        elif self.gender =='pria' and self.umur < 50:
            natrium = 1500
            
        elif self.gender =='pria' and  self.umur < 65:
            natrium = 1300
            
        elif self.gender =='pria' and self.umur < 81:
            natrium = 1100
            
        elif self.gender =='pria' and self.umur > 80:
            natrium = 1000
            
        elif self.gender =='wanita' and self.umur < 13:
            natrium = 1400
            
        elif self.gender =='wanita' and self.umur < 16:
            natrium = 1500
            
        elif self.gender =='wanita' and self.umur < 19:
            natrium = 1600
            
        elif self.gender =='wanita' and self.umur < 50:
            natrium = 1500
            
        elif self.gender =='wanita' and self.umur < 65:
            natrium = 1400
            
        elif self.gender =='wanita' and self.umur < 81:
            natrium = 1200
            
        elif self.gender =='wanita' and self.umur > 80:
            natrium = 1000
            
        return natrium       
    
    
    
    
    def klor(self):
        if self.gender =='pria' and self.umur < 13: 
            klor = 1900
            
        elif self.gender =='pria' and self.umur < 16:
            klor = 2300
            
        elif self.gender =='pria' and self.umur < 19:
            klor = 2500
            
        elif self.gender =='pria' and self.umur < 50:
            klor = 2250
            
        elif self.gender =='pria' and self.umur < 65:
            klor = 2100
            
        elif self.gender =='pria' and self.umur < 81:
            klor = 1900
            
        elif self.gender =='pria' and self.umur > 80:
            klor = 1600
            
        elif self.gender =='wanita' and self.umur < 13:
            klor = 2100
            
        elif self.gender =='wanita' and self.umur < 16:
            klor = 2300
            
        elif self.gender =='wanita' and self.umur < 19:
            klor = 2400
            
        elif self.gender =='wanita' and self.umur < 50:
            klor = 2250
            
        elif self.gender =='wanita' and self.umur < 65:
            klor = 2100
            
        elif self.gender =='wanita' and self.umur < 81:
            klor = 1900
            
        elif self.gender =='wanita' and self.umur > 80:
            klor = 1600
            
        return klor
            
            
            
            
    def tembaga(self):
        if self.gender =='pria' and self.umur < 13:
            tembaga = 700
            
        elif self.gender =='pria' and self.umur < 16:
            tembaga = 795
            
        elif self.gender =='pria' and self.umur < 19:
            tembaga = 890
            
        elif self.gender =='pria' and self.umur > 18:
            tembaga = 900
            
        elif self.gender =='wanita' and self.umur < 13:
            tembaga = 700
            
        elif self.gender =='wanita' and self.umur < 16:
            tembaga = 795
            
        elif self.gender =='wanita' and self.umur < 19:
            tembaga = 890
            
        elif self.gender =='wanita' and self.umur > 18:
            tembaga = 900
            
        return tembaga
# AKHIR GIZI MIKRO
    
    
# GIZI MIKRO IBU HAMIL
class gizimikro_hamil():
    def __init__(self, umur, trimester):
        self.umur = umur 
        self.trimester = trimester
        
    
    def vitamin_a(self):
        if self.trimester == 'Trimester 1':
            vitamin_a = gizimikro(umur=self.umur, gender='wanita').vitamin_a()
            vitamin_a = vitamin_a + 300
        
        elif self.trimester == 'Trimester 2':
            vitamin_a = gizimikro(umur=self.umur, gender='wanita').vitamin_a()
            vitamin_a = vitamin_a + 300
        
        elif self.trimester == 'Trimester 3':
            vitamin_a = gizimikro(umur=self.umur, gender='wanita').vitamin_a()
            vitamin_a = vitamin_a + 300
            
        return vitamin_a
        
        
        
        
    def vitamin_d(self):
        if self.trimester == 'Trimester 1':
            vitamin_d = gizimikro(umur=self.umur, gender='wanita').vitamin_d()
            vitamin_d = vitamin_d 
        
        elif self.trimester == 'Trimester 2':
            vitamin_d = gizimikro(umur=self.umur, gender='wanita').vitamin_d()
            vitamin_d = vitamin_d 
        
        elif self.trimester == 'Trimester 3':
            vitamin_d = gizimikro(umur=self.umur, gender='wanita').vitamin_d()
            vitamin_d = vitamin_d 
        
        return vitamin_d
    
    
    
        
    def vitamin_e(self):
        if self.trimester == 'Trimester 1':
            vitamin_e = gizimikro(umur=self.umur, gender='wanita').vitamin_e()
            vitamin_e = vitamin_e 
        
        elif self.trimester == 'Trimester 2':
            vitamin_e = gizimikro(umur=self.umur, gender='wanita').vitamin_e()
            vitamin_e = vitamin_e 
        
        elif self.trimester == 'Trimester 3':
            vitamin_e = gizimikro(umur=self.umur, gender='wanita').vitamin_e()
            vitamin_e = vitamin_e 
        
        return vitamin_e
    
    
    
    
    def vitamin_k(self):
        if self.trimester == 'Trimester 1':
            vitamin_k = gizimikro(umur=self.umur, gender='wanita').vitamin_k()
            vitamin_k = vitamin_k 
        
        elif self.trimester == 'Trimester 2':
            vitamin_k = gizimikro(umur=self.umur, gender='wanita').vitamin_k()
            vitamin_k = vitamin_k 
        
        elif self.trimester == 'Trimester 3':
            vitamin_k = gizimikro(umur=self.umur, gender='wanita').vitamin_k()
            vitamin_k = vitamin_k 
        
        return vitamin_k
    
    
    
    def vitamin_b1(self):
        if self.trimester == 'Trimester 1':
            vitamin_b1 = gizimikro(umur=self.umur, gender='wanita').vitamin_b1()
            vitamin_b1 = vitamin_b1 + 0.3 
        
        elif self.trimester == 'Trimester 2':
            vitamin_b1 = gizimikro(umur=self.umur, gender='wanita').vitamin_b1()
            vitamin_b1 = vitamin_b1 + 0.3
        
        elif self.trimester == 'Trimester 3':
            vitamin_b1 = gizimikro(umur=self.umur, gender='wanita').vitamin_b1()
            vitamin_b1 = vitamin_b1 + 0.3
        
        return round(vitamin_b1,2)
    
    
    
    
    def vitamin_b2(self):
        if self.trimester == 'Trimester 1':
            vitamin_b2 = gizimikro(umur=self.umur, gender='wanita').vitamin_b2()
            vitamin_b2 = vitamin_b2 + 0.3 
        
        elif self.trimester == 'Trimester 2':
            vitamin_b2 = gizimikro(umur=self.umur, gender='wanita').vitamin_b2()
            vitamin_b2 = vitamin_b2 + 0.3
        
        elif self.trimester == 'Trimester 3':
            vitamin_b2 = gizimikro(umur=self.umur, gender='wanita').vitamin_b2()
            vitamin_b2 = vitamin_b2 + 0.3
        
        return round(vitamin_b2,2)
    
    
    
    
    def vitamin_b3(self):
        if self.trimester == 'Trimester 1':
            vitamin_b3 = gizimikro(umur=self.umur, gender='wanita').vitamin_b3()
            vitamin_b3 = vitamin_b3 + 4 
        
        elif self.trimester == 'Trimester 2':
            vitamin_b3 = gizimikro(umur=self.umur, gender='wanita').vitamin_b3()
            vitamin_b3 = vitamin_b3 + 4
        
        elif self.trimester == 'Trimester 3':
            vitamin_b3 = gizimikro(umur=self.umur, gender='wanita').vitamin_b3()
            vitamin_b3 = vitamin_b3 + 4
        
        return round(vitamin_b3,2)
    
    
    
    
    def vitamin_b5(self):
        if self.trimester == 'Trimester 1':
            vitamin_b5 = gizimikro(umur=self.umur, gender='wanita').vitamin_b5()
            vitamin_b5 = vitamin_b5 + 1 
        
        elif self.trimester == 'Trimester 2':
            vitamin_b5 = gizimikro(umur=self.umur, gender='wanita').vitamin_b5()
            vitamin_b5 = vitamin_b5 + 1
        
        elif self.trimester == 'Trimester 3':
            vitamin_b5 = gizimikro(umur=self.umur, gender='wanita').vitamin_b5()
            vitamin_b5 = vitamin_b5 + 1
    
        return round(vitamin_b5,2)
    
    
    
    
    def vitamin_b6(self):
        if self.trimester == 'Trimester 1':
            vitamin_b6 = gizimikro(umur=self.umur, gender='wanita').vitamin_b6()
            vitamin_b6 = vitamin_b6 + 0.6 
        
        elif self.trimester == 'Trimester 2':
            vitamin_b6 = gizimikro(umur=self.umur, gender='wanita').vitamin_b6()
            vitamin_b6 = vitamin_b6 + 0.6
        
        elif self.trimester == 'Trimester 3':
            vitamin_b6 = gizimikro(umur=self.umur, gender='wanita').vitamin_b6()
            vitamin_b6 = vitamin_b6 + 0.6
    
        return round(vitamin_b6,2)




    def vitamin_b12(self):
        if self.trimester == 'Trimester 1':
            vitamin_b12 = gizimikro(umur=self.umur, gender='wanita').vitamin_b12()
            vitamin_b12 = vitamin_b12 + 0.5 
        
        elif self.trimester == 'Trimester 2':
            vitamin_b12 = gizimikro(umur=self.umur, gender='wanita').vitamin_b12()
            vitamin_b12 = vitamin_b12 + 0.5
        
        elif self.trimester == 'Trimester 3':
            vitamin_b12 = gizimikro(umur=self.umur, gender='wanita').vitamin_b12()
            vitamin_b12 = vitamin_b12 + 0.5
    
        return round(vitamin_b12,2)




    def folat(self):
        if self.trimester == 'Trimester 1':
            folat = gizimikro(umur=self.umur, gender='wanita').folat()
            folat = folat + 200 
        
        elif self.trimester == 'Trimester 2':
            folat = gizimikro(umur=self.umur, gender='wanita').folat()
            folat = folat + 200
        
        elif self.trimester == 'Trimester 3':
            folat = gizimikro(umur=self.umur, gender='wanita').folat()
            folat = folat + 200
    
        return round(folat,2)




    def biotin(self):
        if self.trimester == 'Trimester 1':
            biotin = gizimikro(umur=self.umur, gender='wanita').biotin()
            biotin = biotin  
        
        elif self.trimester == 'Trimester 2':
            biotin = gizimikro(umur=self.umur, gender='wanita').biotin()
            biotin = biotin 
        
        elif self.trimester == 'Trimester 3':
            biotin = gizimikro(umur=self.umur, gender='wanita').biotin()
            biotin = biotin 
        
        return biotin    
        
        
        
        
    def kolin(self):    
        if self.trimester == 'Trimester 1':
            kolin = gizimikro(umur=self.umur, gender='wanita').kolin()
            kolin = kolin + 25 
        
        elif self.trimester == 'Trimester 2':
            kolin = gizimikro(umur=self.umur, gender='wanita').kolin()
            kolin = kolin + 25
        
        elif self.trimester == 'Trimester 3':
            kolin = gizimikro(umur=self.umur, gender='wanita').kolin()
            kolin = kolin + 25
            
        return kolin
            
            
            
            
    def vitamin_c(self):    
        if self.trimester == 'Trimester 1':
            vitamin_c = gizimikro(umur=self.umur, gender='wanita').vitamin_c()
            vitamin_c = vitamin_c + 10 
        
        elif self.trimester == 'Trimester 2':
            vitamin_c = gizimikro(umur=self.umur, gender='wanita').vitamin_c()
            vitamin_c = vitamin_c + 10
        
        elif self.trimester == 'Trimester 3':
            vitamin_c = gizimikro(umur=self.umur, gender='wanita').vitamin_c()
            vitamin_c = vitamin_c + 10

        return vitamin_c
    
    
    
    
    def kalsium(self):
        if self.trimester =='Trimester 1':
            kalsium = gizimikro(umur=self.umur, gender='wanita').kalsium()
            kalsium = kalsium + 200
            
        elif self.trimester =='Trimester 2':
            kalsium = gizimikro(umur=self.umur, gender='wanita').kalsium()
            kalsium = kalsium + 200

        elif self.trimester =='Trimester 3':
            kalsium = gizimikro(umur=self.umur, gender='wanita').kalsium()
            kalsium = kalsium + 200
            
        return kalsium




    def fosfor(self):
        if self.trimester =='Trimester 1':
            fosfor = gizimikro(umur=self.umur, gender='wanita').fosfor()
            fosfor = fosfor 
            
        elif self.trimester =='Trimester 2':
            fosfor = gizimikro(umur=self.umur, gender='wanita').fosfor()
            fosfor = fosfor 

        elif self.trimester =='Trimester 3':
            fosfor = gizimikro(umur=self.umur, gender='wanita').fosfor()
            fosfor = fosfor 
            
        return fosfor
    
    
    
    
    def magnesium(self):
        if self.trimester =='Trimester 1':
            magnesium = gizimikro(umur=self.umur, gender='wanita').magnesium()
            magnesium = magnesium 
            
        elif self.trimester =='Trimester 2':
            magnesium = gizimikro(umur=self.umur, gender='wanita').magnesium()
            magnesium = magnesium 

        elif self.trimester =='Trimester 3':
            magnesium = gizimikro(umur=self.umur, gender='wanita').magnesium()
            magnesium = magnesium 
            
        return magnesium
    
    
    
    
    def besi(self):
        if self.trimester =='Trimester 1':
            besi =  gizimikro(umur=self.umur, gender='wanita').besi()
            besi =  besi 
            
        elif self.trimester =='Trimester 2':
            besi =  gizimikro(umur=self.umur, gender='wanita').besi()
            besi =  besi + 9

        elif self.trimester =='Trimester 3':
            besi =  gizimikro(umur=self.umur, gender='wanita').besi()
            besi =  besi + 9
            
        return besi
    
    
    
    
    def iodium(self):
        if self.trimester =='Trimester 1':
            iodium = gizimikro(umur=self.umur, gender='wanita').iodium()
            iodium = iodium + 70
            
        elif self.trimester =='Trimester 2':
            iodium = gizimikro(umur=self.umur, gender='wanita').iodium()
            iodium = iodium + 70

        elif self.trimester =='Trimester 3':
            iodium = gizimikro(umur=self.umur, gender='wanita').iodium()
            iodium = iodium + 70
            
        return iodium
    
    
    
    
    def seng(self):
        if self.trimester =='Trimester 1':
            seng = gizimikro(umur=self.umur, gender='wanita').seng()
            seng = seng + 2
            
        elif self.trimester =='Trimester 2':
            seng = gizimikro(umur=self.umur, gender='wanita').seng()
            seng = seng + 4

        elif self.trimester =='Trimester 3':
            seng = gizimikro(umur=self.umur, gender='wanita').seng()
            seng = seng + 4
            
        return seng
    
    
    
    
    def selenium(self):
        if self.trimester =='Trimester 1':
            selenium =  gizimikro(umur=self.umur, gender='wanita').selenium()
            selenium =  selenium + 5
            
        elif self.trimester =='Trimester 2':
            selenium =  gizimikro(umur=self.umur, gender='wanita').selenium()
            selenium =  selenium + 5

        elif self.trimester =='Trimester 3':
            selenium =  gizimikro(umur=self.umur, gender='wanita').selenium()
            selenium =  selenium + 5
            
        return selenium
    
    
    
    
    def mangan(self):
        if self.trimester =='Trimester 1':
            mangan = gizimikro(umur=self.umur, gender='wanita').mangan()
            mangan = mangan + 0.2
            
        elif self.trimester =='Trimester 2':
            mangan = gizimikro(umur=self.umur, gender='wanita').mangan()
            mangan = mangan + 0.2

        elif self.trimester =='Trimester 3':
            mangan = gizimikro(umur=self.umur, gender='wanita').mangan()
            mangan = mangan + 0.2
            
        return mangan
 
 
 
 
    def fluor(self):
        if self.trimester =='Trimester 1':
            fluor = gizimikro(umur=self.umur, gender='wanita').fluor()
            fluor = fluor 
            
        elif self.trimester =='Trimester 2':
            fluor = gizimikro(umur=self.umur, gender='wanita').fluor()
            fluor = fluor 

        elif self.trimester =='Trimester 3':
            fluor = gizimikro(umur=self.umur, gender='wanita').fluor()
            fluor = fluor 
            
        return fluor
    
    
    
    
    def kromium(self):
        if self.trimester =='Trimester 1':
            kromium = gizimikro(umur=self.umur, gender='wanita').kromium()
            kromium = kromium + 5 
            
        elif self.trimester =='Trimester 2':
            kromium = gizimikro(umur=self.umur, gender='wanita').kromium()
            kromium = kromium + 5

        elif self.trimester =='Trimester 3':
            kromium = gizimikro(umur=self.umur, gender='wanita').kromium()
            kromium = kromium + 5
            
        return kromium
    
    
    
    
    def kalium(self):
        if self.trimester =='Trimester 1':
            kalium = gizimikro(umur=self.umur, gender='wanita').kalium()
            kalium = kalium 
            
        elif self.trimester =='Trimester 2':
            kalium = gizimikro(umur=self.umur, gender='wanita').kalium()
            kalium = kalium

        elif self.trimester =='Trimester 3':
            kalium = gizimikro(umur=self.umur, gender='wanita').kalium()
            kalium = kalium
            
        return kalium
    
    
    
    
    def natrium(self):
        if self.trimester =='Trimester 1':
            natrium = gizimikro(umur=self.umur, gender='wanita').natrium()
            natrium = natrium 
            
        elif self.trimester =='Trimester 2':
            natrium = gizimikro(umur=self.umur, gender='wanita').natrium()
            natrium = natrium

        elif self.trimester =='Trimester 3':
            natrium = gizimikro(umur=self.umur, gender='wanita').natrium()
            natrium = natrium
            
        return natrium
    
    
    
    
    def klor(self):
        if self.trimester =='Trimester 1':
            klor = gizimikro(umur=self.umur, gender='wanita').klor()
            klor = klor 
            
        elif self.trimester =='Trimester 2':
            klor = gizimikro(umur=self.umur, gender='wanita').klor()
            klor = klor

        elif self.trimester =='Trimester 3':
            klor = gizimikro(umur=self.umur, gender='wanita').klor()
            klor = klor
            
        return klor
    
    
    
    
    def tembaga(self):
        if self.trimester =='Trimester 1':
            tembaga = gizimikro(umur=self.umur, gender='wanita').tembaga()
            tembaga = tembaga + 100 
            
        elif self.trimester =='Trimester 2':
            tembaga = gizimikro(umur=self.umur, gender='wanita').tembaga()
            tembaga = tembaga + 100

        elif self.trimester =='Trimester 3':
            tembaga = gizimikro(umur=self.umur, gender='wanita').tembaga()
            tembaga = tembaga + 100
            
        return tembaga
    
# AKHIR GIZI MIKRO IBU HAMIL



#GIZI MIKRO IBU MENYUSUI

class gizimikro_menyusui():
    def __init__(self, umur, siklus):
        self.umur = umur
        self.siklus = siklus
        
    def vitamin_a(self):
        vitamin_a = gizimikro(umur=self.umur, gender='wanita').vitamin_a()
        vitamin_a = vitamin_a + 350
        return vitamin_a
    
    def vitamin_d(self):
        return gizimikro(umur=self.umur, gender='wanita').vitamin_d()
    
    def vitamin_e(self):
        vitamin_e = gizimikro(umur=self.umur, gender='wanita').vitamin_e()
        vitamin_e = vitamin_e + 4
        return vitamin_e
    
    def vitamin_k(self):
        return gizimikro(umur=self.umur, gender='wanita').vitamin_k()
    
    def vitamin_b1(self):
        vitamin_b1 = gizimikro(umur=self.umur, gender='wanita').vitamin_b1()
        vitamin_b1 = vitamin_b1 + 0.4
        return vitamin_b1
    
    def vitamin_b2(self):
        vitamin_b2 = gizimikro(umur=self.umur, gender='wanita').vitamin_b2()
        vitamin_b2 = vitamin_b2 + 0.5
        return vitamin_b2
     
    def vitamin_b3(self):
        vitamin_b3 = gizimikro(umur=self.umur, gender='wanita').vitamin_b3()
        vitamin_b3 = vitamin_b3 + 3 
        return vitamin_b3
    
    def vitamin_b5(self):
        vitamin_b5 = gizimikro(umur=self.umur, gender='wanita').vitamin_b5()
        vitamin_b5 = vitamin_b5 + 2 
        return vitamin_b5
    
    def vitamin_b6(self):
        vitamin_b6 = gizimikro(umur=self.umur, gender='wanita').vitamin_b6()
        vitamin_b6 = vitamin_b6 + 0.6
        return vitamin_b6
    
    def vitamin_b12(self):
        vitamin_b12 = gizimikro(umur=self.umur, gender='wanita').vitamin_b12()
        vitamin_b12 = vitamin_b12 + 1.0
        return vitamin_b12
    
    def folat(self):
        folat = gizimikro(umur=self.umur, gender='wanita').folat()  
        folat = folat + 100
        return folat 
    
    def biotin(self):
        biotin = gizimikro(umur=self.umur, gender='wanita').biotin() 
        biotin =  biotin + 5
        return biotin
    
    def kolin(self):
        kolin = gizimikro(umur=self.umur, gender='wanita').kolin() 
        kolin =  kolin + 125
        return kolin
    
    def vitamin_c(self):
        vitamin_c = gizimikro(umur=self.umur, gender='wanita').vitamin_c()
        vitamin_c = vitamin_c + 45
        return vitamin_c
    
    def kalsium(self):
        kalsium = gizimikro(umur=self.umur, gender='wanita').kalsium()
        kalsium = kalsium + 200
        return kalsium
    
    def fosfor(self):
        return gizimikro(umur=self.umur, gender='wanita').fosfor()
    
    def magnesium(self):
        return gizimikro(umur=self.umur, gender='wanita').magnesium()
    
    def besi(self):
        return gizimikro(umur=self.umur, gender='wanita').besi()
    
print(gizimikro_hamil(umur=18, trimester='Trimester 2').tembaga())
