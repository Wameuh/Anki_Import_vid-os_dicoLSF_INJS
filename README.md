# Anki_Import_vid-os_dicoLSF_INJS
Programme pour récupérer les vidéos du dictionnaire de l'INJS de langue des signes française et créer un fichier permettant l'import pour la création d'un paquet Anki.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Principe de fonctionnement :
  - Il utilise le fichier "lite_mots.txt" qui correspond à l'ensemble des mots indiqués sur le site : http://www.lsfdico-injsmetz.fr/recherche-alphabetique.php .
  - Par l'intermédiaire de youtube_dl il télécharge les vidéos sur le site http://www.lsfdico-injsmetz.fr correspondants aux mots de la liste. Les vidéos sont stockées dans
  le dossier ./media/ .
  - Il créé et rempli un fichier "importanki.txt" qui va indiquer l'ensemble des éléments nécessaire à Anki pour créer un paquet.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Import dans Anki :
  - Tout d'abord il faut déplacer les vidéos contenues dans le répertoire ./media/ dans le répertoire : \AppData\Roaming\Anki2\nom_compte_anki\collection.media\
  - Lancez Anki. Puis Fichier > Importer et sélectionnez le fichier importanki.txt.
  - Choisissez le type de carte (recommandé : "Basic (and reversed card)"), créez un nouveau paquet, le champs séparés par : "Virgules" et choisissez "importer le cartes
  même si le premier champ existe déjà."
  - cliquez sur importer.
  - dans le nouveau paquet, cliquez sur la route dentée et sélectionnez "Placez les cartes ... hasard" dans "Ordre d'apparition".

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Programme réalisé sur la version python : 3.8
Il nécessite l'installation du paquet youtube_dl.


