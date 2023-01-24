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



#####################################################################################
#                                                                                   #
#   Functions                                                                       #
#                                                                                   #
#####################################################################################

def get_config(config_file="config/versions.yml"):
    """
        Récupération de la liste des sources / repos à surveiller
        Format du yaml:

        source
          user: repo
    """
    print("Get config file: ", config_file)

    with open(config_file) as conf:
        try:
            return load(conf, Loader=FullLoader)

        except:
            print("Error loading configuration: ", config_file)
            raise


def get_raw_feed_from_url(url):
    """
        Get raw feed from passed rss url
    """
    try:
        feed_list = feedparser.parse(url)
        return feed_list

    except:
        print("Error getting feed: ", url)
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

    print("\nAvailable users for github: ", liste_users_github, "\n")
    
    # TODO ERWIN: passer par une fonction

    for user_github,repo in github_versions.items():
        feed_url = "https://github.com/" + user_github + "/" + repo + "/releases.atom "
        print("\n", feed_url, " :")
    
        # Return feed list from given repo : 
        raw = get_raw_feed_from_url(feed_url)

        # raw has both general feed information and release details under entries
        for release in raw.entries:
            print(release.title)

if __name__ == "__main__":
    main()
