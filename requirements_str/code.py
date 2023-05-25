def get_requirements(file_path, list_passed_files=[], str_modules=""):
    with open(file_path, "r") as file:
        for module in file:
            if "-r " != module[:3]:
                
                if len(str_modules) != 0:
                    str_modules += "," + module.split("==")[0]
                else:
                    str_modules += module.split("==")[0]
            else:
                file_name = module.split(" ")[1].split(".")[0]
                
                if "requirements" in file_name and file_name not in list_passed_files:
                    list_passed_files.append(file_name)
                    new_path = file_path.split("\\")
                    new_path[-1] = module.split(" ")[1].strip("\n")
                    new_path = "/".join(new_path)
                    str_modules = get_requirements(new_path, list_passed_files, str_modules)

    return str_modules
