from services import SocialNetworkScraper

if __name__ == "__main__":
    service = SocialNetworkScraper()
    driver = service.create_driver()
    print('done')