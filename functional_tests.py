from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # Run the browser
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Quite the browser
        self.browser.quit()

    def test_can_start_and_retrieve(self):
        # Running the website of the application
        self.browser.get('http://localhost:8000')

        # "Lists" in title?
        self.assertIn('Lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('list', header_text)

        # Typing the list of things to do.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Type thing to do'
        )

        # Typing "Buy the peacock feathers" in the text box.
        inputbox.send_keys('Buy the peacock feathers')

        # After pressing ENTER, the page has been updated.
        # "1. Buy the peacock feathers" as the element of the list.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy the peacock feathers', [row.text for row in rows])

        # It's still the text box on the page.
        # Typing "Use the peacock feathers to make a bait" as a second element.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use the peacock feathers to make a bait')
        inputbox.send_keys(Keys.ENTER)

        # The page has been updated again, now it's two elements on the list.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy the peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use the peacock feathers to make a bait', [row.text for row in rows])

        # Is it remember on the site? It generated special url with the comment.
        self.fail('End of test!')

        # Go to the special URL - there it a list of things to do.

        # End.

if __name__ == '__main__':
    unittest.main(warnings='ignore')