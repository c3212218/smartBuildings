# smartBuildings
Repository for storing configuration and data files for Big Data Management and Analytics Framework for of IoT enabled Smart Buildings. The complete setup was implemented on Cloudera 5.4.2 Virtual Machine environment.

## Code for Python IoT Sensor Application
The code for Python IoT sensor application is in the folder 'Python_IoT_app'. The files inside the folder were developed and run in Pycharm IDE. The application sends data to an elasticsearch index and also to Flume agents. Start this application within Pycharm IDE after all the below mentioned steps are initiated already.

## Flume configuration files
The code for Flume configuration agents is in the folder 'flume_conf_files'. There are ten files for ten Flume agents which accept data coming from the the Python IoT sensor applicaton. These Flume agents store data into HDFS. Run all the Flume agents before running the Python IoT Sensor Application.

## Pyspark code
The Pyspark code is in the folder 'pyspark_code'. This code reads the IoT sensor data being stored in HDFS. Make sure that the pyspark code is running before starting the Python IoT sensor application.

## Elasticsearch and Kibana
Elasticsearch and Kibana were downloaded from web onto the Cloudera VM where these services were started. Elasticsearch and Kibana can both be downloaded from the website and while working in Cloudera VM, they just need to be extracted out of the zip files and they should be ready to use. Make sure that Elasticsearch and Kibana are running before starting the Python IoT sensor Application.



