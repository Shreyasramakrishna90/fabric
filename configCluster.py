from config import *
import fabric.api as fabi

fabi.env.password = 'riaps'
fabi.env.sudo_password = 'riaps'

fabi.env.key_filename = '~/.ssh/cluster_rsa'

@fabi.parallel
def sshd_config():
	'''Change ssh port to 2222, and enable the usb ethernet'''
	fabi.sudo("sed -i 's/Port 22/Port 2222/g' /etc/ssh/sshd_config")
	shutdown()

def getIPs():
	IPs=fabi.sudo('arp-scan -I eth0 --localnet')
	print(type(IPs))


# def interfaces():
# 	fabi.put('configs/interfaces', '/etc/network/interfaces', use_sudo=True)
# 	subnet = fabi.run('hostname -I | cut -d " " -f 1 | cut -d "." -f 3')
# 	cmd = "sed -i 's/10.1.[1-9].0/10.1.%s.0/g' /etc/network/interfaces" %subnet
# 	fabi.sudo(cmd)
# 	cmd = "sed -i 's/10.1.[1-9].1/10.1.%s.1/g' /etc/network/interfaces" %subnet
# 	fabi.sudo(cmd)
# 	fabi.put('configs/dhclient.conf', '/etc/dhcp/dhclient.conf', use_sudo=True)

def putInterfaces():
	fabi.put('Interfaces')
	fabi.sudo('chmod +x ~/Interfaces/setup.sh')

def runInterfaces():
	fabi.sudo('~/Interfaces/setup.sh')


# def router():
# 	fabi.run('echo "supersede routers 172.21.130.1;" | sudo tee --append /etc/dhcp/dhclient.conf')
#
# def usb_eth():
# 	fabi.run('echo "auto eth1" | sudo tee --append /etc/network/interfaces')
# 	fabi.run('echo "iface eth1 inet dhcp" | sudo tee --append /etc/network/interfaces')
# #	fabi.sudo("shutdown -r +1")
#
# def gateway():
# 	subnet = fabi.run('hostname -I | cut -d " " -f 1 | cut -d "." -f 3')
# 	cmd = 'echo "up route add -net 10.1.0.0 netmask 255.255.0.0 gw 10.1.%s.1" | sudo tee --append /etc/network/interfaces' %subnet
# 	fabi.run(cmd)
# 	cmd = 'echo "up route del -net 10.1.%s.0 netmask 255.255.255.0 | sudo tee --append /etc/network/interfaces' %subnet

def secureCOMs():
	'''Copy the local ssh key to the bbbs'''
	fabi.put('~/.ssh/id_rsa.key', '~/.ssh')
        fabi.put('~/.ssh/id_rsa.pub', '~/.ssh')
        fabi.sudo('cp ~/.ssh/authorized_keys ~/.ssh/authorized_keys.bak')
        fabi.sudo('cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys')

@fabi.parallel
def shutdown():
	fabi.sudo("shutdown -r +1")

def tools():
	fabi.run('sudo apt install btrfs-tools')
	fabi.run('sudo apt install arp-scan')

@fabi.parallel
def test():
	fabi.run('echo hello')
	fabi.run('echo 1 >> /sys/class/leds/beaglebone\:green\:usr2/brightness')
	fabi.run('sleep 30')
	fabi.run('echo 0 >> /sys/class/leds/beaglebone\:green\:usr2/brightness')

#@fabi.parallel
def update():
	fabi.sudo('cp /etc/network/interfaces /etc/network/interfaces.bak')
	fabi.sudo('sudo apt-get -y remove "riaps-*"')
	fabi.sudo('sudo apt autoclean')
	fabi.sudo('sudo apt autoremove')
	fabi.sudo('apt update')
	fabi.sudo("apt -y install 'riaps-*'")

@fabi.parallel
def version():
	fabi.run("'dpkg -l | grep riaps'")
