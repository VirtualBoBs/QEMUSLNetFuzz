#!/usr/bin/python3

from scapy.all import *

def ip_vec_to_pkt(vec):
  return IP(ihl=vec[0], tos=vec[1], len=vec[2], id=vec[3], flags=vec[4], frag=vec[5], \
    ttl=vec[6], proto=vec[7], options=IPOption(vec[8]))

def tcp_vec_to_pkt(vec):
  return TCP(sport=vec[0], dport=vec[1], seq=vec[2], ack=vec[3], dataofs=vec[4], \
    reserved=vec[5], flags=vec[6], window=vec[7], urgptr=vec[8], options=vec[9])

def udp_vec_to_pkt(vec):
  return UDP(sport=vec[0], dport=vec[1], len=vec[2])
