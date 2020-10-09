#!/usr/bin/python3

from scapy.all import *

import randomizer
import converter

def gen_pkt():
  # choice = random.choice(["IP", "TCP", "UDP"])
  choice = random.choice(["TCP"])
  if choice == "IP":
    ip = converter.ip_vec_to_pkt(randomizer.new_ip_vec())
    raw = randomizer.new_raw(len(ip))
    return ip / raw
  elif choice == "TCP":
    ip = converter.ip_vec_to_pkt(randomizer.new_ip_vec())
    tcp = converter.tcp_vec_to_pkt(randomizer.new_tcp_vec(len(ip)))
    raw = randomizer.new_raw(len(ip)+len(tcp))
    return ip / tcp / raw
  elif choice == "UDP":
    ip = converter.ip_vec_to_pkt(randomizer.new_ip_vec())
    udp = converter.udp_vec_to_pkt(randomizer.new_udp_vec())
    raw = randomizer.new_raw(len(ip)+len(udp))
    return ip / udp / raw
