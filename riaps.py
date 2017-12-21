#https://github.com/RIAPS/riaps-integration/tree/master/riaps-bbbruntime

#pre-requisite: SD card has base image.

def install_riaps():
    """apt-get update of RIAPS packages"""
    sudo('apt-get install rdate')
    sudo('rdate -n -4 time-a.nist.gov')
    sudo('apt-get update')
    sudo('apt-get install riaps-externals-armhf riaps-core-armhf riaps-pycom-armhf riaps-systemd-armhf riaps-timesync-armhf -y')
    #setEnvVars()
    #
    run('echo "installed RIAPS platform"')

def update_riaps():
    '''Update riaps platform on existing BBBs'''
    sudo('apt-get update')
    sudo('apt-get install "riaps-*" 2>&1 | tee install-riaps-update-bbb.log')
    run('echo "updated RIAPS platform"')

def setEnvVars():
    '''Set the RIAPSAPPS environment variable on btfs apps partition'''
    #TO DO: SET PATH PROPERLY FOR BTFS IMAGE
    run('export RIAPSAPPS=/...')
    run('export RIAPSHOME=/...')
    pass


def start_services():
    ''' start systemd riaps services'''
    pass
    #

def stop_services():
    ''' start systemd riaps services'''
    pass
