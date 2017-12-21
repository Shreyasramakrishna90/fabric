subnet="$(hostname -I | cut -d " " -f 1 | cut -d "." -f 3)"
echo $subnet

sed -i 's/10.1.[1-9].0/10.1.'"$subnet"'.0/g' ~/Interfaces/configs/interfaces
sed -i 's/10.1.[1-9].1/10.1.'"$subnet"'.1/g' ~/Interfaces/configs/interfaces
# should do a sed on the dhclient.conf file too. So if the ip range changes its ok

cp ~/Interfaces/configs/interfaces /etc/network/interfaces
cp ~/Interfaces/configs/dhclient.conf /etc/dhcp/dhclient.conf
rsync -av --delete ~/Interfaces/configs/.ssh/ ~/.ssh
cp ~/Interfaces/configs/sshd_config /etc/ssh/sshd_config

chmod 600 ~/.ssh/id_rsa
#sed -i "s@$old@$new@" file
