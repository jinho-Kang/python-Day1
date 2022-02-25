def convert_to_f(celsius_value):
    return celsius_value * 9.0 / 5 + 32

# fah_converter.py를 직접 실행 시켰을때 test를 해라
# 이걸 안해주면 jupyter notebook에서도 뜸
if __name__== "__main__":
    print('test: ', convert_to_f(30))
