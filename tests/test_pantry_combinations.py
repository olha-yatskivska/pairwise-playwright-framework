import pytest
import csv
from pathlib import Path
from playwright.sync_api import expect
from pages.pantry_page import PantryPage

def load_csv_data():
    """
    Reads the pairwise-data.csv file, skips the header row, 
    and returns a list of tuples for pytest parametrization.
    """
    csv_file = Path(__file__).parent.parent / "data" / "pairwise_data.csv"
    data = []
    
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        
        for row in reader:
            # Skip empty rows
            if not row or not row[0].strip():
                continue 
                
            test_id = row[0]
            pantry = row[1]
            occasion = row[2]
            diet = row[3]
            people = row[4]
            full_matched = row[5]
            
            # Extract the 'Valid' boolean from index 6
            # .strip().upper() ensures robust matching against "True" or "TRUE"
            is_valid = row[6].strip().upper() == "TRUE"
            
            data.append(pytest.param(pantry, occasion, diet, people, full_matched, is_valid, id=test_id))
            
    return data

@pytest.mark.parametrize("pantry, occasion, diet, people, full_matched, is_valid", load_csv_data())
def test_pantry_pairwise_combinations(pantry_page: PantryPage, pantry, occasion, diet, people, full_matched, is_valid):
    """
    Data-driven test running all PICT-generated pairwise combinations.
    Expected outcome is now determined by the 'is_valid' flag from the CSV.
    """
    # 0. Handle 'NA' conditions with deterministic defaults
    # When PICT generates 'NA' (Don't Care), we use the UI's default state 
    # to ensure the test is 100% reproducible and avoids unexpected side-effects.
    if occasion == "NA":
        occasion = "None"
    if diet == "NA":
        diet = "uncheck"
    if full_matched == "NA":
        full_matched = "OFF"
        
    # 1. Fill out the form
    pantry_page.select_pantry_items(meat=pantry, fish=pantry, veg=pantry)
    pantry_page.select_occasion(occasion)
    pantry_page.select_diets(diet)
    
    if people == "EMPTY":
        pantry_page.fill_number_of_people("")
    elif people != "NA":
        pantry_page.fill_number_of_people(people)
        
    if full_matched != "NA":
        pantry_page.set_full_matched(full_matched)
        
    pantry_page.submit_form()
    
    # 2. Determine Expected Outcome using the 'is_valid' flag
    if not is_valid:
        # We expect the success alert to be hidden (blocked by HTML5 validation)
        expect(pantry_page.success_alert).to_be_hidden()
        assert not pantry_page.is_people_input_valid(), "HTML5 validation failed to catch invalid input."
        
        # Extract and print the native validation message for the Trace Viewer and terminal
        validation_msg = pantry_page.get_people_input_validation_message()
        print(f"\nExpected validation failure caught: '{validation_msg}'")
    else:
        # We expect the success alert to be visible
        expect(pantry_page.success_alert).to_be_visible()