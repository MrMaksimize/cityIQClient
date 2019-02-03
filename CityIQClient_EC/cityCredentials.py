import os
name = 'San Diego'
uaa = 'https://624eff02-dbb1-4c6c-90bc-fa85a29e5fa8.predix-uaa.run.aws-usw02-pr.ice.predix.io'
eventservice = 'https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/'
metadataservice = 'https://ic-metadata-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/'
mediaservice = 'https://ic-media-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/'
websocket = 'wss://https://ic-websocket-service-sandiego.run.aws-usw02-pr.ice.predix.io'
client = os.environ['IQclient']
secret = os.environ['IQpwd']
parking = 'SD-IE-PARKING'
environment = 'SD-IE-ENVIRONMENTAL'
pedestrian = 'SD-IE-PEDESTRIAN'
traffic = 'SD-IE-TRAFFIC'
video = 'SD-IE-VIDEO'
images = 'SD-IE-IMAGE'
bbox = '33.077762:-117.663817,32.559574:-116.584410'
