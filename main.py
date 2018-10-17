import base64, zlib, os, json


if __name__ == "__main__":
    output_file = "output.jl"
    if os.path.exists(output_file):
        append_write = 'a'
        print("File exists, appending records to file...")
    else:
        append_write = 'w'
        print("File doesn't exist, creating new file " + output_file + "...")
    file_count = 0
    line_count = 0
    with open(output_file, append_write) as out:   
        for compressedfilepath in os.listdir("data/"):
            file_count+=1
            with open("data/" + compressedfilepath, "rb") as f:
                decompressed = zlib.decompress(f.read())
                decompressed_and_decoded = decompressed.decode('utf8')
                json_list = decompressed_and_decoded.replace("'", '"').splitlines()
                for line in json_list:
                    line_json = json.loads(line)
                    line_json['content'] = base64.b64decode(line_json['content'])
                    out.write(str(line_json) + '\n')
                    line_count+=1
    print("Read " + str(file_count) + " compressed files and retrieved " + str(line_count) + " pages to json lines file.")


