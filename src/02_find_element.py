import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(executable_path="./chromedriver")
        self.driver.get("http://demo-store.seleniumacademy.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_id("q")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_id("input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_element_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img'
        )

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector(
            "div.header-minicart span.icon"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
