## TODOs:

- [ ] Fill docs
- [ ] Reorg folder/file structure
- [ ] Receive CSV filepath from command line
- [ ] Check if CSV already exists to insert first base row
- [ ] Fill requirements.txt (pipreqs not working as expected)
- [ ] Script to spam TCP requests
- [ ] Entire setup in a single docker-compose

## Running Mininet with the Controller

To run our mininet topology, execute: 

```bash
sudo mn --switch ovsk --controller remote --custom ./ryu/topology.py --topo tutorialTopology
```

Then, run the Ryu Controller with the following:

```bash
ryu-manager ./ryu/controller.py
```

## Acessing Packet payload with Ryu Controller

If the TCP packet payload exists, it will be the last element on pkt.protocols, e.g.
```
pkt.protocols = [ethernet(...), ipv4(...), tcp(...), 'payload_data']
```

If the payload does not exist, then the object will be such as e.g.
```
pkt.protocols = [ethernet(...), ipv4(...), tcp(...)]
```

## CSV File Writing

As of now, CSV filepath is staticly defined as 'packet_contents.csv', saved into the folder from which the controller is executed.