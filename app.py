import openai

openai.api_key = 'YOUR_API_KEY' #not sure if they are needed right now

def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        input_data = file.read()

    # Call the OpenAI API to get the response / Still need to cehck how to get it from APIGEE Endpoints
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_data,
        temperature=0.7,
        max_tokens=100
    )

    with open(output_file, 'w') as file:
        file.write(response.choices[0].text)

if __name__ == "__main__":
    input_file = "data.txt"
    output_file = "output.txt"

    process_data(input_file, output_file)
    print(f"Output written to {output_file}.")
