import fabric.api as fabi
from config import *
groupRAW = 'ip172_1_1'
group = 'ip172_1_1:2222'

fabi.env.password = 'riaps'
fabi.env.sudo_password = 'riaps'

path='~/projects/sandbox/consul'

@fabi.hosts(fabi.env.roledefs[group][0])
def install_etcd():
    fabi.run('mkdir -p tmp')
    fabi.put(path+'/install.sh', './tmp')
    fabi.run('chmod +x ./tmp/install.sh')
    #fabi.sudo('./tmp/install.sh')
    #fabi.run('rm -rf ./tmp')
