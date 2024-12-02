import pytest
import ollama

from reviewer import FileHandler
from reviewer import Response

def test_file_open(tmpdir):
    file = FileHandler(tmpdir.join('responses.txt'))
    file.open_write_file()

def test_file_write(tmpdir):
    file = FileHandler(tmpdir.join('responses.txt'))
    file.open_write_file()
    assert file.write_file("Testing/n")



def test_prompt():
    response = Response("""Test that Phi-3 generates a response""")
    r = response.prompt()
    assert r.message.content is not None
    assert len(r.message.content) > 0

