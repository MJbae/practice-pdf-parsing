from tika import parser


# coding=utf-8
def print_hi(name):
    print("Hi, {0}".format(name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pdf_path = "test.pdf"

    # PDF 파일에서 텍스트를 추출
    raw_pdf = parser.from_file(pdf_path)
    contents = raw_pdf['content']
    contents = contents.strip()

    starting_index_of_crop = contents.find('Ⅰ')
    starting_index_of_vegetable = contents.find('Ⅱ')
    starting_index_of_fruit = contents.find('Ⅲ')
    crop_content = contents[starting_index_of_crop:starting_index_of_vegetable]
    vegetable_content = contents[starting_index_of_vegetable:starting_index_of_fruit]
    fruit_content = contents[starting_index_of_fruit:starting_index_of_fruit + 200]
    print("--- crop --- ")
    print(crop_content)
    print("--- vegetable --- ")
    print(vegetable_content)
    print("--- fruit --- ")
    print(fruit_content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
