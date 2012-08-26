#! /usr/bin/env python
# Written by Steeve 'steevel' Lennmark

def readline(socket, size=4096):
    last_pos = 0
    buffer = ""

    if not socket or not hasattr(socket, "recv"):
        raise Exception("socket-like object needs a recv method")

    recv = socket.recv
    while True:
        data = recv(size)
        if not data:
            if buffer:
                yield buffer
            break
        buffer += data

        while True:
            current_pos = last_pos
            last_pos = buffer.find("\n", last_pos) + 1
            if last_pos == 0:
                if current_pos > 0:
                    buffer = buffer[current_pos:]
                break

            yield buffer[current_pos:last_pos-1].rstrip()
