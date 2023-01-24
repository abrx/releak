from yaml import load,FullLoader
# from PyQt6.QtWidgets import QApplication, QLabel, QWidget

"""
    Un genre de gestionnaire RSS spécialisé sur les releases, suivis de version et CVE 
"""

#####################################################################################
#                                                                                   #
#   Configuration                                                                   #
#                                                                                   #
#####################################################################################

url_grafana = "https://github.com/grafana/grafana"

#####################################################################################
#                                                                                   #
#   Fonctions                                                                       #
#                                                                                   #
#####################################################################################

def get_config(config_file="config/versions.yml"):
    """
        Récupération de la liste des sources / repos à surveiller
        Format du yaml:

        source
          user: repo
    """
    print("Récupération de la configuration dans", config_file)

    with open(config_file) as conf:
        try:
            return load(conf, Loader=FullLoader)

        except:
            print("erreur lors du chargement de la configuration", config_file)
            raise



#####################################################################################
#                                                                                   #
#   Main                                                                            #
#                                                                                   #
#####################################################################################


def main():
    """
        récupère la config en yaml
    """
    versions = get_config()

    # retourne un dictionnaire
    github_versions = versions["github"]
    liste_users_github = list(github_versions)

    print("Liste des users disponibles pour github: ", liste_users_github)
    
    # TODO ERWIN: passer par une fonction
    print("liste des repos: ")
    for user_github,repo in github_versions.items():
        print("https://github.com/",user_github,"/",repo,"/releases.atom ",sep='')

if __name__ == "__main__":
    main()
