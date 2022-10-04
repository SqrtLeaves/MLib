# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def write2file(file_name, content):
    output = open(file_name, "w+")
    for word in content:
        if len(word) < 1:
            continue
        output.write("{}\n".format(word))
    output.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # 打开文件
    skip_word = open("Data/skip_word").read().split("\n")
    important_word = open("Data/important_word").read().split("\n")
    data = open("Data/knowledge").read().split("****\n")

    # 遍历所有thm
    for thm in data:
        lines = thm.split("\n")
        if len(lines) < 1:
            continue

        # 遍历每个单词，筛选关键词
        keyword = []
        for word in lines[0].split():

            # 预处理单个单词
            if word == "":
                continue
            word = word.replace(",", "").replace(".", "").lower()

            # 单词分类
            if word in skip_word:
                continue
            elif word in important_word:
                keyword.append(word)
            else:
                # 人工判断
                while 1:
                    print("'{}' is important?".format(word))
                    ans = input()
                    if ans == "y":
                        important_word.append(word)
                        break
                    elif ans == "n":
                        skip_word.append(word)
                        break
        intro = lines[0]
        origin = lines[1]

    write2file("Data/skip_word", skip_word)
    write2file("Data/important_word", important_word)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
