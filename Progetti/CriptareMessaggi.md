# Criptare messaggi
### Difficoltà: media

### Regole:
- Il programmatore stabilisce una codifica fissa per i messaggi;
- L'utente inserisce un messaggio da criptare; 
- Il computer restituisce il messaggio opportunamente decodificato;

### Suggerimenti:
- Definire una variabile "alphabet", dove inserire tutto l'alfabeto (esclusi i caratteri speciali);
- Tramite una funzione random(), creare una mappa che abbia come chiave il risultato della funzione e come valore, il carattere; assicurarsi che la funzione random abbia sufficienti valori quante le lettere dell'alfabeto;
- Usare un for per ciclare ogni carattere della variabile "alphabet";
- Chiedere all'utente di inserire un messaggio tramite la funzione input(); 
- Criptare il messaggio, utilizzando la mappa creata precedentemente e stampare il messaggio criptato;
- L'utente che dovrà trasformare i numeri in caratteri per decifrare il messaggio.