import os


## Le programme demarre ici
print("Recherche de fichiers malveillants...")


## On commence par iterer sur les fichiers presents dans le dossier sites_clients

## racine est une variable qui contient le nom du repertoire: e.g., ./sites_clients/site_photographes_paris/
## fichiers est une liste de fichiers presents dans le repertoire: ["fichier1.php", "fichier2.php"...]
chemin_complet = os.path.dirname(os.path.abspath(__file__))
for racine, _, fichiers in os.walk(chemin_complet + "/sites_clients"):
    for fichier in ...: # a remplir (etape 2)
        malveillant = ... # a remplir

        if fichier...: # a remplir (etape 3)
            print(fichier)
            malveillant = ... # a remplir

        nom_complet = racine + "/" + fichier
        fichier_ouvert = ... # a remplir (etape 4)
        contenu = ... # a remplir (etape 4)
        if ...: # a remplir (etape 4)
            print(fichier)
            malveillant = ...

        if malveillant:
            print("Renommer le fichier %s" % fichier)
            nouveau_nom = ... # a remplir
            ... # a remplir

        fichier_ouvert.close()
