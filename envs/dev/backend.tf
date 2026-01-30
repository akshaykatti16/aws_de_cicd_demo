terraform {
  backend "s3" {
    bucket = "nagarro-terraform-state"
    key    = "glue/dev/terraform.tfstate"
    region = "ap-south-1"
  }
}
