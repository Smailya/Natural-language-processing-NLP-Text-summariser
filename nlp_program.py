import re
import heapq

# Your original text
text = '''Introduction

Trees, those silent giants that populate our landscapes, have always been an integral part of our natural world. They provide us with oxygen, shade on a hot summer day, and a refuge for countless creatures. Yet, beyond their physical presence, trees have a secret life that is truly fascinating. One of the most intriguing aspects of their existence is their ability to communicate with each other and form intricate networks beneath the soil. In this article, we'll delve into this extraordinary fact about trees – their ability to communicate and share vital information with their neighbors.

The Wood Wide Web

Imagine a vast underground network, similar to the World Wide Web, but made of roots and fungi. This is what scientists have aptly named the "Wood Wide Web." This underground system enables trees to exchange a wealth of information, such as warnings about pests and diseases, sharing nutrients, and even sending distress signals during times of danger.

The Mycorrhizal Connection

At the heart of the Wood Wide Web are mycorrhizal fungi, which have a symbiotic relationship with trees. These fungi attach themselves to the tree's roots and extend their thread-like structures, known as hyphae, far and wide through the soil. This intricate network of hyphae connects multiple trees, forming a mycorrhizal network.

Sharing Nutrients

One of the most remarkable aspects of this tree communication system is the sharing of nutrients. Trees, through their roots, provide sugars and carbohydrates to the fungi. In return, the fungi scavenge the soil for essential nutrients, such as phosphorus and nitrogen, which are often scarce. The fungi then transport these nutrients back to the trees, ensuring their mutual survival.

Warning Signals

When a tree is under attack by insects or disease, it can release chemical signals into the air and soil. These signals are picked up by neighboring trees through their roots and can trigger a defensive response. For example, when a tree is infested with aphids, it can release chemicals that repel aphids or attract predators of aphids. This warning system can help neighboring trees prepare for an impending threat.

Sharing Resources

In a dense forest, where trees compete for sunlight, the Wood Wide Web allows for a form of cooperation. Larger, older trees with more access to sunlight can share some of their energy with smaller, shaded trees. This cooperative behavior ensures the survival of the entire forest ecosystem.

Conclusion

The fact that trees communicate with each other through the Wood Wide Web is not only fascinating but also a testament to the interconnectedness of life on Earth. It highlights the complexity of ecosystems and the importance of preserving our forests. Understanding this hidden world of tree communication can lead to more sustainable forestry practices and a deeper appreciation for the remarkable lives of these silent giants. The next time you walk through a forest, take a moment to marvel at the incredible network of communication happening beneath your feet, where trees share their secrets and support one another in the silent language of nature.'''

# Hardcoded list of English stopwords (common words to ignore)
stopwords = set("""
i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its 
itself they them their theirs themselves what which who whom this that these those am is are was were be been being have 
has had having do does did doing a an the and but if or because as until while of at by for with about against between 
into through during before after above below to from up down in out on off over under again further then once here there 
when where why how all any both each few more most other some such no nor not only own same so than too very s t can will 
just don should now
""".split())

# Split the text into sentences using regex (a rough but serviceable splitter)
sentence_list = re.split(r'(?<=[.!?])\s+', text)

# Tokenize text into words using regex
word_list = re.findall(r'\b\w+\b', text.lower())

# Frequency map (word -> count)
frequency_map = {}
for word in word_list:
    if word not in stopwords:
        if word not in frequency_map:
            frequency_map[word] = 1
        else:
            frequency_map[word] += 1

# Normalize frequency scores
max_frequency = max(frequency_map.values())
for word in frequency_map:
    frequency_map[word] = frequency_map[word] / max_frequency

# Calculate sentence scores
sent_scores = {}
for sent in sentence_list:
    words_in_sent = re.findall(r'\b\w+\b', sent.lower())
    for word in words_in_sent:
        if word in frequency_map and len(sent.split(' ')) < 35:
            if sent not in sent_scores:
                sent_scores[sent] = frequency_map[word]
            else:
                sent_scores[sent] += frequency_map[word]

# Get top 10 sentences
summary = heapq.nlargest(10, sent_scores, key=sent_scores.get)

# Output summary
for a in summary:
    print(a)
