import json
from .utils import get_files_path


def get_user_info(path):
    data = path.split('/')
    user = data[-1][:len("_replies.json") * - 1]
    return data[2], user


def main():
    periodos = ["Campaña", "Precampaña", "Poscamapaña"]
    for periodo in periodos:
        print("Reestructurando", periodo)
        replies_paths = get_files_path("tweets/" + periodo, "replies.json")
        for path in replies_paths:
            role, username = get_user_info(path)
            with open(path, 'r') as f:
                replies_raw = f.readlines()
            for line in replies_raw:
                line = line.strip()
                data = json.loads(line)
                if len(data["replies"]) > 1 and isinstance(data["replies"], list):
                    data["_id"] = str(data["id"])
                    del data["id"]
                    data["tweet"] = data["replies"].pop(0)
                    data["rol"] = role
                    data["usuaria"] = username
                    data["periodo"] = periodo.lower()
                    with open("neotweets/" + username + ".json", 'a') as f:
                        json.dump(data, f)
                        f.write('\n')


if __name__ == '__main__':
    main()
