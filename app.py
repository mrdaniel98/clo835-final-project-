from flask import Flask, render_template
import boto3
import os
import logging

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.INFO)

# Environment variables from ConfigMap or run command
bucket_name = os.getenv("S3_BUCKET_NAME", "final-clo835")
background_image_key = os.getenv("BACKGROUND_IMAGE_KEY", "background.jpg")
group_name = os.getenv("GROUP_NAME", "Group-7")
group_slogan = os.getenv("GROUP_SLOGAN", "We Build the Cloud")

# Set up S3 client using credentials passed as env vars or mounted secrets
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

# Download the image to use locally inside the container
local_image_path = f'static/{background_image_key}'

try:
    s3_client.download_file(bucket_name, background_image_key, local_image_path)
    logging.info(f"✔️ Background image downloaded from S3: {bucket_name}/{background_image_key}")
except Exception as e:
    logging.error(f"❌ Failed to download image from S3: {e}")

@app.route("/")
def home():
    return render_template("index.html", group=group_name, slogan=group_slogan, background=background_image_key)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
