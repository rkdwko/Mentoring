from sklearn.preprocessing import OneHotEncoder

def main():
    enc = OneHotEncoder()
    sourcedata = [
        [65],
        [66],
        [67]
    ]
    enc.fit(sourcedata)

    data =[
        [65],
        [66],
        [67],
        [65],
        [67]
    ]
    print(enc.transform(data).toarray())

if __name__ == '__main__':
    main()