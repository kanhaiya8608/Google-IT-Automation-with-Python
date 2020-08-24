def calculate_frequencies(file_contents):
    # Here is a list of punctuations and boring words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    boring_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    # Removes puntuations 
    no_puntuations = ""
    for char in file_contents:
        if char not in punctuations:
            no_puntuations += char.lower()  #lower case
    words = no_puntuations.split()          #list
    
    # Iterates through the boring_words
    boring_words_set = set()                #creating a set
    for word in boring_words:     
        if word not in boring_words_set:
            boring_words_set.add(word)
    
    # Iterates through the words to create a dictionary of words
    words_dictionary = {}
    for word in words:
        if word not in words_dictionary and word not in boring_words_set:
            words_dictionary[word] = 0
        if word in words_dictionary and word not in boring_words_set:
            words_dictionary[word] += 1
    return words_dictionary


file_contents = "You were the shadow to my light. Did you feel us? Another star. You fade away. Afraid our aim is out of sight.Wanna see us. Alight. Where are you now?. Where are you now?. Was it all in my fantasy? Were you only imaginary?"

print(calculate_frequencies(file_contents))
