#!/usr/bin/env python



##################################################

#  VM Snapshot Creation & Cleanup Script 	     #

# Created by: Cole Lavallee                      #

# Date: 1/21/2014                                #

##################################################



from pysphere import VIServer
from datetime import date

today = date.today()

snapshot_name = vm_name + str(today)

server = VIServer()

server.connect(vcenter, vcuser, password)

# Actions:

# 1. Shut the VM off

# 2. Delete existing VM snapshots

# 3. Create a new snapshot with VM name and current date.

# 4. Turn the VM back on


vm = server.get_vm_by_name('vm_name')


	if vm.is_powered_on():

		vm.power_off()



	if vm.is_powered_off():

		try:

			vm.delete_current_snapshot(remove_children=True)

		except:

			print "No snapshot exists, creating new snapshot"

	

	try:

		vm.create_snapshot(snapshot_name)

	except:

		print "Snapshot creation failed"

try:

	if vm.is_powered_off():

		vm.power_on()
except: 

		print "VM could not power on or is already powered on"

