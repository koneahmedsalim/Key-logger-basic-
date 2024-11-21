Ce projet est un keylogger simple écrit en Python. Il enregistre les frappes clavier de l'utilisateur dans un fichier local et les envoie périodiquement à un serveur distant (whebhook server en ligne ) via une requête HTTP POST.

1. Fonctionnalités

Enregistrement des frappes clavier dans un fichier texte local (key_log.txt).
Envoi des logs vers un serveur distant toutes les 30 secondes.
Formatage des touches spéciales (espace, tabulation, entrée, etc.) pour une meilleure lisibilité.

2. Installation

Prérequis
Python 3.x
Les modules Python suivants (installés automatiquement si vous suivez les étapes ci-dessous) :
pynput
requests

3. Étapes
Clonez ou téléchargez ce dépôt.

Installez les dépendances requises avec la commande suivante :
pip install pynput requests

Modifiez l'URL du serveur distant (server_url) dans le fichier principal pour correspondre à votre propre webhook ou endpoint si vous en avez pas rendez vous sur https://webhook.site/  :

server_url = "https://votre-webhook-ou-endpoint"


4. Utilisation
Lancez le script en exécutant :python keylogger.py

Le keylogger commencera à écouter les frappes clavier et à les enregistrer dans le fichier key_log.txt

Les logs seront envoyés automatiquement au serveur spécifié toutes les 30 secondes.

