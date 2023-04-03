# SP-API-LWA-Rotation


## Background 

To reduce the risk of exposed and compromised credentials, starting from [February 6th, 2023](https://developer-docs.amazon.com/sp-api/docs/rotating-your-apps-lwa-credentials), the SP-API Services require all developers to rotate their “Login With Amazon” (LWA) credentials every 180 days. If the SP-API LWA credentials are not updated before the expiration target date, the API integration will lose access to the SP-API. All Amazon SP-API Developers are required to follow secure coding standards to follow Personal Identifiable Information (PII) requirements from the [Data Protection Policy](https://sellercentral.amazon.com/mws/static/policy?documentType=DPP&locale=en_US). Credentials include, but are not limited to the encryption key, secret access key, password, and other sensitive credentials are not supposed to be hardcoded in the code. Based on the requirements mentioned above, Amazon is introducing a secure way to utilize Amazon AWS Systems Manager Parameter Store, AWS Key Management Service (KMS), Amazon EventBridge, and Amazon SNS to rotate your SP-API credentials in a timely manner. The overall architecture can be found below:

![architecture](./static/secure-lwa.png)


## Introduction

This project includes the code repo for building a Lambda LWA token exchanger utilizing the Parameter Store and KMS Services and the Implementation Guide.

```.
├── BLOG.md     ----- Implementation Guide
├── README.md       ----- Project README
├── lambda-lwa      ----- Lambda Function for the LWA Toekn Exchangeer
│   ├── lwa-lambda-exchanger.zip      ---- Lambda Function Zip File
│   ├── lambda_function.py      ----- Lambda Function Python Code File        
│   └── requests        ----- Dependencies
├── static      ----- Static Files
│   ├── auto-rotate.png
│   ├── parameter-store.png
│   ├── secret-manager.png
│   └── secure-lwa.png
└── templates        
    ├── event-bridge-cloudformation.yaml        ---- Rules for EventBridge  
    └── lambda-iam-role-policy.json     ---- IAM Policy for the Lambda to call KMS and System Manager

```

