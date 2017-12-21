IF=${1:=eth0}

mapfile -t IPs < <(sudo arp-scan -I $IF --localnet)
IPs=("${IPs[@]::${#IPs[@]}-3}");

for ip in "${IPs[@]:3}"
do
  echo $ip | cut -d " " -f1
done
