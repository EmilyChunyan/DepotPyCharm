# importation des modules necessaires
from selenium import webdriver  # importer le module de selenium pour interagir avec les navigateurs
from selenium.webdriver.common.keys import Keys  # importation de keys pour simuler les frappes du clavier(comme Enter)
from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException # Importer des exception specifiques de selenium
import time

# indiquer le chemin vers la page HTML
path_to_html_file = "file:///Users/JCY/Desktop/Selenium/index.html"
#/Users/JCY/Desktop/Selenium

try:
    # configurer le webdriver (ici chrome)
    options = webdriver.EdgeOptions() #Creation d'un instance du navigateur chrome
    ## creer et ouvrir (lancer) une nouvelle session du navigateur chrome
    driver = webdriver.Edge(options=options) # initialisation du webdriver pour chrome avec les options specifique pqr defaut
    # etape 1 : ouvrir la page web
    driver.get(path_to_html_file)  ## chargement de la page web
    # etape 2: envoyer les donnnées au formulaire
    username_input = driver.find_element("id", "username")  # recherche de l'element username par son ID
    password_input = driver.find_element("id", "password")  # recherche de l'element password par son ID
    # Étape 3 : Remplir le formulaire avec les valeurs réelles
    username_input.send_keys("emily")  # remplier le champs username
    password_input.send_keys("12345")  # remplier le champs password
    # Étape 4: Attendre une durée pour visualiser le remplissage du formulaire
    time.sleep(2) # temps d'attete de deux (2) secondes pour visualiser l'action
    # Étape 5 : soumettre le formulaire
    password_input.send_keys(Keys.RETURN) # soummission du formulaire en simulant la touche ENTER
    # étape 6 :Attendre une durée pour visualiser
    time.sleep(10)

except NoSuchElementException as e:
    # Gestion de l'exception pour page introuvable
    print(f"Erreur: element introuvable : {e}")

except WebDriverException as e:
    # Gestion de l'exception si on a un probleme de connexion avec le navigateur
    print(f"Erreur: erreur WebDriver : {e}")

finally:
    # étape 7 fermer le navigateur
    driver.quit()  # fermeture du navigateur pour liberer les ressources