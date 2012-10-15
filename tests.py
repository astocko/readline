#! /usr/bin/env python

import unittest
from readline import readline
from mock import MagicMock

class TestReadline(unittest.TestCase):
    def setUp(self):
        self.socket = MagicMock()
        self.socket.recv.side_effect = ("foo\nbar\nbaz\n", "")

    def test_read_buffer_until_end(self):
        it = readline(self.socket)
        self.assertEquals(next(it), "foo")
        self.assertEquals(next(it), "bar")
        self.assertEquals(next(it), "baz")
        with self.assertRaises(StopIteration):
            next(it)

    def test_read_buffer_until_end_without_ending_newline(self):
        self.socket.recv.side_effect = ("foo\nbar\nbaz", "")

        it = readline(self.socket)
        self.assertEquals(next(it), "foo")
        self.assertEquals(next(it), "bar")
        self.assertEquals(next(it), "baz")
        with self.assertRaises(StopIteration):
            next(it)

    def test_recv_with_a_length_of_one(self):
        self.socket.recv.side_effect = tuple("foo\nbar\nbaz\n") + ("", )

        it = readline(self.socket)
        self.assertEquals(next(it), "foo")
        self.assertEquals(next(it), "bar")
        self.assertEquals(next(it), "baz")
        with self.assertRaises(StopIteration):
            next(it)

    def test_pass_something_that_doesnt_have_a_recv_method(self):
        with self.assertRaises(Exception):
            next(readline(None))
