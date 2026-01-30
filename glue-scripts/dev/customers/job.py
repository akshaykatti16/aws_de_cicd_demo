import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(
    sys.argv,
    ['env', 'job_type', 'config']
)

print("===== CUSTOMERS JOB =====")
print("ENV:", args['env'])
print("TYPE:", args['job_type'])

print("Running FULL refresh of customers table...")
print("Deleting old data and reloading everything")
