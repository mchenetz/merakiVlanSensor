import requests


class merakivlansensor:



    def __init__(self, merakiAPIKey, network):
        self.headers = {
            'X-Cisco-Meraki-API-Key': merakiAPIKey
        }
        self.base = 'https://api.meraki.com/api/v0/'
        self.network = network
    def getVlans(self):
        return requests.get(self.base + 'networks/'+self.network+'/vlans', headers=self.headers).json()

if __name__ == '__main__':
    mvlan = merakivlansensor()

    for vlan in mvlan.getVlans():
        print (vlan['name'] + ':', vlan['id'])
