# importation des modules necessaires
from selenium import webdriver  # importer le module de selenium pour intéragir avec les navifateurs web
from selenium.webdriver.common.keys import Keys  # importation de keys pour sumuler les frappes du clavier (comme ENTER)
from selenium.common.exceptions import NoSuchElementException, WebDriverException  # Importation des exceptions spécifiques de selenium
import time

# indiquer le chemin vers la page HTML à tester
path_to_html_file = "file:////Users/JCY/Desktop/Selenium/index.html"
print(path_to_html_file)

try:
    # configurer le we driver (ici chrome)
    options = webdriver.ChromeOptions()  # Création des options du navigateur chrome
    # créer et ouvrir une nouvelle du navigateur chrome
    driver = webdriver.Chrome(options=options)  ##initialisation du webdriver pour chrome avec les options par spécifiques defaut
    # étape 1: ouvrir la page web
    driver.get(path_to_html_file)  ##chargement de la page web
    # étape 2: envoyer les données au formulaire
    username_input = driver.find_element("id", "username")  # Recherche de l'element username par son id
    password_input = driver.find_element("id", "password")  # Recherche de l'element password par son id
    # étape 3: Remplir le formulaire avec les valeurs réélles
    username_input.send_keys("emily")  # Remplir le champs username
    password_input.send_keys("123456")  # Remplir le champs password
    # étape 4: attente d'une durée pour visualiser le remplissage du formulaire
    time.sleep(2)  # temps d'attente de 2 secondes pour visualiser l'action
    # étapes 5: soumettre le formulaire
    password_input.send_keys(Keys.RETURN)  # soumission du formulaire ensimulant la touche ENTER
    # étape 6: attente d'une durée pour visualiser
    time.sleep(10)

except NoSuchElementException as e:
    # Gestion de l'exception pour page introuvable
    print(f"Erreur: element introuvable : {e}")

except WebDriverException as e:
    # Gestion de l'exception si on a un problème de connextion avec le navigateur
    print(f"Erreur: erreur WebDriver : {e}")
finally:
    # étape 7: fermer le navigateur
    driver.quit()  # Fermeture du navigateur pour libérer les ressources