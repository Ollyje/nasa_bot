from openai import AzureOpenAI
import os
import requests
import json

client = AzureOpenAI(
	api_key = os.getenv("AZURE_KEY"),
	api_version = "2023-10-01-preview",
	azure_endpoint = os.getenv("AZURE_ENDPOINT")
)

with open('nasakey.txt', 'r') as nasa_file:
    nasa_key = nasa_file.read().strip()


messages = [
	# {"role": "system", "content": "Respond to everything a short etheral mysterious poem about the speeds of Coronal Mass Ejections"},
	{"role": "user", "content": "Find the speed of the latest Coronal Mass Ejections in miles per hour"}
]

def cme_speed(cme_date, mph):
	url = f"https://api.nasa.gov/DONKI/CME?startDate={cme_date}&endDate={cme_date}&api_key={nasa_key}"
	print(url)
	response = requests.get(url)
	data = response.json()
	speed = [cme['speed']for cme in data if cme['activityID'] == cme_date][0]
	return f"The current speed of {cme_date} is {speed} {mph}"

functions = [
	{
		"type": "function", 
		"function": {
			"name": "get_speed",
			"description": "Gets the speed of a coronal mass ejection in miles per hour",
			"parameters": {
					# letting chatgpt know that it's geting key-value pairs
				"type": "object",
				"properties": {
					"cme_date": {
						"type": "string",
						"description": "The date of the coronal mass ejection i want to look up"
					},
					"mph": {
						"type": "string",
						"description": "The speed metric for converting the speed of coronal mass ejections. Use the official abbreviation for Miles Per Hour."
					}

				},
				"required":["cme_date", "mph"]
			}

		}
	}

]

response = client.chat.completions.create(
	model = "GPT-4",
	messages = messages,
	tools = functions,
	# auto means chatgpt decides when to use external functions
	tool_choice = "auto"
)

# print(response.choices[0].message)
response_message = response.choices[0].message 
gpt_tools = response.choices[0].message.tool_calls

if gpt_tools:
	available_functions = {
			"get_speed": cme_speed
	}

	messages.append(response_message)
	for gpt_tool in gpt_tools:
		function_name = gpt_tool.function.name
		function_to_call = available_functions[function_name]
		function_parameters = json.loads(gpt_tool.function.arguments)
		function_response = function_to_call(function_parameters.get('cme_date'), function_parameters.get('mph'))
		print(function_response)

else:
	print(response.choices[0].message.content)