#!/usr/bin/python3

import random
import config
import converter

# auxilary funxtions
def str_to_opt(pay):
  st = False # state - false if receiving key else true
  res = []
  key = b""
  val = b""
  for i in pay:
    if not st:
      key += (i).to_bytes(1, byteorder='little')
      st = True if random.random() < config.OPTION_SPLIT_PROB else False
    else:
      val += (i).to_bytes(1, byteorder='little')
      if random.random() < config.OPTION_SPLIT_PROB:
        res.append((key, val))
        key = b""
        val = b""
        st = False
  print(res)
  return res

# start

def new_ip_vec():
  # fields
  ihl = None if random.random() < config.PARAM_PROB else random.randint(20, 60) # protocol specification says max 15 -> 15 * 4 + 1
  tos = 0x0 if random.random() < config.PARAM_PROB else random.randint(0, 2**6-1)
  _len = None if random.random() < config.PARAM_PROB else random.randint(0, 2**16-1)
  _id = 1 if random.random() < config.PARAM_PROB else random.randint(0, 2**16-1)
  flags = 0 if random.random() < config.PARAM_PROB else random.randint(0, 2**3-1)
  frag = 0 if random.random() < config.PARAM_PROB else random.randint(0, 2**13-1)
  ttl = 64 if random.random() < config.PARAM_PROB else random.randint(0, 2**8-1)
  proto = 0x0 if random.random() < config.PARAM_PROB else random.randint(0, 2**8-1)
  options = b"" if random.random() < config.PARAM_PROB else bytes(bytearray(random.getrandbits(8) for _ in range(random.randint(0, config.MTU-24))))
  return (ihl, tos, _len, _id, flags, frag, ttl, proto, options)

def new_tcp_vec(hlen): # gets header length of ip
  # fields
  sport = random.randint(0, 2**16-1)
  dport = random.choice(config.protos) if random.random() < config.PARAM_PROB else random.randint(0, 2**16-1)
  seq = 0 if random.random() < config.PARAM_PROB else random.randint(0, 2**32-1)
  ack = 0 if random.random() < config.PARAM_PROB else random.randint(0, 2**32-1)
  dataofs = None if random.random() < config.PARAM_PROB else random.randint(0, 2**4-1)
  reserved = 0 if random.random() < config.PARAM_PROB else random.randint(0, 2**3-1)
  flags = 2 if random.random() < config.PARAM_PROB else random.randint(0, 2**9-1)
  window = 8192 if random.random() < config.PARAM_PROB else random.randint(0, 2**16-1)
  urgptr = 0 if random.random() < config.PARAM_PROB else random.randint(0, 2**16-1)
  options = [] if random.random() < config.PARAM_PROB else str_to_opt(bytearray(random.getrandbits(8) for _ in range(random.randint(0, config.MTU-hlen-20))))
  return (sport, dport, seq, ack, dataofs, reserved, flags, window, urgptr, options)

def new_udp_vec():
  # fields
  sport = random.randint(0, 2**16-1)
  dport = random.choice(config.protos) if random.random() < config.PARAM_PROB else random.randint(0, 2**16-1)
  _len = None if random.random() < config.PARAM_PROB else random.randint(0, 2**16-1)
  return (sport, dport, _len)

def new_raw(hlen): # gets header length
  return b"" if random.random() < config.PARAM_PROB else bytes(bytearray(random.getrandbits(8) for _ in range(random.randint(0, config.MTU-hlen))))
