#! /usr/bin/env python

import unittest
from readline import readline

class MockSocket(object):
    def __init__(self, buf):
        self.buf = buf

    def recv(self, size=1024):
        print type(size), size
        retval = self.buf[0:size]
        self.buf = self.buf[size:]
        return retval

class ReadlineTests(unittest.TestCase):
    def get_iterator(self, buf="foo\nbar\nbaz\n", recv_len=1024):
        return readline(MockSocket(buf), recv_len)

    def test_read_buffer_until_end(self):
        generator = self.get_iterator()
        self.assertEquals(next(generator), "foo")
        self.assertEquals(next(generator), "bar")
        self.assertEquals(next(generator), "baz")
        with self.assertRaises(StopIteration):
            next(generator)

    def test_read_buffer_until_end_without_ending_newline(self):
        generator = self.get_iterator("foo\nbar\nbaz")
        self.assertEquals(next(generator), "foo")
        self.assertEquals(next(generator), "bar")
        self.assertEquals(next(generator), "baz")
        with self.assertRaises(StopIteration):
            next(generator)

    def test_recv_with_a_length_of_one(self):
        generator = self.get_iterator(recv_len=1)
        self.assertEquals(next(generator), "foo")
        self.assertEquals(next(generator), "bar")
        self.assertEquals(next(generator), "baz")
        with self.assertRaises(StopIteration):
            next(generator)

    def test_pass_something_that_doesnt_have_a_recv_method(self):
        with self.assertRaises(Exception):
            next(readline(None))
