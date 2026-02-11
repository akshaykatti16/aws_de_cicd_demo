variable "region" {
  type = string
}

variable "script_bucket" {
  type = string
}

variable "glue_role_arn" {
  type = string
}

variable "lambda_role_arn" {
  type = string
}

variable "step_function_role_arn" {
  description = "Existing Step Functions execution role ARN"
  type        = string
}