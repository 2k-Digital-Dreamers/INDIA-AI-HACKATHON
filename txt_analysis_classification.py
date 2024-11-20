dataset = {
    "phishing":["email","text messages","phone calls","trick","sharing", "sensitive data", "downloading malware"],
    "team":["jeeva","bala","harini","abi"]
}

# accepting compliant from the victim
compliant = str(input("GIVE YOUR COMPLIANT\n"))

# converting the compliant into words
splitted_compliant = compliant.split()

# creating an data set for joining words
join_words = ['he', 'same', 'as', 'on', 'o', 'off', 'is', 'during', 'was', 'out', 'such', 'into', 'll', 'doing', 'where', 'shouldn', 'after', 'wouldn', 'the', 'couldn', 'because', 'hers', 've', "should've", 'him', 'who', 'my', "it's", 'herself', 'mightn', 'there', "you'd", 'most', 're', 'am', 'before', "shouldn't", 'through', 'not', "didn't", 'below', 'about', 'in', 'over', 'can', 'our', "weren't", 'has', 'once', 'by', 'at', 'here', 'just', 'why', "hasn't", 'too', "isn't", "won't", 'don', 'are', 'mustn', 'any', 'have', 'down', 'her', 'again', 'should', 'being', 'each', 'will', "you'll", 'while', "wouldn't", 'an', 'doesn', 'were', "couldn't", 'now', 'ma', 'myself', 'won', 'you', 'them', 'yourselves', "you've", 'she', 'd', "shan't", 'when', 'few', 'his', "haven't", 'or', 'be', 'other', 'yourself', 'yours', 'didn', 'for', 'its', 'your', 'm', 'some', 'but', 'than', 'ours', "aren't", 'all', 'itself', "she's", 'if', 't', "hadn't", "mightn't", 'weren', 'very', 'then', 'theirs', 'up', 'to', 'own', 'more', "needn't", 'had', 'i', 'themselves', 'did', 'these', 'their', 's', 'ourselves', 'under', 'me', "you're", 'those', 'wasn', "don't", 'of', 'isn', 'against', 'and', 'from', 'himself', 'hadn', "doesn't", 'what', 'this', 'hasn', 'no', 'with', 'both', 'y', 'between', 'whom', 'until', "that'll", 'how', 'only', 'further', 'a', 'that', 'do', 'they', 'needn', 'above', "mustn't", 'which', 'aren', 'it', 'so', 'nor', 'shan', 'ain', 'haven', 'does', "wasn't", 'we', 'having', 'been']

# removing joining words from the splitted_compliant variable
for join_word in join_words:
    if join_word in splitted_compliant:
         splitted_compliant.remove(join_word)
     
#  reading the each dictionary elements one by one
for data in dataset:
   # comparing with the user's word(input)
   for splitted_word in splitted_compliant:
       for  i in dataset[data]:
            if splitted_word == i:
                print(1,data)


