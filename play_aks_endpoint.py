import requests
import json
from azureml.core import Workspace, Webservice
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig

ws = Workspace.from_config()
service = Webservice(workspace=ws, name='edusohomlops-aks')
print(service.scoring_uri)
print(service.swagger_uri)

primary, secondary = service.get_keys()
print(primary)

#token, refresh_by = service.get_token()
#print(token)


# Two sets of data to score, so we get two results back
data = {"data":
        [
            [
                0.038075906,0.050680119,0.061696207,0.021872355,-0.044223498,-0.034820763,-0.043400846,-0.002592262,0.019908421,-0.017646125
            ],
            [
                -0.001882017,-0.044641637,-0.051474061,-0.026327835,-0.008448724,-0.01916334,0.074411564,-0.039493383,-0.068329744,-0.09220405
            ]
        ]
        }
# Convert to JSON string
input_data = json.dumps(data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {primary}'

# Make the request and display the response
resp = requests.post(service.scoring_uri, input_data, headers=headers)
print(resp.text)
