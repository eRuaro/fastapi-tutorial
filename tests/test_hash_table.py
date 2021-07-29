import pytest
import sys 

sys.path.append('..')
from app.hash_table import HashTable

test_hashtable = HashTable()

def test_add():
    """
    Tests adding a new key-value pair to the hashtable
    """
    test_hashtable.add('key', 'value')
    assert test_hashtable.get('key') == 'value'

def test_replace_word():
    """
    Tests replacing a value given a key
    """
    og_value = test_hashtable.get('key')
    test_hashtable.add('key', 'new value')
    assert test_hashtable.get('key') != og_value

def test_get():
    """
    Tests getting a value from the hashtable
    """
    test_hashtable.add('key', 'value')
    assert test_hashtable.get('key') == 'value'

def test_delete():
    """
    Tests deleting a key-value pair from the hashtable
    """
    test_hashtable.delete('key')
    assert test_hashtable.get('key') is None