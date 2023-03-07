import json
import os

if __name__ == '__main__':

    path = "/Users/mr.dong/Web3Project/PetsMetadata/Images"  # 文件夹目录
    files = os.listdir(path)
    print(files)


    for file in files:
        nameArr = file.split(".")[0].split("-")
        lv = nameArr[0]
        ind = int(nameArr[1])
        json_dict = {
            "name": "PetTrader #%s" % ind,
            "description": "It is a cute pet trader with chat function that can help you manage your finances on cryptocurrency exchanges.",
            "image": "",
            "attributes": [
                {
                    "trait_type": "lv",
                    "value": "%s" % lv
                }
            ]
        }

    # with open("../config/record.json", "w") as dump_f:
    #     json.dump(load_dict, dump_f)
    #
    # print("加载入文件完成...")