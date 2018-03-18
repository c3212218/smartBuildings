import time
threshold_oxygen=14
threshold_smoke=19
threshold_luminosity=16
threshold_garbage=20
while(1):
	dataRDD = sc.textFile("/user/cloudera/data/netcat.*")
	for line in dataRDD.collect():
		id,value,postcode=line.split(",")
		id=int(id)
		value=int(value)
		postcode=int(postcode)
		if(id<201):
			if(value<threshold_oxygen):
				print ("HVAC system " ,id, " turned ON")
			else:
				print("Oxygen level at ",id," OKAY")
		if(200<id<401):
			if(value>threshold_smoke):
				print ("Fire Alarm " ,id-200, " turned ON")
			else:
				print("No fire at " , id-200)
		if(400<id<601):
			if(value>0):
				print ("Parking " ,id-400, " is occupied")
			else:
				print("Parking " ,id-400, " is empty")
		if(600<id<801):
			if(value<threshold_luminosity):
				print ("Lights at " ,id-600, " turned ON")
			else:
				print("Luminosity level at" ,(id-600), " OKAY")
		
		if(id>800):
			if(value>threshold_garbage):
				print ("Garbage at " ,id-800, " is Full")
			else:		
				print("Garbage at " ,id-800, " has space")
	
	time.sleep(10)
