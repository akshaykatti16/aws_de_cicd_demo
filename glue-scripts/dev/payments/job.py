import sys
from awsglue.utils import getResolvedOptions
import boto3
import logging

args = getResolvedOptions(
    sys.argv,
    ['env', 'job_type', 'config']
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to get secrets from AWS Secrets Manager
def get_secret(secret_name):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        return get_secret_value_response['SecretString']
    except Exception as e:
        logger.error(f"Error retrieving secret {secret_name}: {e}")
        return None

logger.info("===== PAYMENTS JOB =====")
logger.info("ENV --- %s", args['env'])
logger.info("TYPE --- %s", args['job_type'])

# Fetching a secret (replace 'your_secret_name' with the actual secret name)
secret = get_secret('your_secret_name')
if secret:
    logger.info(f"Retrieved secret: {secret}")

logger.info("Applying CDC logic:")
logger.info("I -> Insert")
logger.info("U -> Update")
logger.info("D -> Delete")
