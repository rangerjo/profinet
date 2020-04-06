
## Usage

### Station Configuration

Wireshark filter: `pn_dcp`


`sudo python main.py -i eth0 discover`

`sudo python main.py -i eth0 get-param 00:30:11:33:d7:1a name`

`sudo python main.py -i eth0 set-param 00:30:11:33:d7:1a name foobar`

`sudo python main.py -i eth0 get-param 00:30:11:33:d7:1a ip`

Setting the ip-adress does not work yet.

### Cyclic data

`sudo python main.py -i eth0 read station-name api slot subslot index`, 
eg. 
`sudo python main.py -i eth0 read foobar 0 1 1 2`.

Wireshark filter: `pn_io_device`