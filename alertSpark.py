from merakivlansensor import merakivlansensor
from ciscosparkapi import CiscoSparkAPI
import os
import time

#Setup Meraki Vlan Sensor
mvlan = merakivlansensor(os.environ['meraki-token'], os.environ['meraki-network'])

#Setup Spark API with token
api = CiscoSparkAPI(access_token=os.environ['access-token'])

allVlans = []
firstRun = True # On first gathering of VLANs will not Alert

while True:
    print("Checking VLANs...")
    for vlan in mvlan.getVlans():
        print (vlan['name'] + ':', vlan['id'])
        if vlan['id'] in allVlans:
            pass
        else:
            if firstRun:
                allVlans.append(vlan['id'])
            else:
                allVlans.append(vlan['id'])
                api.messages.create(roomId=os.environ['meraki-roomid'],
                                    text='New VLAN added: ' + str(vlan['id']))
    firstRun = False
    time.sleep(5) #Run check every 5 seconds
