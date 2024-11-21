fraud_dataset = {
    "phishing": ["email", "messages", "phone", "calls", "trick", "share", "sensitive", "data", "malware", "suspicious", "locked", "security", "password", "login", "unauthorized", "identity", "click", "offer", "won", "deal", "gift", "information", "billing", "payment", "reactivate", "greeting", "attachments", "fake"],
    "identity theft": ["stolenidentity", "stolen", "identity", "personalinformation", "personal", "information", "socialsecurity", "social", "security", "creditcard", "credit", "card", "fraud", "impersonation", "unauthorizedaccess", "unauthorized", "access"],
    "credit card fraud": ["stolencard", "stolen", "card", "unauthorizedtransactions", "unauthorized", "transactions", "cardcloning", "card", "cloning", "skimming", "onlinepurchase", "online", "purchase", "fraudalert", "fraud", "alert"],
    "ransomware": ["malware", "encryption", "ransom", "bitcoin", "cyberattack", "cyber", "attack", "datahostage", "data", "hostage", "decryptionkey", "decryption", "key", "lockscreen", "lock", "screen"],
    "malware": ["virus", "trojan", "spyware", "worm", "infection", "malicioussoftware", "malicious", "software", "systemdamage", "system", "damage", "datatheft", "data", "theft"],
    "cyber extortion": ["threat", "blackmail", "demand", "payment", "cyberattack", "cyber", "attack", "sensitiveinformation", "sensitive", "information", "ransom"],
    "online scams": ["fakewebsite", "fake", "website", "lottery", "inheritance", "romance", "investment", "advancefee", "advance", "fee", "phishing", "fraud"],
    "data breach": ["stolendata", "stolen", "data", "leakedinformation", "leaked", "information", "compromisedsystem", "compromised", "system", "unauthorizedaccess", "unauthorized", "access", "personaldata", "personal", "data", "securitybreach", "security", "breach"],
    "ddos": ["attack", "overload", "servercrash", "server", "crash", "trafficflood", "traffic", "flood", "botnet", "networkdisruption", "network", "disruption", "downtime"],
    "cyber stalking": ["harassment", "onlinetracking", "online", "tracking", "threateningmessages", "threatening", "messages", "privacyinvasion", "privacy", "invasion", "monitoring", "intimidation"],
    "intellectual_property_theft": ["piracy", "copyrightinfringement", "copyright", "infringement", "stolencode", "stolen", "code", "trademarkviolation", "trademark", "violation", "illegaldistribution", "illegal", "distribution", "counterfeit"],
    "cyber defamation": ["falseaccusation", "false", "accusation", "onlineslander", "online", "slander", "libel", "damagingreputation", "damage", "reputation", "maliciouscontent", "malicious", "content", "internetdefamation", "internet", "defamation"]
}


victim_dataset = {
    "bank": [ "fraud", "theft", "cyberattack", "cyber", "attack", "phishing", "ransomware", "data", "breach", "financial", "scam", "hacking", "unauthorized", "transaction", "account", "takeover", "wire", "robbery", "money", "laundering", "ATM", "skimming", "check", "loan", "investment", "manipulation", "credit", "debit", "Ponzi", "scheme", "kiting", "identity", "false", "creation" ],
    "company": [ "corporate", "espionage", "data", "breach", "intellectual", "property", "theft", "cyber", "extortion", "employee", "business", "fraud", "insider", "trading", "malware", "financial", "misconduct", "contract", "bribery", "embezzlement", "trade", "secrets", "industrial", "sabotage", "statement", "misappropriation", "assets", "fake", "invoices", "kickback", "schemes", "vendor", "procurement", "shell", "company", "misstatement", "spying" ],
    "individual": [ "identity", "theft", "credit", "card", "fraud", "personal", "data", "breach", "harassment", "assault", "domestic", "violence", "stalking", "financial", "scam", "elder", "abuse", "child", "cyber", "bullying", "online", "phone", "mugging", "pickpocketing", "dating", "email", "lottery", "investment", "fraudulent", "schemes", "false", "pretenses", "home", "invasion", "carjacking", "social", "engineering", "cyberstalking", "internet" ], 
    "non_government_organization": [ "funding", "fraud", "donation", "scam", "phishing", "data", "breach", "misappropriation", "embezzlement", "fake", "charity", "volunteer", "unauthorized", "access", "cyberattack", "grant", "counterfeit", "donations", "trust", "fund", "misuse", "financial", "irregularities", "fraudulent", "fundraising", "campaigns", "embezzled", "funds", "reporting", "donor", "tax", "evasion", "projects", "diversion", "cyberfraud" ], 
    "government_organization": [ "cyber", "espionage", "data", "breach", "phishing", "ransomware", "bribery", "corruption", "embezzlement", "document", "fraud", "identity", "theft", "misuse", "funds", "government", "political", "scandal", "whistleblower", "retaliation", "procurement", "graft", "public", "sector", "extortion", "contracts", "ghost", "employees", "budget", "misallocation", "policy", "kickbacks", "regulatory", "election", "threats" ], 
    "industry": [ "industrial", "espionage", "data", "theft", "cyberattack", "phishing", "sabotage", "patent", "infringement", "trade", "secret", "counterfeit", "unauthorized", "access", "fraudulent", "contracts", "supply", "chain", "production", "intellectual", "property", "violation", "brand", "regulatory", "compliance", "market", "manipulation", "insider", "products", "manipulation", "tech", "environmental", "advertising" ]
}

