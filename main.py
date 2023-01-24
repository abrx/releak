from yaml import load,FullLoader
import feedparser
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


def get_raw_feed_from_url(url):
    """
        Get title list from passed rss url
    """
    print("Récupération du contenu de", url)
    
    try:
        feed_list = feedparser.parse(url)
        print(feed_list)
    except:
        print("Erreur lors de la récupération du feed", url)
        raise


#####################################################################################
#                                                                                   #
#   Main                                                                            #
#                                                                                   #
#####################################################################################


def main():
    """
        Get yaml config
        Build github urls
        Return feed titles 
    """
    versions = get_config()

    # Return dictionary of desired versions
    github_versions = versions["github"]
    liste_users_github = list(github_versions)

    print("Liste des users disponibles pour github: ", liste_users_github, "\n\n")
    
    # TODO ERWIN: passer par une fonction
    print("liste des repos: ")
    for user_github,repo in github_versions.items():
        feed_url = "https://github.com/" + user_github + "/" + repo + "/releases.atom "
        print(feed_url, "\n\n")
    
        # Return feed list from given versions : 
        get_raw_feed_from_url(feed_url)

if __name__ == "__main__":
    main()
