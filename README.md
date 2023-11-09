# docker-godaddy-ddns
Raspberry Pi Docker image to provide a DDNS service for godaddy domains. Uses the GoDaddy REST API to update the given domain's DNS IP address to the public IP address of the host it is executing on. Performs a check every 10 minutes, but you can alter this if you like by modifying /etc/cron.d/godaddy-ddns inside the container.

## Running
First, get a GoDaddy developer key & secret from https://developer.godaddy.com/keys/. Log in with your GoDaddy account then generate the API key/secret. Note that the very first time you do this, it will be created as .Test. environment (seen at the time of writing). Go back to the same page again or click on the .Keys. top menu then generate a new .Production. API key/secret instead.

### In Docker
Update IPV4 address for single mydomain.com
```
sudo docker run -d --name=ddns --restart=always \
	-e "GODADDY_KEY=<YOUR_KEY>" \
	-e "GODADDY_SECRET=<YOUR_SECRET>" \
	-e "GODADDY_DOMAIN=mydomain.com" \
	loganavatar/rpi-godaddy-ddns
```

Update IPV4 address for mysubdomain.mydomain.com
```
sudo docker run -d --name=ddns --restart=always \
        -e "GODADDY_KEY=<YOUR_KEY>" \
        -e "GODADDY_SECRET=<YOUR_SECRET>" \
        -e "GODADDY_DOMAIN=mydomain.com" \
        -e "GODADDY_TYPE=A" \
        -e "GODADDY_NAME=mysubdomain" \
        loganavatar/rpi-godaddy-ddns
```

### In Kubernetes
Download and edit the k8s-deploy.yml file locally to use your Key/Secret/Domain, and add Type/Name if doing a subdomain.

When you have a finished editing the k8s-deploy.yml file, run this command
```
kubectl apply -f k8s-deploy.yml
```

## Building
sudo docker build --rm -t loganavatar/rpi-godaddy-ddns .

## Credit
Forked from https://github.com/peteward44/docker-godaddy-ddns
Uses modified script from http://teanazar.com/2016/05/godaddy-ddns-updater/
testing
