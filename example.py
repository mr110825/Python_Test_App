# 1.example.pyを作成して「hello world」と出力してください。

print("hello world")

# 2.greet関数を実装し、「こんにちは」と出力するようにしてください。
# 関数を呼び出して、実際に出力されることを確認してください。

def greet():
    print("こんにちは")

# greet関数を実行する
greet()

# 3.nameを引数に取り、「私の名前は{name}です」と
# 出力するprint_name関数を実装し、関数を呼び出して動作を確認してください。

test_name = input("課題3の変数name設定する名前を入力：")

def print_name(name):
    print("私の名前は" + name + "です")

print_name(test_name)

# 4.「おはようございます」という文字列を戻り値として返すget_greet関数を実装し、
# 戻り値をprint関数で出力してください。

def get_greet():
    return "おはようございます"

print(get_greet())

# 5. a, bを引数に取り、その足し算の結果を戻り値として返す
# add関数を実装し、関数を呼び出して結果をprint関数で出力してください。

num_a = int(input("課題5のaの値を入力："))
num_b = int(input("課題5のbの値を入力："))

def add(a,b):
    sum_num = a + b
    return sum_num

print(add(num_a,num_b))
