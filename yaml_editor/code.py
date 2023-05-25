def get_all_key_paths_in_json(yaml_obj, full_yaml, config_input, keep_or_lose , parent_key=''):
    result = []
    if isinstance(yaml_obj, dict):
        if len(config_input) == 1 and list(config_input.keys())[0] in list(yaml_obj.keys()):
            if isinstance(yaml_obj[list(config_input.keys())[0]], list):
                if keep_or_lose:
                    yaml_obj[list(config_input.keys())[0]].append(config_input[list(config_input.keys())[0]])
                else:
                    right_index = 0
                    for index, item in enumerate(yaml_obj[list(config_input.keys())[0]]):
                        if list(item.keys()) == list(config_input.keys()):
                            right_index = index
                    yaml_obj[list(config_input.keys())[0]].remove(yaml_obj[list(config_input.keys())[0]][right_index])
                    yaml_obj[list(config_input.keys())[0]].append(config_input)
            else:
                if keep_or_lose:
                    yaml_obj[list(config_input.keys())[0]] = [yaml_obj[list(config_input.keys())[0]], config_input[list(config_input.keys())[0]]]
                else:
                    yaml_obj[list(config_input.keys())[0]] = config_input[list(config_input.keys())[0]]
        elif len(config_input) > 1 and list(config_input.keys()) == list(yaml_obj.keys()):
            data = full_yaml
            if not keep_or_lose:
                keys = parent_key.split('.')
                for key in keys[:-1]:
                    if str.isdigit(key):
                        key = int(key)
                    data = data.setdefault(key, {}) if isinstance(data, dict) else data[key]
                key = keys[-1]
                if str.isdigit(key):
                    key = int(key)
                data[key] = config_input
            else:
                keys = parent_key.split('.')
                for key in keys[:-1]:
                    if str.isdigit(key):
                        key = int(key)
                    data = data.setdefault(key, {}) if isinstance(data, dict) else data[key]
                if isinstance(data, dict):
                    data[keys[-1]] = [data[keys[-1]], config_input]
                else:
                    data.append(config_input)
        for key, value in yaml_obj.items():
            current_key = f"{parent_key}.{key}" if parent_key else key
            result.append(current_key)
            result.extend(get_all_key_paths_in_json(value, full_yaml, config_input, keep_or_lose, current_key))
    elif isinstance(yaml_obj, list):
        for index, item in enumerate(yaml_obj):
            current_key = f"{parent_key}.{index}"
            result.extend(get_all_key_paths_in_json(item, full_yaml, config_input, keep_or_lose, current_key))
            return parent_key
    return result
