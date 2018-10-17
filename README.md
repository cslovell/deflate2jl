# Tool to transform .deflate files to json lines format
A simple docker-compose this tool to transform data from the NYU ache crawler in the FILE format to the JSON LINES format required by the DIG crawler. 

## How to use this tool
To use this tool, clone the repository to your computer. Docker and docker-compose are both required. You will also require a working internet connection.

Once you have cloned this repository, nagivate to the directory. 

Copy the data to be transformed to the "data" folder. Sample data is included in the format desired. 

Once all the files have been copied, enter "docker-compose up" to run the tool. 

This will produce an output.jl file with the required json lines file. 



