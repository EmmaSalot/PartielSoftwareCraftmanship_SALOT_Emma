# partielSC

## 1. Forkez ce repo ou suivez son exemple de format dans un repo que vous devez me partager à l'adresse remi.hamy@gmail.com
## Format du nom de repo PartielSoftwareCraftmanship"< Votre NOM PRENOM >"

## 2. Partie questions
Veuillez copier les questions et y répondre dans ce README pour les questions textes.
Pour les autres questions, mettez votre code dans le dossier CODE à la racine de votre repo

2. Qu’est ce que du code propre ?  
Un code propre est un code facile à comprendre et à faire évoluer. Il n'est pas répétitif et est bien organisé.  

3. De votre expérience de l’agilité en entreprise, en vous basant sur
les piliers du manifeste vu en cours. Que pourriez vous améliorer dans
la geson de vos projets ?  
Dans mon entreprise nous utilisont la méthode agile pour nos projets mais depuis peu de temps, il y a donc encore des choses à amélorier.  
Il devrait y avoir plus de démos avec le client, même si c'est difficile avec les agendas de toutes les parties je pense que ça manque au bon développement de certains projets. Un autre axe d'amélioration serait de pouvoir travailler avec les utilisateurs de temps en temps, je sais que cela est impossible dans certains cas mais je pense que cela pourrait améliorer nos livrables. 

4. Code review   
-La classe OrderProcessor fait trop de choses. Elle est responsable de vérifier l'inventaire, enregistrer les commandes, envoyer des emails, mettre à jour l'inventaire et appliquer des remises. Ces responsabilités devraient être séparées dans différentes classes ou méthodes pour améliorer la maintenabilité et la lisibilité.

-La classe OrderProcessor crée ses dépendances (Database, EmailService, InventorySystem) en interne. Cela rend difficile le test de la classe.

-L'utilisation d'une RuntimeException générique n'est pas une bonne pratique. Des exceptions plus spécifiques devraient être utilisées pour avoir un meilleur contexte d'erreur.

-Le pourcentage de remise (10%) est codé en dur. Il devrait être défini comme une constante.


Commenter pour le Kata:  
Le test "test_survivant_rencontre_zombie" ne passe pas toujours comme le mouvement du zombie et les dégats sont aléatoires.