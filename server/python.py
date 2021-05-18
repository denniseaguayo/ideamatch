import MySQLdb
import random
from codicefiscale import codicefiscale

'''
npm i 
npm i cors
pip install python-codicefiscale
pip install MySQL

python python.py

'''

def insert(query, i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19):
    conn =  MySQLdb.connect('remotemysql.com','iF0nI0tX1B','DbGYu5wcRW','iF0nI0tX1B')
    cursor = conn.cursor()
    cursor.execute(query,(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19)) 
    conn.commit()
    conn.close()

def insert3(query, i1,i2,i3,i4,i5,i6,i7,i8):
    conn =  MySQLdb.connect('remotemysql.com','iF0nI0tX1B','DbGYu5wcRW','iF0nI0tX1B')
    cursor = conn.cursor()
    cursor.execute(query,(i1,i2,i3,i4,i5,i6,i7,i8)) 
    conn.commit()
    conn.close()



def selectAll(query):
    conn =  MySQLdb.connect('remotemysql.com','iF0nI0tX1B','DbGYu5wcRW','iF0nI0tX1B')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def selectWhere(query, codice):
    conn =  MySQLdb.connect('remotemysql.com','iF0nI0tX1B','DbGYu5wcRW','iF0nI0tX1B')
    cursor = conn.cursor()
    cursor.execute(query,codice)
    row = cursor.fetchone()
    return row 
    conn.close()



def main():
   
    
    print('succefull connection')
    check = True
    while(check == True):
        print('0-exit')
        print('1-Registrazione')
        print('2-login')
        print('3-richiesta')
         
        sel = int(input('inserie opzione: '))
        
        if sel == 0 :
            print('uscita')
            check = False
           
        elif sel == 1:
          
            i=0
            p=0
            while i==0:
                email= input("inserisci email: ")
                emailControllo= input("Conferma email: ")
                while p==0 :
                    if (email==emailControllo):
                        pw=input("inserisci password: ")
                        pwControllo=input("Conferma password: ")
                        if(pw==pwControllo):
                            print("Credenziali corrette")
                            i=1
                            p=1
                        else:
                            print("le password non corrispondono")
                            pw=''
                            pwControllo=''
                            p=0
                    else:
                        print("l'email inserita non corrisponde")
                        email=''
                        emailControllo=''
                        i=0
                        p=1

            t=input("Vuoi essere cliente (C) o lavoratore (L)? ")
            cf = input('inserisci Codice fiscale: ')
            nome = input('inserisci nome: ')
            cognome = input('inserisci cognome: ')
            eta = input('inserisci età: ')
            dataNascita = input('inserisci data nascita [aaaammgg]: ')
            luogoNascita = input('inserisci luogo di nascita: ')
            indirizzo = input('inserisci indirizzo: ')
            sesso = input('inserisci sesso: ')
            cartaIdentita = input('inserisci carta di identità: ')
            tel = input('inserisci numero telefonico: ')
            nazionalita = input('inserisci nazionalità: ')
            tipo=t
            c=0
            contolloCF=''
        
            
            while c==0:
                contolloCF=codicefiscale.encode(surname=cognome, name=nome, sex=sesso, birthdate=dataNascita, birthplace=luogoNascita)
                if(cf==contolloCF):
                    c=1
                else:
                    print("il codice fiscale inserito è ERRATO")
                    cf=input("inserisci Codice fiscale:")
                    c=0
            print("I dati inseriti sono CORRETTI")
            if(t=="C"):
                q = "insert into utente values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                insert(q,cf,nome,cognome,eta,dataNascita,luogoNascita,indirizzo,sesso,cartaIdentita,tel,nazionalita,email,pw,tipo,'null','null','null','null','null') 
                
            elif(t=="L"):  
                
                colCap = input('inserisci colore capelli: ')
                colOcc = input('inserisci colore occhi: ')
                altezza = input('inserisci altezza: ')
                peso = input('inserisci peso: ')
                tipoCap = input('inserisci tipo capelli: ')
                
                q = "insert into utente values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                insert(q,cf,nome,cognome,eta,dataNascita,luogoNascita,indirizzo,sesso,cartaIdentita,tel,nazionalita,email,pw,tipo,colCap,colOcc,altezza,peso,tipoCap)      
       

        if sel == 3 :
    
            cfCliente=input("inserisci codice fiscale: ")
            codice=selectAll("select cf from utente where tipo='C'")
            print(codice) 
          

     
            for i in codice:
                for codiceR in range(len(codice)):
                    print(codiceR)
                    print('inserisci le caratteristiche che vuoi che abbia la persona che cerchi')
                    colOcchi=input("inserisci colore occhi: ")
                    colCapelli=input("inserisci colore capelli: ")
                    tipoCapelli=input("inserisci il tipo di capelli: ")
                    pesoRichiesta=input("inserisci peso: ")
                    altezzaRichiesta=input("inserisci altezza: ")
                    naz=input("inserisci nazionalita: ")
                    insert3("insert into richiesta values(%d,%s,%s,%s,%s,%s,%s,%s)",codiceR,colOcchi,colCapelli,tipoCapelli,naz,pesoRichiesta,altezzaRichiesta,cfCliente) 
                    #print(selectAll("select cfLavoratore from richiesta,utente where colOcchi=colOcc or colCapelli=colCap or tipoCapelli=tipoCap or pesoRichiesta=peso or altezzaRichiesta=altezza or naz=nazionalita"))
                
        
                

            
                
main()