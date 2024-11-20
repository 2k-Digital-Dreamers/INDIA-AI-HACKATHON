dataset = {
    "phishing":["email","text messages","phone calls","trick","sharing", "sensitive data", "downloading malware"],
    "team":["jeeva","bala","harini","abi"]
}
jeeva=input("enter the word: ")

#  reading the each dictionary elements one by one
for data in dataset:
    print (data)
    print(dataset[data])
   # comparing with the user's word(input)
    for  i in dataset[data]:
        if jeeva == i:
            print(1,data)

  
