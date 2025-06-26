# awsglue

Solution has three parameters:
* BRONZE_S3BUCKET - specifies brone bucket for relevant environment
* silver_s3bucket - specifies silver bucket for relevant environment
* source_supplier - specifies source relevant environment

## Dev

Dev code is maintained in dev folder of bucket https://aws-glue-assets-632234552657-eu-north-1.s3.eu-north-1.amazonaws.com/scripts/

All relevant jobs should be first created specyfing correct configuration.  Job name should be prefixed with DEV, job file name should be in original name without dev prefix.
Job folder path should be from dev

## Prod

Prod code is maintained in prod folder of bucket https://aws-glue-assets-632234552657-eu-north-1.s3.eu-north-1.amazonaws.com/scripts/

All relevant jobs should be first created specyfing correct configuration.  Job name should be with no prefix, job file name should be in original name without prefix.
Job folder path should be from prod.  

## Source control

Within source control you can find json file describing each job as configured in dev.
dev branch contains dev code released into dev setup with dev jobs. Release is automatic and on every checkin of code, new version is released into dev.
Any configuraiton changes must be handled manually.

In order to release into live, check all code into dev and create a pull request from dev into master.  On completion of pull request code deployment pipeline will be triggered to release the code into prod.

