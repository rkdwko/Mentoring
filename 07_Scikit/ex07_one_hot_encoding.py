from sklearn.preprocessing import OneHotEncoder

def main():
    enc = OneHotEncoder()
    sourcedata = [
        [ord('r')],  #red
        [ord('b')],  #blue
        [ord('y')]   #yellow
    ]
    enc.fit(sourcedata)
    data =[
        [ord('r')],
        #[ord('b')],
        #['b'],
        [ord('y')]
    ]
    print(enc.transform(data).toarray())

if __name__ == '__main__':
    main()


