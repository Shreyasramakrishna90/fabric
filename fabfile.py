import fabric.api as fabi
import fabric.operations as fop
import re
from config import *

fabi.env.password = 'riaps'
fabi.env.sudo_password = 'riaps'

fabi.env.key_filename = '~/.ssh/cluster_rsa'

@fabi.parallel
def runCommand(command):
	"""run with fab -R '<role to run command on, e.g c2_1>' runCommand:<command to run>
		or to run on a specific host: fab -H '10.0.2.194:2222' runCommand:'hostname'"""
	results = ''
	#with fabi.hide('output', 'running', 'warnings', 'aborts'), fabi.settings(warn_only=True):
	with fabi.hide('warnings', 'aborts'), fabi.settings(warn_only=True):
		results = fabi.run(command)
	#print(results)

def shutdown():
	fabi.sudo("shutdown -r +1")
