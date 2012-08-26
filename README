A fast socket.readline implementation

Example usage
```
import sys
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 80))
s.send("GET / HTTP/1.0\r\nHost: localhost\r\n\r\n")

for line in readline(s):
	print line,
```
