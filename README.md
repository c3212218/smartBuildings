# smartBuildings
Repository for storing configuration and data files for Big Data Management and Analytics Framework for of IoT enabled Smart Buildings. The complete setup was implemented on Cloudera 5.4.2 Virtual Machine environment.

## Code for Python IoT Sensor Application
The code for Python IoT sensor application is in the folder 'Python_IoT_app'. The files inside the folder were developed and run in Pycharm IDE. The application sends data to an elasticsearch index and also to Flume agents. Start this application within Pycharm IDE after all the below mentioned steps are initiated already.

## Flume configuration files
The code for Flume configuration agents is in the folder 'flume_conf_files'. There are ten files for ten Flume agents which accept data coming from the the Python IoT sensor applicaton. These Flume agents store data into HDFS. Run all the Flume agents before running the Python IoT Sensor Application.
To run the Flume agents, consider the below command to run one Flume agent with configuration file named 'sensor1000.conf' that is located in /home/cloudera/flume/conf 

flume-ng agent --name a1  --conf /home/cloudera/flume/conf  --conf-file /home/cloudera/flume/conf/sensor1000.conf


## Pyspark code
The Pyspark code is in the folder 'pyspark_code'. This code reads the IoT sensor data being stored in HDFS. Make sure that the pyspark code is running before starting the Python IoT sensor application.

## Elasticsearch and Kibana
Elasticsearch and Kibana were downloaded from web onto the Cloudera VM where these services were started. Elasticsearch and Kibana can both be downloaded from the website and while working in Cloudera VM, they just need to be extracted out of the zip files and they should be ready to use. Make sure that Elasticsearch and Kibana are running before starting the Python IoT sensor Application. For Elasticsearch we installed kopf plugin as we found it very convenient to look at the indeces and documents within indeces in Elasticsearch. Since the Python IoT sensor application sends the data to Elasticsearch in near-real time, we used this plugin for debugging as we could see documents being uploaded into indeces in near-real time.
The kopf plugin can be found here:
https://github.com/lmenezes/elasticsearch-kopf

## Instructions for setting up the pipeline
1-	Download the Cloudera VM from one drive https://studentutsedu-my.sharepoint.com/:u:/g/personal/12532293_student_uts_edu_au/EUqYnb7DEtBDi9w35eSgkSsBlJjR6pSNPcZqZVpQRvsHIg?e=A5Q2Ik 

2-	The Password for the download is IoTSmartBuildings

3-	Download and install VMWare workstation player.

4-	Open the VM in VMWare workstation player with at least 8 GB (12GB recommended) of RAM dedicated to the VM.

5-	Open the terminal 

6-	Open Pycharm using the following commands 
-	 cd Downloads/pycharm-community-2016.1.5/bin
-	./pycharm.sh

7-	Run flume agents. We have ten flume agents running so we need to run the following ten commands. The configuration files are located in /home/cloudera/flume directory. The conf are named sensor100.conf, sensor200.conf, sensor300.conf, sensor400.conf, sensor500.conf, sensor600.conf, sensor700.conf, sensor800.conf, sensor900.conf and sensor1000.conf. Run each flume agent in a new terminal. Hence run the following ten flume agents in ten different terminals.
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor100.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor200.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor300.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor400.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor500.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor600.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor700.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor800.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor900.conf
-	flume-ng agent --name a1 --conf /home/cloudera/flume/conf --conf-file /home/cloudera/flume/conf/sensor1000.conf

8-	Run Elasticsearch. Before running elasticsearch, download kopf plugin for Elasticsearch. It can be downloaded from https://github.com/lmenezes/elasticsearch-kopf. The installation instructions are available on the download site. Open Terminal and type the following commands:
-	cd elasticsearch-1.5.2
-	./bin/elasticsearch 

9-	Open elasticsearch using the kopf plugin by opening up the browser and entering the following in the address bar: http://localhost:9200/_plugin/kopf/#!/cluster 

10-	Run Kibana. Open a new terminal and enter the following commands:
-	 cd kibana-4.0.2-linux-x64
-	./bin/kibana

11-	Open Kibana dashboard by entering the following in the address bar: http://localhost:5601 

12-	After opening the kibana tool from the web browser. Go to Settings tab and make sure index named ‘iot’ is selected. Go to the discover tab and you will see historical values of the sensors.

13-	Run PySpark code. In order to run the PySpark code, open another terminal and type the following command and hit enter
-	Pyspark

14-	Copy the code from the PySpark folder from the github repo and paste it into the PySpark terminal.

15-	Run the Python IoT application from PyCharm. To do this, right click on any of the sensor100.py – sensor1000.py files and click run.

16-	This will complete the pipeline, the pycharm code will start generating data, flume agents will ingest this data into HDFS, the PySpark code will do the analysis on the received data. The analysis results can be seen in the terminal window. The data will be stored both in HDFS and Elasticsearch. To stop PySpark code, press Ctrl + C to kill the process.

17-	To view data in HDFS, open the browser and click ‘Hue’ tab on the top left hand side of the browser. If the dialog box appears for the username and password, just press enter. Click on ‘job browser’ tab on the top right side of the browser. Open the folder named ‘data’. This is the folder where flume agents store the data from IoT sensors into HDFS.

18-	To view data in Elasticsearch, Open the Kibana webpage and go to the discover tab to view the incoming data. New visualizations and dashboards can be created in Kibana by following its online documentation. 

19-	To stop the pipeline you can Ctrl + C on individual terminals or simply shut down the VM.




