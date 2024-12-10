import pytest
from bs4 import BeautifulSoup
import requests
import ollama

from reviewer import FileHandler, WebScrapper, Response, UrlFile, find_numbers

def test_file_handler_write(tmp_path):
  # Create an instance of FileHandler
  file_handler = FileHandler(str(tmp_path / "output.txt"))

  # Write some text to the file
  file_handler.open_write_file()
  file_handler.write_file("This is some test data.")
  file_handler.close_file()

  # Read the contents of the file
  with open(str(tmp_path / "output.txt"), "r") as f:
    content = f.read()

  # Assert that the data is written correctly
  assert content == "This is some test data."

def test_find_numbers():
  # Create a test file with review data
  review_data = """Positive review\nNegative review\nNuetral review"""
  with open("reviews.txt", "w") as f:
    f.write(review_data)

  # Call the find_numbers function
  positive, negative, neutral = find_numbers("reviews.txt")

  # Assert that the reviews are counted correctly
  assert positive == 1
  assert negative == 1
  assert neutral == 1

def test_url_file_open_read(tmp_path):
  # Create a temporary file with some URLs
  urls_file = tmp_path / "urls.txt"
  urls_file.write_text("https://example.com/review1\nhttps://example.com/review2")

  # Create an instance of UrlFile
  url_obj = UrlFile(str(urls_file))

  # Open and read the file
  opened_urls = url_obj.open_file()

  # Assert that the URLs are read correctly
  assert len(opened_urls) == 2
  assert opened_urls[0] == "https://example.com/review1\n"
  assert opened_urls[1] == "https://example.com/review2"

def test_web_scrapper_get_parse(mocker, tmp_path):
  # Mock the requests.get function to return a fake response
  mock_response = mocker.Mock()
  mock_response.text = """<div class="pre-white-space">This is a positive review.</div>
  <div class="pre-white-space">This is a neutral review.</div>"""

  def mock_requests_get(url, headers, timeout):
    return mock_response

  mocker.patch('requests.get', side_effect=mock_requests_get)

  # Create a temporary file with a URL
  url_file = tmp_path / "url.txt"
  url_file.write_text("https://example.com/reviews")

  # Create an instance of WebScrapper
  scraper = WebScrapper(str(url_file), 1)

  # Get and parse the reviews
  data = scraper.get_reviews()
  reviews = scraper.parse(data)

  # Assert that the reviews are parsed correctly
  assert len(reviews) == 2
  assert reviews[0].text.strip() == "This is a positive review."
  assert reviews[1].text.strip() == "This is a neutral review."