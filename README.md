# SP-API-LWA-Rotation


## Background 

Starting from February 6th, 2023. The SP-API Services required all developers need to rotate their "Login With Amazon" (LWA's)s credential for every 180 days. If the LWA credentials is not updated before the expiry target date, the API integration will lose the access to the SP-API.
To meet this requirement. We propose a way of using AWS System Manager Parameter Store KMS EventBridge and SNS to encrypt the LWA key and a rotation notification services.

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

