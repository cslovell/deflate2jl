# Tool to transform .deflate files to json lines format
A simple docker-compose this tool to transform data from the NYU ache crawler in the FILE format to the JSON LINES format required by the DIG crawler. 

## How to use this tool
To use this tool, clone the repository to your computer. Docker and docker-compose are both required. You will also require a working internet connection.

Once you have cloned this repository, nagivate to the directory. 

Copy the data to be transformed to the "data" folder. Sample data is included in the format desired. 

Once all the files have been copied, enter "docker-compose up" to run the tool. 

this will open a simple webserver that does two things: 

on http://localhost:5000/generate_file/ this builds the json lines file and tells you what's in it

on http://localhost:5000/get_jl/ this will download the file as output.jl




