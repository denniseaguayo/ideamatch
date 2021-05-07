import MySQLdb
import random



def insert(conn, query, i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19):
    cursor = conn.cursor()
    cursor.execute(query,(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19)) 
    conn.commit()

#def selectAll(conn, query):
 #   cursor = conn.cursor()
  #  cursor.execute(query)
   # rows = cursor.fetchall()
    #return rows


def main():
   
    conn =  MySQLdb.connect('remotemysql.com','jAFoXk1z8p','DOZwJcdGpZ','jAFoXk1z8p')
    print('succefull connection')
    check = True
    while(check == True):
        print('0-exit')
        print('1-Registrazione')
        print('2-login')
         
        sel = int(input('inserie opzione: '))
        
        if sel == 0 :
            print('uscita')
            check = False
           
        elif sel == 1:
          
            i=0
            p=0
            while i==0:
                email= input("inserisci email ")
                emailControllo= input("Conferma email ")
                while p==0 :
                    if (email==emailControllo):
                        pw=input("inserisci password")
                        pwControllo=input("Conferma password")
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

            t=input("Vuoi essere cliente (C) o lavoratore (L)?")
            cf = input('inserisci Codice fiscale: ')
            nome = input('inserisci nome: ')
            cognome = input('inserisci cognome ')
            eta = input('inserisci età: ')
            dataNascita = input('inserisci data nascita [aaaammgg]: ')
            luogoNascita = input('inserisci luogo di nascita: ')
            indirizzo = input('inserisci indirizzo: ')
            sesso = input('inserisci sesso: ')
            cartaIdentita = input('inserisci carta di identità: ')
            tel = input('inserisci numero telefonico: ')
            nazionalita = input('inserisci nazionalità: ')
            tipo=t
            
          

            if(t=="C"):
                q = "insert into utente values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                insert(conn, q,cf,nome,cognome,eta,dataNascita,luogoNascita,indirizzo,sesso,cartaIdentita,tel,nazionalita,tipo,email,pw,'null','null','null','null','null') 
                
            elif(t=="L"):  
                
                colCap = input('inserisci colore capelli: ')
                colOcc = input('inserisci colore occhi: ')
                altezza = input('inserisci altezza: ')
                peso = input('inserisci peso: ')
                tipoCap = input('inserisci tipo capelli: ')
                
                q = "insert into utente values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                insert(conn, q,cf,nome,cognome,eta,dataNascita,luogoNascita,indirizzo,sesso,cartaIdentita,tel,nazionalita,tipo,email,pw,colCap,colOcc,altezza,peso,tipoCap)      
            #selectAll(conn, q)
       
            
main()