
def in_set(input: set, value: any) -> bool:
    return value in input

def main():
    data = {'banana', 'apple', 'cherry'}
    if in_set( data , 'apple'):
        print(f"'apple' is in the set {data}.")
    else:
        print(f"'apple' is not in the set {data}.")

    if in_set( data , '5'):
        print(f"'5' is in the set {data}.")
    else:
        print(f"'5' is not in the set {data}.")

if __name__ == '__main__':
    main()