# accepting compliant from the victim
compliant = str(input("GIVE YOUR COMPLIANT\n==>")).lower()

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
join_words = ['he', 'same', 'as', 'on', 'o', 'off', 'is', 'during', 'was', 'out', 'such', 'into', 'll', 'doing', 'where', 'shouldn', 'after', 'wouldn', 'the', 'couldn', 'because', 'hers', 've', "should've", 'him', 'who', 'my', "it's", 'herself', 'mightn', 'there', "you'd", 'most', 're', 'am', 'before', "shouldn't", 'through', 'not', "didn't", 'below', 'about', 'in', 'over', 'can', 'our', "weren't", 'has', 'once', 'by', 'at', 'here', 'just', 'why', "hasn't", 'too', "isn't", "won't", 'don', 'are', 'mustn', 'any', 'have', 'down', 'her', 'again', 'should', 'being', 'each', 'will', "you'll", 'while', "wouldn't", 'an', 'doesn', 'were', "couldn't", 'now', 'ma', 'myself', 'won', 'you', 'them', 'yourselves', "you've", 'she', 'd', "shan't", 'when', 'few', 'his', "haven't", 'or', 'be', 'other', 'yourself', 'yours', 'didn', 'for', 'its', 'your', 'm', 'some', 'but', 'than', 'ours', "aren't", 'all', 'itself', "she's", 'if', 't', "hadn't", "mightn't", 'weren', 'very', 'then', 'theirs', 'up', 'to', 'own', 'more', "needn't", 'had', 'i', 'themselves', 'did', 'these', 'their', 's', 'ourselves', 'under', 'me', "you're", 'those', 'wasn', "don't", 'of', 'isn', 'against', 'and', 'from', 'himself', 'hadn', "doesn't", 'what', 'this', 'hasn', 'no', 'with', 'both', 'y', 'between', 'whom', 'until', "that'll", 'how', 'only', 'further', 'a', 'that', 'do', 'they', 'needn', 'above', "mustn't", 'which', 'aren', 'it', 'so', 'nor', 'shan', 'ain', 'haven', 'does', "wasn't", 'we', 'having', 'been'


]

# removing joining words from the splitted_compliant variable
for join_word in join_words:
    if join_word in splitted_compliant:
         splitted_compliant.remove(join_word)

# Identify the type of cyber crime 
detect_fraud = []
for word in splitted_compliant:
    
    for crime,keywords in fraud_dataset.items():
        count =0
        for key in keywords:
            if key == word:
                count += 1
        if count > 0:
            detect_fraud.append([crime,count])

# uniformly arranging the detect_fraud elements
temp_dict = {}
for item in detect_fraud:
    category = item[0]
    temp_dict[category] = temp_dict.get(category, 0) + item[1]

fraud_probability = [[category, count] for category, count in temp_dict.items()]

# detect the fraud
_fraud=""
_fcount=0
for crime,count in fraud_probability:
        
    if _fcount < count:
        _fraud = crime
        _fcount = count
    elif _fcount == count:
        _fraud += " or " + crime
        _fcount = count
    else:
        continue
    
# Identify the type of victim
detect_victim = []
for word in splitted_compliant:
    
    for victim,keywords in victim_dataset.items():
        count =0
        for key in keywords:
            if key == word:
                count += 1
        if count > 0:
            detect_victim.append([victim,count])

# uniformly arranging the detect_victim elements
temp_dict = {}
for item in detect_victim:
    category = item[0]
    temp_dict[category] = temp_dict.get(category, 0) + item[1]

victim_probability = [[category, count] for category, count in temp_dict.items()]

# detect the victim
_victim=""
_vcount=0
for victim,count in victim_probability:
    
    if _vcount < count:
        _victim = victim
        _vcount = count
    elif _vcount == count:
        _victim += " or " + crime
        _vcount = count
    else:
        continue

# displaying the output
print(f"\n==>detected cyber crime fraud \n------->> {_fraud}")

# displaying the output
print(f"\n==>detected victim \n-------> {_victim}\n\n")