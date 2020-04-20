
## Usage

### Station Configuration

Wireshark filter: `pn_dcp`


`sudo python main.py -i eth0 discover`

`sudo python main.py -i eth0 get-param 00:30:11:33:d7:1a name`

`sudo python main.py -i eth0 set-param 00:30:11:33:d7:1a name foobar`

`sudo python main.py -i eth0 get-param 00:30:11:33:d7:1a ip`

`sudo python main.py -i eth0 set-param 00:30:11:33:d7:1a ip 192.168.1.15,255.255.255.0,192.168.1.1`

### Cyclic data

`sudo python main.py -i eth0 read station-name api slot subslot index`, 
eg. 
`sudo python main.py -i eth0 read foobar 0 1 1 2`.

Wireshark filter: `pn_io_device`