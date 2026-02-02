import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(
    sys.argv,
    ['env', 'job_type', 'config']
)

print("===== PAYMENTS JOB =====")
print("ENV --- ", args['env'])
print("TYPE --- ", args['job_type'])

print("Applying CDC logic:")
print("I -> Insert")
print("U -> Update")
print("D -> Delete")
