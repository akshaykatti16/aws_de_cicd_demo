provider "aws" {
  region = var.region
}

###################
# ORDERS JOB
###################
resource "aws_s3_object" "orders_script" {
  bucket = var.script_bucket
  key    = "dev/orders/job.py"
  source = "../../glue-scripts/dev/orders/job.py"
  etag   = filemd5("../../glue-scripts/dev/orders/job.py")
}

module "orders_glue_job" {
  source = "../../modules/glue-job"

  job_name        = "orders-dev"
  script_location = "s3://${var.script_bucket}/dev/orders/job.py"
  role_arn        = var.glue_role_arn

  default_arguments = {
    "--env"       = "dev3"
    "--job_type"  = "INCRMNTL"
    "--config"    = "s3://${var.script_bucket}/dev/orders/config.json"
  }
}

###################
# CUSTOMERS JOB
###################
resource "aws_s3_object" "customers_script" {
  bucket = var.script_bucket
  key    = "dev/customers/job.py"
  source = "../../glue-scripts/dev/customers/job.py"
  etag   = filemd5("../../glue-scripts/dev/customers/job.py")
}

module "customers_glue_job" {
  source = "../../modules/glue-job"

  job_name        = "customers-dev"
  script_location = "s3://${var.script_bucket}/dev/customers/job.py"
  role_arn        = var.glue_role_arn

  default_arguments = {
    "--env"       = "dev"
    "--job_type"  = "full"
    "--config"    = "s3://${var.script_bucket}/dev/customers/config.json"
  }
}

###################
# PAYMENTS JOB
###################
resource "aws_s3_object" "payments_script" {
  bucket = var.script_bucket
  key    = "dev/payments/job.py"
  source = "../../glue-scripts/dev/payments/job.py"
  etag   = filemd5("../../glue-scripts/dev/payments/job.py")
}

module "payments_glue_job" {
  source = "../../modules/glue-job"

  job_name        = "payments-dev"
  script_location = "s3://${var.script_bucket}/dev/payments/job.py"
  role_arn        = var.glue_role_arn

  default_arguments = {
    "--env"       = "dev5"
    "--job_type"  = "changedatacapture"
    "--config"    = "s3://${var.script_bucket}/dev/payments/config.json"
  }
}
