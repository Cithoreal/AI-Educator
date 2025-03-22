# AI-Educator

Runs on openAI API

Open-WebUI included as a submodule in the front end
when cloning use 
git clone --recurse-submodules 

run frontend with the following.
docker run -d -p 3000:8080 -e OPENAI_API_KEY=your_secret_key -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

