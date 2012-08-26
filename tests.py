#! /usr/bin/env python

from gevent import monkey
monkey.patch_all()

import socket
import unittest
from readline import readline

class ReadlineTests(unittest.TestCase):
    def setUp(self):
        # Default buffer to test against
        self.buffer = "foo\nbar\nbaz\n"

        from gevent.server import StreamServer
        def handle(socket, address):
            socket.sendall(self.buffer)
            socket.close()

        server = StreamServer(("127.0.0.1", 0), handle)
        server.start()
        self.server_port = server.server_port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("127.0.0.1", self.server_port))

    def tearDown(self):
        if self.socket:
            self.socket.close()

    def get_connection(self, size=4096):
        return readline(self.socket, size)

    def test_everything_in_buffer(self):
        generator = self.get_connection()
        self.assertEquals(next(generator), "foo")
        self.assertEquals(next(generator), "bar")
        self.assertEquals(next(generator), "baz")
        with self.assertRaises(StopIteration):
            next(generator)

    def test_recv_1(self):
        generator = self.get_connection(1)
        self.assertEquals(next(generator), "foo")
        self.assertEquals(next(generator), "bar")
        self.assertEquals(next(generator), "baz")
        with self.assertRaises(StopIteration):
            next(generator)

    def test_not_a_socket(self):
        with self.assertRaises(Exception):
            next(readline(None))

    def test_no_ending_newline(self):
        self.buffer = "foo\nbar\nbaz"
        generator = self.get_connection()
        self.assertEquals(next(generator), "foo")
        self.assertEquals(next(generator), "bar")
        self.assertEquals(next(generator), "baz")
        with self.assertRaises(StopIteration):
            next(generator)

if __name__ == "__main__":
    unittest.main(verbosity=2)
