from services import SocialNetworkScraper

if __name__ == "__main__":
    service = SocialNetworkScraper()

    title = "Test automated post"
    content = "Test automated post content"
    # service.social_network_login()
    service.social_network_add_post(title, content)
    # driver = service.create_driver()
    print('done')