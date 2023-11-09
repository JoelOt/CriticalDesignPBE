from tkinter import ttk
from tkinter import *
import requests
import json

class Product:
    def __init__(self, window): #definim la nostre finestra. li anirem afegint variables amb self.aaa   (sekf es el this de java) 
        self.wind = window
        self.wind.title('Aplicacó de productes')
        
        #frame
        frame = LabelFrame(self.wind, text = 'registrar un nou producte')  #creem un frame on hi posarem coses. (self.wind: a la nostra finestra, text: que s'hi mostra)
        frame.grid(row= 0, column=0, columnspan= 3, pady= 20)  #per colocar el frame on volguem. (files, columnes, cols vuides al inici, relleno vertical en pixels pk els seguents elements no es veiguin tant junts ) 
    
        #name input
        Label(frame, text = 'Nom : ').grid(row= 1, column= 0) #fem una etiqueta perque l'usuari entri dades
        self.nom = Entry(frame) #fem que l'usuari entri dades i ho guardem a la variable name per poder manipular-la
        self.nom.focus() #fa que el cursos comenci ya colocat per escriure a nom
        self.nom.grid(row= 1, column= 1)
        
        #price input
        Label(frame, text = 'Preu : ').grid(row= 2, column= 2)
        self.preu = Entry(frame) 
        self.preu.grid(row= 2, column= 3)
        
        
        #Taula
        self.tree = ttk.Treeview(height= 10, columns= 2) #es una taula de dades de 10 pixels d'altura i 2 columnes guardada a la variable tree
        self.tree.grid(row= 4, column=0 , columnspan= 2)
        self.tree.heading('#0', text = 'Nom', anchor= CENTER) #capçalera de la primera columna de caselles (indicata primera en #0). anchor = center vol dir que la capçalera esta centrada
        self.tree.heading('#1', text= 'Preu', anchor= CENTER) #una altra per la segona columna de caselles
        
        
        #Botó afegir producte:  command serveix per dir-li que ha de fer cada cop que es clica, ha d'estar en forma de funció
        ttk.Button(frame, text = 'Guardar producte', command=self.guardar_producte).grid(row= 3, columnspan= 2, sticky= W + E) #fem que al clicar-se cridi agreagar producte, per fer aquesta funció al clicar-se
                                                                                                                                 #sticky: desde on fins a on ocupa el botó, de oest (W) fins a est (E)
        #output msg:    volem fer un missatge que sols es mostri quan volem
        self.missatge = Label(text= '', fg = 'red') #inicialment el missatge està buit. fg és per canviar el color del text
        self.missatge.grid(row = 3, column= 0 , columnspan= 2, sticky= W + E)
        
    def guardar_producte(self):  #consulta http
        # obté el nom y el preu del producte a afegir
        nom = self.nom.get()  #agafa el valor escrit al recuadre self.nom
        preu = self.preu.get()

        # realizar la request per afegir el producte
        url = "http://localhost:8080/phpProject2/back/index.php?nom={}&preu={}".format(nom,preu)  #url de l'arxiu index.php on s'envia la request per que el processiç
        
        # #dades que envie, 
        response = requests.get(url)  #fem una request post a l'url enviant les data
    
        # verificar si la request és exitosa
        if response.status_code == 200: #200 exitosa, 404 url no trobat, 500 error en el php...
            producto = response.json() # obtenir el producte afegit
            self.tree.insert('', 'end', text=producto['nom'], values=(producto['preu'])) # afegir el producte a la lista tree
            self.missatge.config(text=f'Producto añadido: nom: {producto["nom"]} , preu:  {producto["preu"]}', fg='green') # mostrar el producte afegit en el missatge
            print("{}, {}".format(producto['nom'], producto['preu']))
        else:
            self.missatge.config(text='Error al añadir el producto: {}'.format(response.status_code), fg='red')



if __name__ == '__main__':  #basicament si s'executa com a main, ens desplega la finestra
    window = Tk() #crea una finestra
    application = Product(window)  #es guarda la finestra
    window.mainloop()  #la desplega
