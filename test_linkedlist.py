import pytest
from linkedlist import LinkedList

linked_list = LinkedList(["hello", "world", "!!!"])
def test_constructor():
    assert linked_list.head.getval() == "hello"
    assert linked_list.head.getnext().getval() == "world"
    assert linked_list.head.getnext().getnext().getval() == "!!!"

def test_length():
    assert linked_list.length() == 3

def test_first():
    assert linked_list.first() == "hello"

def test_last():
    assert linked_list.last() == "!!!"

def test_get():
    assert linked_list.get(2) == "!!!"

def test_append():
    linked_list.append("gibberish")
    assert linked_list.get(3) == "gibberish"

def test_delete():
    linked_list.delete(1)
    assert linked_list.get(1) == "!!!"

def test_insert():
    linked_list.insert("waaaa?", 1)
    assert linked_list.get(1) == "waaaa?"
    assert linked_list.get(2) == "!!!"
