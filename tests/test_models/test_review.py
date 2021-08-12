#!/usr/bin/python3
"""Module for test Review class"""
import unittest
import pep8
import json
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review class implementation"""
    def test_doc_module(self):
        """Module documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Checks type """
        new = self.value(place_id="123456789s")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Checks type """
        new = self.value(user_id="123456789s")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Checks type """
        new = self.value(text="Lorem Ipsum")
        self.assertEqual(type(new.text), str)


if __name__ == '__main__':
    unittest.main()
