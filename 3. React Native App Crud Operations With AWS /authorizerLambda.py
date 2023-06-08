import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    auth = 'Deny'
    if event['authorizationToken'] == 'RedshiftAws':
        auth = 'Allow'
    else:
        auth = 'Deny'
    authResponse = {
        'principalId': 'RedshiftAws',
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Resource': ['arn:aws:execute-api:ap-south-1:awsAccountID:38g303h2uh/*/*'],
                    'Effect': auth
                }
            ]
        }
    }
    return authResponse
