from playwright.sync_api import Page
from pages.base_page import BasePage

class PantryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Locators using the highly reliable data-testid attributes
        self.meat_select = page.get_by_test_id("select-meat")
        self.fish_select = page.get_by_test_id("select-fish")
        self.veg_select = page.get_by_test_id("select-vegetables")
        
        self.full_matched_toggle = page.get_by_test_id("checkbox-full-matched")
        self.occasion_select = page.get_by_test_id("select-occasion")
        self.people_input = page.get_by_test_id("input-people-count")
        
        self.diet_low_glycemic = page.get_by_test_id("checkbox-diet-low-glycemic")
        self.diet_vegetarian = page.get_by_test_id("checkbox-diet-vegetarian")
        self.diet_gastritis = page.get_by_test_id("checkbox-diet-gastritis")
        
        self.submit_button = page.get_by_test_id("button-submit")
        self.success_alert = page.get_by_test_id("success-alert")
        self.error_alert = page.get_by_test_id("error-alert")

    def fill_number_of_people(self, count: str):
        self.people_input.fill(str(count))

    def select_pantry_items(self, meat: str, fish: str, veg: str):
        if meat and meat.upper() != "NA":
            self.meat_select.select_option(meat)
        if fish and fish.upper() != "NA":
            self.fish_select.select_option(fish)
        if veg and veg.upper() != "NA":
            self.veg_select.select_option(veg)

    def set_full_matched(self, state: str):
        if state.upper() == "ON":
            self.full_matched_toggle.check()
        elif state.upper() == "OFF":
            self.full_matched_toggle.uncheck()

    def select_occasion(self, occasion: str):
        self.occasion_select.select_option(occasion)

    def select_diets(self, diet_string: str):
        # Ensure all are unchecked initially to prevent state bleeding between tests
        self.diet_low_glycemic.uncheck()
        self.diet_vegetarian.uncheck()
        self.diet_gastritis.uncheck()

        if diet_string == "None" or not diet_string or diet_string.lower() == "uncheck":
            return 
            
        if diet_string == "All check":
            self.diet_low_glycemic.check()
            self.diet_vegetarian.check()
            self.diet_gastritis.check()
            return

        # Handle specific comma-separated diets
        if "Low-Glycemic" in diet_string:
            self.diet_low_glycemic.check()
        if "Vegetarian" in diet_string:
            self.diet_vegetarian.check()
        if "Gastritis" in diet_string:
            self.diet_gastritis.check()

    def submit_form(self):
        self.submit_button.click()

    def is_success_alert_visible(self) -> bool:
        return self.success_alert.is_visible()
        
    def is_error_alert_visible(self) -> bool:
        return self.error_alert.is_visible()
        
    def is_people_input_valid(self) -> bool:
        return self.people_input.evaluate("node => node.validity.valid")

    def get_people_input_validation_message(self) -> str:
        return self.people_input.evaluate("node => node.validationMessage")