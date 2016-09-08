from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEquals(
            input_box.location['x'] + input_box.size['width'] / 2,
            self.browser.get_window_size()['width'] / 2,
            delta=5
        )

        # She starts a new list and sees the input is nicely
        # centered there too
        input_box.send_keys('testing\n')
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEquals(
            input_box.location['x'] + input_box.size['width'] / 2,
            self.browser.get_window_size()['width'] / 2,
            delta=5
        )
