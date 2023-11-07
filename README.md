# UE-AD-A1-MIXTE

Ce TP suit l'architecture suivante:

![Alt text](images\structure.png?raw=true "Structure des services")

## TP vert

Au travers du service User (porte d'accès du réseau de services), un utilisateur peut effectuer différentes opérations:
- set_booking_user: Permet de rajouter un booking à un utilisateur avec un film, une date et un utilisateur. Cela fait intervenir les services de Movie, Bookings et Times
- get_booking_byuser: Permet de récupérer l'ensemble des bookings d'un utilisateur. Cela fait intervenir les services de Bookings
- get_movies_byuser: Permet de récupérer l'ensemble des movies d'un utilisateur. Cela fait intervenir les services de Movies

## TP rouge

Nous avons transformé la requête get_booking_by_user. Pour l'exécuter vous devez commenter les lignes 175 et 176 de user/user.py et décomenter la ligne 177. Cela va lancer un run prédéfini avec un call a get_booking_by_user puis en parallèle un getBooking et on doit voir arriver la réponse de la première requêtes 5 secondes après. 

## Lancement

Pour lancer les services il suffit seulement d'ouvrir 4 terminaux (un pour chaque service) puis à chaque fois de se positionner dans le dossier associé (ex: ``` cd ./movie ```) puis de lancer la commande ``` python service.py ```

