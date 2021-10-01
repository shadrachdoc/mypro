provider "aws" {
         region = "us-east-1"
}

resource "aws_instance" "vm"{
         ami = "ami-087c17d1fe0178315"
         subnet_id ="subnet-0cc1faee8763b3d25"
         instance_type = "t3.micro"
         tags = {
                Name = "my-first-code"
    }
}
