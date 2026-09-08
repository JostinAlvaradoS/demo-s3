output "web_bucket" {
  description = "Bucket que sirve el front compilado"
  value       = aws_s3_bucket.web.bucket
}
