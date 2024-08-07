def write_output_to_file(result, output_file_name="result"):
    file = open(output_file_name, 'w')
    file.write(str(result))
    file.close()
