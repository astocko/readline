#! /usr/bin/env python

import unittest
from readline import readline
from mock import MagicMock

class TestReadline(unittest.TestCase):
    def iterate_readline(self, iterator, recv_len=1024):
        socket = MagicMock()
        socket.recv.side_effect = iterator + ("", )

        it = readline(socket, recv_len)
        self.assertEquals(next(it), "foo")
        self.assertEquals(next(it), "bar")
        self.assertEquals(next(it), "baz")
        with self.assertRaises(StopIteration):
            next(it)

    def test_read_buffer_until_end(self):
        self.iterate_readline(("foo\nbar\nbaz\n", ))

    def test_read_buffer_until_end_without_ending_newline(self):
        self.iterate_readline(("foo\nbar\nbaz", ))

    def test_recv_with_a_length_of_one(self):
        self.iterate_readline(tuple("foo\nbar\nbaz\n"), 1)

    def test_pass_something_that_doesnt_have_a_recv_method(self):
        with self.assertRaises(Exception):
            next(readline(None))
