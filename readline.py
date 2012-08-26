# Copyright 2012 Steeve Lennmark
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""An attempt at creating a fast version of socket.readline()"""

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
