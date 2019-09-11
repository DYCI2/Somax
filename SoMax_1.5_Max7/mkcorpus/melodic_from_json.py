import argparse
import json


class MelJsonGenerator:

    def __init__(self):
        pass

    @staticmethod
    def generate_mel_json(filename, is_held):
        mel_dict = dict()

        with open(filename) as jos:
            somax_dict = json.load(jos)
            mel_dict["type"] = somax_dict["type"]
            mel_dict["typeID"] = somax_dict["typeID"]
            mel_dict["size"] = somax_dict["size"]
            mel_dict["name"] = somax_dict["name"]
            mel_dict["data"] = []
            mel_dict["data"].append(dict(somax_dict["data"][0]))
            i = 1
            for d in somax_dict["data"]:
                tmp = dict(d)
                note_tmp = None
                max_pitch = -1
                for d in d["notes"]:
                    p = d["note"][0]
                    if is_held:
                        cond = p > max_pitch
                    else:
                        cond = p > max_pitch and d["note"][1] != 0
                    if cond:
                        max_pitch = int(p)
                        note_tmp = dict(d)
                if max_pitch != -1:
                    if i > 2 and max_pitch == mel_dict["data"][i - 1]["slice"][0]:
                        mel_dict["data"][i - 1]["time"][1] += tmp["time"][0] - mel_dict["data"][i - 1]["time"][0]
                    else:
                        tmp["notes"] = [dict(note_tmp)]
                        tmp["slice"] = [note_tmp["note"][0] % 12, 0]
                        # tmp["time"][0] += note_tmp["time"][0]
                        mel_dict["data"].append(tmp)
                        if i > 0:
                            mel_dict["data"][i - 1]["time"][1] = mel_dict["data"][i]["time"][0] - \
                                                                 mel_dict["data"][i - 1]["time"][0]
                        i += 1
                        # print tmp["slice"][0], mel_dict["data"][i-1]["beat"][0]/4+1, mel_dict["data"][i-1]["beat"][0]

        split_filepath = filename.split(".")
        del split_filepath[-1]

        output_file = ".".join(split_filepath) + "_m.json"

        MelJsonGenerator.dump(output_file, mel_dict)

    @staticmethod
    def dump(filepath, mel_dict):
        with open(filepath, 'w') as jw:
            json.dump(mel_dict, jw)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Makes a melodic version of a standard SoMax json.")
    parser.add_argument('filename', metavar='file', type=str, help='path of the standard SoMax json')
    parser.add_argument('--held', default=True, action='store_true',
                        help='if on, takes account notes even if they were played in a previous state')

    args = parser.parse_args()
    MelJsonGenerator.generate_mel_json(args.filename, args.held)
