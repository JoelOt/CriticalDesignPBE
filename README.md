# CriticalDesignPBE

Està fet fent servir XAMPP. Està configurat per estar al port :8080 https://www.apachefriends.org/es/download.html

Coses a fer:
  - Client:
    - Fer que sols es facin requests a la DB en threads auxiliars (concurrent)
    - Fer interficie gràfica PyGObject amb tot adient al que es mostra als exemples.
    - Fer el login i logout(amb rfid i lcd)
    - Tractar les dades rebudes per mostrar-les al gtk en una taula
  - Servidor:  
    - Crear els diferents apartats de la DB MySQL.
    - Fer que es pugui rebre els objectes de la DB amb les restriccions posades a la comanda get
    - Mirar de fer una LAN per fer client-servidor amb la RPi
    - Fer el parsing com esta posat a l'exemple
    - Mirar d'enviar les dades al client de la millor manera
