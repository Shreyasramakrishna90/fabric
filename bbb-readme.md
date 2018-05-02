Reference : https://github.com/eiselesr/fabric.git
runFab.sh


Change port to 2222
$ sed -i 's/Port 22/Port 2222/g' /etc/ssh/sshd_config

Then can use runFab.sh if wanted.
./runFab 'ip4_2'
./runFab 'ip4_2' update

or do the steps manually

copy ssh keys
scp ~/.ssh/id_rsa.key riaps@<ip>:~/.ssh
scp ~/.ssh/id_rsa.pub riaps@<ip>:~/.ssh
cp ~/.ssh/authorized_keys ~/.ssh/authorized_keys.bak'
cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys'


update
sudo apt update
sudo apt -y install 'riaps-*'


add to /etc/network/interfaces
# is the router that the board is connected to.
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet dhcp
up route add -net 10.1.0.0 netmask 255.255.0.0 gw 10.1.#.1
up route del -net 10.1.#.0 netmask 255.255.255.0

overwrite /etc/dhcp/dhclient.conf
