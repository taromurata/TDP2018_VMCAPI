${zip-file} = "XXX.zip"
${lambda-arn} = "arn:aws:lambda:xxxxxxx:xxxxxxx:function:xxxxxxxx"

#
# You must configure awscli first to use this script.
# To do it, type `aws configure`
#

Write-Output "> Creating archive ${zip_file}"
Compress-Archive -Path .\alexa-program\* -DestinationPath ${zip-file} -Force
Write-Output "> Done."

Write-Output "> Uploading..."
aws lambda update-function-code --function-name ${lambda-arn} --zip-file "fileb://${zip-file}"
Write-Output "> Done."