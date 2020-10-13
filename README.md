# QEMUSLNetFuzz
Stateless Network Fuzzer for QEMU (Targeting SLiRP)

## Introduction

A naive way of fuzzing is implemented in this repository. Fuzzing is done **statelessly** instead of being done in *stateful* method which is done in *state-of-art* fuzzers. The attempts of doing the fuzzing statefully were practically done first, but it was hard because of high overhead in VMs.

This fuzzer uses randpkt from wireshark to generate packets. A file is considered to be a set of packets that could possibly crash the VM. If the VM is crashed, then the packet will be stored in file.

The fuzzer consists of two parts: (1) fuzzer part that runs in host, (2) target part that runs in host. Fuzzer part runs VM and target and sends random vectors to target, so that target can receive the packet and convert it to packet, thus try to send it back to host. The fuzzer watches the state of VM and records the packet to a file. The target part is just a simple server that receives the vector and assemble the packet, send it back to host.