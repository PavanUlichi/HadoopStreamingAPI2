# project03
The given data set is available at openlibrary.org.
We are going to analyze this data using Hadoop.

Dump location: http://openlibrary.org/data/ol_dump_works_latest.txt.gz

## Below are the instructions for using this code on hadoop server which supports HadoopStreamingAPI

As it has huge data we are going to analyse it using hadoop streaming API

Go to home directory

First, clone these repository either using https or ssh on to the hadoop server
After successful clone, you can see both mapper and reducer programs
Then run the below command on hadoop cluster by making small modifications in  output path where you want to store 

 hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/openlibrary/ol_dump_works_latest-20161202.txt -output /users-cloud-16fs/ulichitr/project03-out/output2 -mapper ~/project03/mapper.py -reducer ~/project03/reducer.py -file ~/project03/{mapper,reducer}.py

##Output
After successful execution of hadoop jobs, the output statistics can be viewed in hdfs using below command

hdfs dfs -cat /users-cloud-16fs/ulichitr/project03-out/output2/part-00000

maximum_subject	History

minimum_subject	{Plants

count_median	1

count_average	34
