# UE-AD-A1-MIXTE

Ce TP suit l'architecture suivante:

![Alt text](images\structure.png?raw=true "Structure des services")

## TP vert

Au travers du service User (porte d'accès du réseau de services), un utilisateur peut effectuer différentes opérations:
- set_booking_user: Permet de rajouter un booking à un utilisateur avec un film. Cela fait intervenir les services de Movie, Bookings et Times
- get_booking_byuser: Permet de récupérer l'ensemble des bookings d'un utilisateur. Cela fait intervenir les services de Bookings
- get_movies_byuser: Permet de récupérer l'ensemble des movies d'un utilisateur. Cela fait intervenir les services de Movies
