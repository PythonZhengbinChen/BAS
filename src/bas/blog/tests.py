#!/usr/bin/python
#-*- coding: utf-8 -*-
from django.test import TestCase
from modal.bookModal import BookModal

# Create your tests here.


book = BookModal()
print book.getAuthorInfo("陈忠实")