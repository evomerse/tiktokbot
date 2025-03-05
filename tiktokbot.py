from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# URL du site web fictif
url = "https://example.com"

# Fonction pour liker une vidéo
def like_video(driver, video_id):
    # Naviguer vers la page de la vidéo
    driver.get(f"{url}/video/{video_id}")

    # Attendre que la page se charge
    time.sleep(2)

    # Trouver le bouton "Like" et cliquer dessus
    like_button = driver.find_element(By.XPATH, '//button[@aria-label="Like"]')
    like_button.click()

    print(f"Video {video_id} liked successfully.")

# Fonction pour suivre un utilisateur
def follow_user(driver, username):
    # Naviguer vers la page de l'utilisateur
    driver.get(f"{url}/user/{username}")

    # Attendre que la page se charge
    time.sleep(2)

    # Trouver le bouton "Follow" et cliquer dessus
    follow_button = driver.find_element(By.XPATH, '//button[@aria-label="Follow"]')
    follow_button.click()

    print(f"User {username} followed successfully.")

# Fonction pour lire les identifiants à partir d'un fichier CSV
def read_identifiers(file_path):
    df = pd.read_csv(file_path)
    return df['video_id'].tolist(), df['username'].tolist()

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialiser le navigateur
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Lire les identifiants à partir du fichier CSV
    videos_to_like, users_to_follow = read_identifiers('data.csv')

    # Liker les vidéos
    for video_id in videos_to_like:
        like_video(driver, video_id)
        time.sleep(1)  # Attendre 1 seconde entre chaque like pour éviter de se faire bannir

    # Suivre les utilisateurs
    for username in users_to_follow:
        follow_user(driver, username)
        time.sleep(1)  # Attendre 1 seconde entre chaque follow pour éviter de se faire bannir

    # Fermer le navigateur
    driver.quit()