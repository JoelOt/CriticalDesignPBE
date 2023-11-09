# CriticalDesignPBE

Jo he fet servir XAMPP, no es lo únic que es pot fer servir pero amb això és fàcil i tmb servirà quan haguem de fer el client web. el php està configurat per estar al port :8080 https://www.apachefriends.org/es/download.html

La interficie grafica aquesta de prova es en ttk (nativa de python) perquè es mes fàcil de fer servir i hi ha templates. S'ha de canviar a PGObject.

Coses a fer:
  - Client:
    - Fer que sols es facin requests a la DB en threads auxiliars i tal 
    - Fer interficie gràfica PyGObject amb tot adient al que es mostra als exemples.
    - Fer que al python es pugui rebre llistes fila/columna i ensenyar-les a la interfície
  - Servidor:
    - El php també ha de sols accedir a la DB en threads auxiliars.   
    - Crear els diferents apartats de la DB MySQL.
    - Fer que es pugui rebre els objectes de la DB amb les restriccions posades a la comanda get
    - Mirar d'exposar això al servidor de la UPC en comptes del localhost
