from services import SocialNetworkScraper

if __name__ == "__main__":
    service = SocialNetworkScraper()

    title = "Selenium post"
    content = "Now I can debug my website:)"
    service.social_network_add_post(title, content)
    print('done')
