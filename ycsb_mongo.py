import subprocess
import sys

workloads = ['workloada', 'workloadb', 'workloadc', 'workloadd', 'workloade', 'workloadf']

# Function to execute YCSB commands
def run_ycsb_command(workload):
    command = "./bin/ycsb.sh load jdbc mongodb -s -P workloads/" + workload + " > " + workload + "_mongo.txt"
    ret_code = subprocess.call(command, shell=True)
    if ret_code != 0:
        sys.exit("Error executing YCSB command for workload: " + workload)

# Function to delete data from Mongo DB
def delete_data_from_table():
    command = 'mongo --eval "db.getSiblingDB(\'ycsb\').dropDatabase();"'
    ret_code = subprocess.call(command, shell=True)
    if ret_code != 0:
        sys.exit("Error deleting data from MySQL table")

# Loop through workloads
for workload in workloads:
    run_ycsb_command(workload)
    delete_data_from_table()

