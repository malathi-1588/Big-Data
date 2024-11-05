## Links ##
1. VPC & EC2 Lab : https://youtu.be/AsSQb--MNXA (no audio)
2. Route 53 Labs : https://youtu.be/-ndsfa-6GMI (no audio)
3. IAM Concept & Lab : https://youtu.be/9asvt7jh27M
# Commands for Hadoop:
start-all.sh

hdfs dfs -mkdir /word_count_in_python

hdfs dfs -copyFromLocal /path/to/local/word_count_data.t xt /word_count_in_python/
#hdfs dfs -copyFromLocal /path 1 /path 2 .... /path n /d estination

chmod +x mapper.py reducer.py

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-st reaming-*.jar \\
-input /word_count_in_python/word_count_data.txt \\ -output /word_count_in_python/output \\
-mapper /path/to/mapper.py \\ -reducer /path/to/reducer.py
e.g 
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-st reaming-*.jar \
-input /path/to/input.txt \ (/word_count_in_python/word_ count_data.txt)
-output /path/to/output \ (/word_count_in_python/output) -mapper /path/to/mapper.py \ (/home/dikshant/Documents/m apper.py)
-reducer /path/to/reducer.py (/home/dikshant/Documents/reducer.py)

hadoop jar hadoop_user/share/hadoop/tools/lib/hadoop-st reaming-3.3.6.jar \\
-input /word_count/data.csv \\ -output /word_count/op \\
-mapper mapper.py \\ -reducer reducer.py

![image](https://github.com/user-attachments/assets/0a36bacc-3bd9-4b29-9369-2e14cb031469)
