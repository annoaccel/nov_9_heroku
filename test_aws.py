import boto3
import cv2

s3_client = boto3.client("s3")

bucket = "avistosvideobucket"
key = "Double1.mp4"

url = s3_client.generate_presigned_url(
    "get_object", Params={"Bucket": bucket, "Key": key}, ExpiresIn=600
)  # this url will be available for 600 seconds

cap = cv2.VideoCapture(url)

ret, frame = cap.read()
