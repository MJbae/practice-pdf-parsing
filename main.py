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

    print(contents)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
