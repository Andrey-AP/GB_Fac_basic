import json


def red_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as r_file:
        for str_f in r_file:
            yield str_f


def json_ls(file_path):
    aver_prof = 0.0
    firm_counter = 0
    out_ls = []
    fr_dic = {}
    for n_str in red_file(file_path):
        name, form, revenue, costs = n_str.split(' ')
        prof = float(revenue) - float(costs)
        fr_dic[name] = prof
        if prof > 0:
            firm_counter += 1
            aver_prof += prof
    out_ls.append(fr_dic)
    out_ls.append({'average_profit': aver_prof/firm_counter})
    return out_ls


def write_to_json_file(out_ls):
    with open("text_77_1.json", 'w', encoding='UTF-8') as js_out:
        json.dump(out_ls, js_out, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    file_name = "text_7.txt"

    write_to_json_file(json_ls(file_name))
