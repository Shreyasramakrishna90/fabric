import fabric.api as fabi
from config import *
groupRAW = 'ip172_1_1'
group = 'ip172_1_1:2222'

fabi.env.password = 'riaps'
fabi.env.sudo_password = 'riaps'

path='~/projects/sandbox/etcd-bones'

@fabi.hosts(fabi.env.roledefs[group][0])
def install_etcd():
    fabi.run('mkdir -p tmp')
    fabi.put(path+'/install.sh', './tmp')
    fabi.run('chmod +x ./tmp/install.sh')
    #fabi.sudo('./tmp/install.sh')
    #fabi.run('rm -rf ./tmp')

@fabi.hosts(fabi.env.roledefs[group][0])
def startDisco():
    hostname = fabi.run("hostname")
    print(hostname)
    IP = fabi.env.roledefs[groupRAW][0]
    DISCO="http://%s:2379/v2/keys/discovery/%s" %(IP, hostname)
    print(DISCO)
    fabi.run('mkdir -p etcd')
    fabi.put(path+'/setupDisco.sh', './etcd')
    fabi.run('chmod +x ./etcd/setupDisco.sh')
