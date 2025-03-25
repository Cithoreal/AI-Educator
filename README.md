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

Need to set up the agent/pipeline in open web ui properly. Pretty shakey on my concepts here and need to learn and follow some tutorials so I know what I'm doing. Once I have all the basics set up I can focus on the application itself.

I thought using open web ui would streamline the development of this application by using an existing front end so I could focus on backend development and fucntionality, but it turned out that learning how to use and develop for open web ui was the most intensive part of this application.

running pipelines docker container

Even though I spent a lot of time learning langchain, I'm starting to think I should use all of Open-WebUI's built in features to build this project before the deadline. I was hoping to keep the application relatively decoupled from the front end so I could reasonably reuse my progress and eventually build a dedicated and specialized front end for it, but Open-WebUI has all the tools I want to use integrated and it makes more sense to rely on them in the time I have left.