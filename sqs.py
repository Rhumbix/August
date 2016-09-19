from boto3.session import Session
session = Session()
client = session.client('sqs')
response = client.get_queue_url(QueueName='Pipi')
url = response['QueueUrl']
#messages = client.receive_message(
     #QueueUrl=url,
     #AttributeNames=['All'],
     #MaxNumberOfMessages=1,
     #VisibilityTimeout=60,
     #WaitTimeSeconds=5
#)
message = 'Hello world!'
response = client.send_message(
    QueueUrl=url,
    MessageBody=message,
    DelaySeconds=0,
)
