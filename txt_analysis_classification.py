fraud_dataset = {
    "phishing": ["email", "messages", "phone", "calls", "trick", "share", "sensitive", "data", "malware", "suspicious", "locked", "security", "password", "login", "unauthorized", "identity", "click", "offer", "won", "deal", "gift", "information", "billing", "payment", "reactivate", "greeting", "attachments", "fake"],
    "identity_theft": ["stolenidentity", "stolen", "identity", "personalinformation", "personal", "information", "socialsecurity", "social", "security", "creditcard", "credit", "card", "fraud", "impersonation", "unauthorizedaccess", "unauthorized", "access"],
    "credit_card_fraud": ["stolencard", "stolen", "card", "unauthorizedtransactions", "unauthorized", "transactions", "cardcloning", "card", "cloning", "skimming", "onlinepurchase", "online", "purchase", "fraudalert", "fraud", "alert"],
    "ransomware": ["malware", "encryption", "ransom", "bitcoin", "cyberattack", "cyber", "attack", "datahostage", "data", "hostage", "decryptionkey", "decryption", "key", "lockscreen", "lock", "screen"],
    "malware": ["virus", "trojan", "spyware", "worm", "infection", "malicioussoftware", "malicious", "software", "systemdamage", "system", "damage", "datatheft", "data", "theft"],
    "cyber_extortion": ["threat", "blackmail", "demand", "payment", "cyberattack", "cyber", "attack", "sensitiveinformation", "sensitive", "information", "ransom"],
    "online_scams": ["fakewebsite", "fake", "website", "lottery", "inheritance", "romance", "investment", "advancefee", "advance", "fee", "phishing", "fraud"],
    "data_breach": ["stolendata", "stolen", "data", "leakedinformation", "leaked", "information", "compromisedsystem", "compromised", "system", "unauthorizedaccess", "unauthorized", "access", "personaldata", "personal", "data", "securitybreach", "security", "breach"],
    "ddos": ["attack", "overload", "servercrash", "server", "crash", "trafficflood", "traffic", "flood", "botnet", "networkdisruption", "network", "disruption", "downtime"],
    "cyber_stalking": ["harassment", "onlinetracking", "online", "tracking", "threateningmessages", "threatening", "messages", "privacyinvasion", "privacy", "invasion", "monitoring", "intimidation"],
    "intellectual_property_theft": ["piracy", "copyrightinfringement", "copyright", "infringement", "stolencode", "stolen", "code", "trademarkviolation", "trademark", "violation", "illegaldistribution", "illegal", "distribution", "counterfeit"],
    "cyber_defamation": ["falseaccusation", "false", "accusation", "onlineslander", "online", "slander", "libel", "damagingreputation", "damage", "reputation", "maliciouscontent", "malicious", "content", "internetdefamation", "internet", "defamation"]
}

victim_dataset = {
    "team":["jeeva","balasurya","harinisri","abinaya"]
}

# accepting compliant from the victim
compliant = str(input("GIVE YOUR COMPLIANT\n")).lower()

# removing symbols by replacing it with single space
temp_compliant = ""
for char in compliant:
    if char.isalnum():
        temp_compliant += char
    else:
        temp_compliant += ' '
        
compliant = temp_compliant

# converting the compliant into words
splitted_compliant = list(compliant.split())

# removing tenses form
temp_splitted_compliant = []
for index, word in enumerate(splitted_compliant):
    
    if word[-3:] == 'ing':
        temp_splitted_compliant.insert(index, word[:-3])
    
    elif word[-2:] == 'ed' or word[-2:] == 'es':
        temp_splitted_compliant.insert(index, word[:-2])
    
    elif word[-1:] == 's' and not word[-2:] == 'ss':
        temp_splitted_compliant.insert(index, word[:-1])
    
    else:
        temp_splitted_compliant.insert(index, word)

splitted_compliant = temp_splitted_compliant

# creating an data set for joining words
join_words = ['he', 'same', 'as', 'on', 'o', 'off', 'is', 'during', 'was', 'out', 'such', 'into', 'll', 'doing', 'where', 'shouldn', 'after', 'wouldn', 'the', 'couldn', 'because', 'hers', 've', "should've", 'him', 'who', 'my', "it's", 'herself', 'mightn', 'there', "you'd", 'most', 're', 'am', 'before', "shouldn't", 'through', 'not', "didn't", 'below', 'about', 'in', 'over', 'can', 'our', "weren't", 'has', 'once', 'by', 'at', 'here', 'just', 'why', "hasn't", 'too', "isn't", "won't", 'don', 'are', 'mustn', 'any', 'have', 'down', 'her', 'again', 'should', 'being', 'each', 'will', "you'll", 'while', "wouldn't", 'an', 'doesn', 'were', "couldn't", 'now', 'ma', 'myself', 'won', 'you', 'them', 'yourselves', "you've", 'she', 'd', "shan't", 'when', 'few', 'his', "haven't", 'or', 'be', 'other', 'yourself', 'yours', 'didn', 'for', 'its', 'your', 'm', 'some', 'but', 'than', 'ours', "aren't", 'all', 'itself', "she's", 'if', 't', "hadn't", "mightn't", 'weren', 'very', 'then', 'theirs', 'up', 'to', 'own', 'more', "needn't", 'had', 'i', 'themselves', 'did', 'these', 'their', 's', 'ourselves', 'under', 'me', "you're", 'those', 'wasn', "don't", 'of', 'isn', 'against', 'and', 'from', 'himself', 'hadn', "doesn't", 'what', 'this', 'hasn', 'no', 'with', 'both', 'y', 'between', 'whom', 'until', "that'll", 'how', 'only', 'further', 'a', 'that', 'do', 'they', 'needn', 'above', "mustn't", 'which', 'aren', 'it', 'so', 'nor', 'shan', 'ain', 'haven', 'does', "wasn't", 'we', 'having', 'been']

# removing joining words from the splitted_compliant variable
for join_word in join_words:
    if join_word in splitted_compliant:
         splitted_compliant.remove(join_word)

# Identify the type of cyber crime 
detected_cyber_crime_fraud = None
for crime, keywords in fraud_dataset.items():
    if any(keyword in splitted_compliant for keyword in keywords):
        detected_cyber_crime_fraud = crime

# Identify the type of victim
detected_victim = None
for crime, keywords in victim_dataset.items():
    if any(keyword in splitted_compliant for keyword in keywords):
        detected_victim = crime

# displaying the output
print(f"detected cyber crime fraud : {detected_cyber_crime_fraud}")
print(f"detected victim : {detected_victim}")
