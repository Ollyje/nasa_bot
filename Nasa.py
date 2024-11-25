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
	{"role": "system", "content": "Respond to everything a short etheral mysterious poem about the speeds of Coronal Mass Ejections"},
	{"role": "user", "content": "Find the speed of a Coronal Mass Ejections on a specific day"}

]

date = "2018-01-03"

def nasa_cme(cme_date):
	url = f"https://api.nasa.gov/DONKI/CME?startDate=[{date}&endDate={date}&api_key={nasa_key}"
	response = requests.get(url)
	data = response.json()
	print(url)
	# current_price = [coin['current_price'] for coin in data if coin['id'] == crypto_name][0]
	# return f"The current price of {cme_date} is {current_price} {fiat_currency}"


functions = [
	{
		"type": "function", 
		"function": {
			"name": "cme_speed",
			"description": "Gets the speed of a coronal mass ejection on a specific day",
			"parameters": {
				# letting chatgpt know that it's geting key-value pairs
				"type": "object",
				"properties": {
					"cme_date": {
					"type": "string",
					"description": "The date that i want to look up"

					},
					}
				},
				"required":["cme_date"]
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

response_message = response.choices[0].message 

# if chatgpt doesn't need help, this will be None
gpt_tools = response.choices[0].message.tool_calls

# if gpt_tools is not none
# gpt_tools is a list!
if gpt_tools:

	# set up a 'phonebook', if we see a funiton name, we need to tell our code which function to call
	available_functions = {
			"cme_speeds": cme_speed
	}

	messages.append(response_message)
	for gpt_tool in gpt_tools:
		# figure out which friend to call in the phonebook
		function_name = gpt_tool.function.name
		# looking up funciton name in phonebook
		function_to_call = available_functions[function_name]
		# need to get the parameters for the funciton
		function_parameters = json.loads(gpt_tool.function.arguments)
		function_response = function_to_call(function_parameters.get('cme_speeds'))
		messages.append(
			{
				"tool_call_id": gpt_tool.id,
				"role": "tool",
				"name": function_name,
				"content": function_response
			}
		)
		second_response = client.chat.completions.create(
			model = "GPT-4",
			messages=messages
		)
		print(second_response.choices[0].message.content)

else:
	print(response.choices[0].message.content)

# print(response.choices[0].message)

