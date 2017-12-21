gethURL =  "https://gethstore.blob.core.windows.net/builds/geth-linux-arm7-1.7.0-6c6c7b2a.tar.gz"
@fabi.roles('all2')
def setupGETH():
	fabi.put('~/.ssh/id_rsa.key', '~/.ssh')
	fabi.put('~/.ssh/id_rsa.pub', '~/.ssh')
	fabi.sudo('cp ~/.ssh/authorized_keys ~/.ssh/authorized_keys.bak')
	fabi.sudo('cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys')
	fabi.sudo("apt install dtach")
	fabi.run("mkdir Downloads")
	fabi.run("wget -O ~/Downloads/geth.tar.gz " + gethURL)
	fabi.run("tar -xvzf ~/Downloads/geth.tar.gz")
	fabi.run("cp geth.tar.gz")
