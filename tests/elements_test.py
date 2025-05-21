from pages.elements_page import CheckBoxPage, TextBoxPage
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box') 
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "email does not match"
            assert current_address == output_cur_addr, "current address does not match"
            assert permanent_address == output_per_addr, "permanent address does not match"



            # input_data = text_box_page.fill_all_fields() #сокращенный вариант (не показывает где ошибка и менее понятен)
            # output_data = text_box_page.check_filled_form()
            # assert input_data == output_data


    class TestCheck_box:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkboxes have not been selected'