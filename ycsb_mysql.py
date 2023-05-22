import subprocess
import sys

workloads = ['workloada', 'workloadb', 'workloadc', 'workloadd', 'workloade', 'workloadf']

# Function to execute YCSB commands
def run_ycsb_command(workload):
    command = "./bin/ycsb.sh load jdbc -P ./jdbc-binding/conf/db.properties -P workloads/" + workload + " > " + workload + "_mysql.txt"
    ret_code = subprocess.call(command, shell=True)
    if ret_code != 0:
        sys.exit("Error executing YCSB command for workload: " + workload)

# Function to delete data from MySQL table
def delete_data_from_table():
    command = "mysql -uroot -ppassword -D BenchTest -e 'DELETE FROM usertable;'"
    ret_code = subprocess.call(command, shell=True)
    if ret_code != 0:
        sys.exit("Error deleting data from MySQL table")

# Loop through workloads
for workload in workloads:
    run_ycsb_command(workload)
    delete_data_from_table()

