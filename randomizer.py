#!/usr/bin/python3

import random

# [20, 21, 23, 80, 513, 544, 543, 6667, 6668, 7070, 113, random.randint(1, 65535)]

def new_ip_vec():
  # fields
  ihl = None if random.random() > 0.93 else random.randint(20, 60) # protocol specification says max 15 -> 15 * 4 + 1
  tos = 0x0 if random.random() > 0.93 else random.randint(0, 2**6-1)
  _len = None if random.random() > 0.93 else random.randint(0, 2**16-1)
  _id = 1 if random.random() > 0.93 else random.randint(0, 2**16-1)
  flags = 0 if random.random() > 0.93 else random.randint(0, 2**3-1)
  frag = 0 if random.random() > 0.93 else random.randint(0, 2**13-1)
  ttl = 64 if random.random() > 0.93 else random.randint(0, 2**8-1)
  proto = 0x0 if random.random() > 0.93 else random.randint(0, 2**8-1)
  options = b"" if random.random() > 0.93 else bytes(bytearray(random.getrandbits(8) for _ in range(random.randint(0, 1500-24))))

  return (ihl, tos, _len, _id, flags, frag, ttl, proto, options)

