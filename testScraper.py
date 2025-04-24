# This file is for testing some modules in the Scraper class
# Test by bashing "pytest testScraper.py" in the terminal

import pytest
from scraper import Scraper

# This is sample webpage with headings to test the Scraper with
sample_html = '''
<html>
  <body>
    <h3 class="ListItem-title">Headline 1</h3>
    <h3 class="ListItem-title">Headline 2</h3>
    <h2 class="ListItem-title">Headline 3</h2>
  </body>
</html>
'''
# Test headline extraction
def test_get_headline():
    scraper = Scraper()
    headlines = scraper.get_headlines(sample_html)
    # There are the correct number of headlines
    assert len(headlines) == 2
    # They have the correct name
    assert headlines[0].get_text() == 'Headline 1'
    assert headlines[1].get_text() == 'Headline 2'

# Test writing headlines on a temporary file
def test_write_headlines(tmp_path):
    scraper = Scraper()
    # Create temporary file to write to
    file_path = tmp_path / "output.txt"
    # Create a class to test
    class FakeHeadline:
        def get_text(self):
            return "Test Title"
    # Establish the list of headlines to test
    headlines = [FakeHeadline(), FakeHeadline()]
    scraper.write_headlines(headlines, str(file_path))

    # Check that it output
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # Expected content
    assert lines == ["Test Title\n", "Test Title\n"]
