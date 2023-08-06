rm -rf package
#pip3 install --target ./package requests==2.28.2
pip3 install --target ./package opensearch-py
pip3 install --target ./package requests_aws4auth
cd package
zip -r ../lambda.zip .

cd ..
zip -g lambda.zip s3tosearch.py