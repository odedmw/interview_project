def get_requirements(file_path, found_modules = [], files_read = {} ):
    files_read[file_path] = True

    with open(file_path, "r") as file:
        line = file.readline()

        while line:
            if line[:3] == "-r ":
                sub_file_name = line[3:].strip()

                if sub_file_name not in files_read and "requirements" in sub_file_name:
                    get_requirements(sub_file_name, found_modules, files_read)

                line = file.readline()
                continue

            module_name = line.split("==")[0]

            if module_name not in found_modules:
                found_modules.append(module_name)

            line = file.readline()

    return ",".join(found_modules)
