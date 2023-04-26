from services import SocialNetworkScraper

if __name__ == "__main__":
    service = SocialNetworkScraper()

    title = "Selenium post"
    content = "Автоматический пост, тепрь я смогу взламівать Пентагон :)"
    service.social_network_add_post(title, content)
    print('done')