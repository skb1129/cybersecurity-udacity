##################################################
# Ignore this until you reach Course 3 of Term 1 #
##################################################

resource "aws_s3_bucket" "server-files-bucket-suryakantbansal" {
  bucket = "server-files-bucket-suryakantbansal"
  acl    = "private"
}

resource "aws_s3_bucket_object" "server-files" {
  bucket = "${aws_s3_bucket.server-files-bucket-suryakantbansal.bucket}"
  key    = "server-files.tar.gz"
  source = "./server_files.tar.gz"
}

resource "aws_s3_bucket_object" "boot-file" {
  bucket = "${aws_s3_bucket.server-files-bucket-suryakantbansal.bucket}"
  key    = "bootstrap.sh"
  source = "./webserver_scripts/bootstrap.sh"
}
