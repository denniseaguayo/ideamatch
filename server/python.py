import mysqli as pys
import random

def insert8(conn, query, i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17):
    cursor = conn.cursor()
    cursor.execute(query,(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17)) 
    conn.commit()

def main():
   
    conn =  pys.connect(server = 'remotemysql.com', user = 'jAFoXk1z8p', password = 'DOZwJcdGpZ', database  = 'jAFoXk1z8p')
    print('succefull connection')
    check = True
    while(check == True):
        print('0-exit')
        print('1-Registrazione')
         
        sel = int(input('inserie opzione: '))
        
        if sel == 0 :
            print('uscita')
            check = False
           
        elif sel == 1:
            t=input("Vuoi essere cliente (C) o lavoratore (L)?")
            if(s=="C"):
                cf             = input('inserisci Codice fiscale: ')
                nome       = input('inserisci nome: ')
                cognome = input('inserisci cognome ')
                eta           = int(input('inserisci età: '))
                dataNascita           = input('inserisci data nascita [aaaammgg]: ')
                luogoNasita = input('inserisci luogo di nascita: ')
                indirizzo      = input('inserisci indirizzo: ')
                sesso          = input('inserisci sesso: ')
                cartaIdentita   = input('inserisci carta di identità: ')
                tel          = input('inserisci numero telefonico: ')
                nazionalita          = input('inserisci nazionalità: ')
                tipo=t
                
            else:  
                cf             = input('inserisci Codice fiscale: ')
                nome       = input('inserisci nome: ')
                cognome = input('inserisci cognome ')
                eta           = int(input('inserisci età: '))
                dataNascita           = input('inserisci data nascita [aaaammgg]: ')
                luogoNasita = input('inserisci luogo di nascita: ')
                indirizzo      = input('inserisci indirizzo: ')
                sesso          = input('inserisci sesso: ')
                cartaIdentita   = input('inserisci carta di identità: ')
                tel          = input('inserisci numero telefonico: ')
                nazionalita          = input('inserisci nazionalità: ')
                tipo=t
                colCap      = input('inserisci indirizzo: ')
                colOcc          = input('inserisci sesso: ')
                altezza  = input('inserisci carta di identità: ')
                peso          = float(input('inserisci numero telefonico: '))
                tipoCap          = input('inserisci nazionalità: ')

            q = "insert into utente values(%s,%s,%s,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%f,%s)"
            insert8(conn, q,cf,nome,cognome,eta,dataNascita,luogoNascita,indirizzo,sesso,cartaIdentita,tel,nazionalita,tipo,colCap,colOcc,altezza,peso,tipoCap)      
        
       
            
main()