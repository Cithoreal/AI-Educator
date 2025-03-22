# AI-Educator

Runs on openAI API

Open-WebUI included as a submodule in the front end
when cloning use 
git clone --recurse-submodules 

run frontend with the following.
docker run -d -p 3000:8080 -e OPENAI_API_KEY=your_secret_key -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

Worked alongide ChatGPT for project creation and structure. 

Using the sample code ChatGPT gives me to build the project. I'm going over the code line by line, typing it myself into the files. The exact way GPT is setting things up isn't the way I intend things so the files will end up changing over commits. Using the files to set up the project is very useful though, and will allow me to get a base template running so I can focus on implementing my vision from there.

Chat Source: https://chatgpt.com/share/67de0d7e-339c-800b-ab50-ef55725a53eb