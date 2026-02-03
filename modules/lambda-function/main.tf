resource "aws_lambda_function" "this" {
  function_name = var.function_name
  role 			= var.lambda_role_arn
  handler       = var.handler
  runtime       = var.runtime

  filename         = var.zip_path
  source_code_hash = filebase64sha256(var.zip_path)

  timeout = 300
  memory_size = 512

  environment {
    variables = {
      GLUE_JOB_NAME = var.glue_job_name
    }
  }
}
