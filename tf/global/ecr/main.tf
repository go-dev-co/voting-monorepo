resource "aws_ecr_repository" "container_repository" {
  name                 = "container-repository"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
