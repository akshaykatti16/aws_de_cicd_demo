data "aws_caller_identity" "current" {}

module "ord_cust_pipeline_sfn" {
  source    = "../../modules/step-function"
  name      = "ord_cust_pipeline-dev"
  role_arn = var.step_function_role_arn

  definition = templatefile(
    "${path.module}/../../step-functions/dev/orders_customers_job.asl.json",
    {
      region     = var.region
      account_id = data.aws_caller_identity.current.account_id
    }
  )
}