import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['env', 'config'])

print("Orders Glue Job Running")
print("ENV:", args['env'])
print("CONFIG:", args['config'])
