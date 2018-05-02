#fab -f configCluster.py -H $1:2222 update

input=$2
MODE=${input:="default"}
if [ "default" == "$MODE" ]; then

  fab -H $1:2222 runCommand:'sudo apt autoclean'

  fab -H $1:2222 runCommand:'sudo apt autoremove'

  fab -f configCluster.py -H $1:2222 putInterfaces

  fab -f configCluster.py -H $1:2222 runInterfaces

#elif [ "$MODE" == "restart" ]; then
  cmd='systemctl restart networking.service'
  fab -H $1:2222 runCommand:"sudo $cmd"

elif [ "$MODE" == "test" ]; then
  fab -H $1:2222 runCommand:'hostname'

  fab -H $1:2222 runCommand:'hostname -I'

  fab -H $1:2222 runCommand:'echo 1 >> /sys/class/leds/beaglebone\:green\:usr2/brightness'

  fab -H $1:2222 runCommand:'read -n1 -p "Check led : Press CTRL-C to continue"'

	fab -H $1:2222 runCommand:'echo 0 >> /sys/class/leds/beaglebone\:green\:usr2/brightness'

  fab -H $1:2222 runCommand:'route'

  fab -H $1:2222 runCommand:'ping -c 4 8.8.8.8'

  fab -H $1:2222 runCommand:'ping -c 4 10.1.1.198'

  fab -H $1:2222 runCommand:'dpkg -l | grep riaps'

elif [ "$MODE" == "update" ]; then
# for some reason must use 172 address, update fails when using hostname
  fab -H $1:2222 runCommand:'sudo apt-get remove ‘riaps-*’'

  fab -H $1:2222 runCommand:'sudo apt autoclean'

  fab -H $1:2222 runCommand:'sudo apt autoremove'

  #fab -H $1:2222 runCommand:"sudo apt -y install 'riaps-*'"

  fab -H $1:2222 runCommand:'sudo apt update'

  fab -H $1:2222 runCommand:'sudo apt-get -y install rdate'

  fab -H $1:2222 runCommand:'sudo rdate -n -4 time-a.nist.gov'

  fab -H $1:2222 runCommand:'sudo apt update'

  fab -H $1:2222 runCommand:"sudo apt -y install 'riaps-*'"

elif [ "$MODE" == "version"]; then

  fab -H $1:2222 runCommand:'dpkg -l | grep riaps'
  #statements

fi
