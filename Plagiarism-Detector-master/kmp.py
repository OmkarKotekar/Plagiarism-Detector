import re
from lps import computeLPSArray

def KMPSearch(pat, text, p):
    pat_words = re.findall(r'\w+', pat.lower())  # Split pattern into words
    text_sentences = re.split(r'[\.\?!]', text.lower())  # Split text into sentences
    text_words = [re.findall(r'\w+', sentence) for sentence in text_sentences]  # Split each sentence into words

    M = len(pat_words)
    N = sum(len(sentence) for sentence in text_words)  # Total number of words in text
    lps = [0] * M
    computeLPSArray(pat_words, M, lps)
    j = 0 
    for i in range(len(text_words)):
        k = 0  # Index for pattern words
        for word in text_words[i]:
            while k > 0 and pat_words[k] != word:
                k = lps[k-1]
            if pat_words[k] == word:
                k += 1
            if k == M:
                p += 1
                k = lps[k-1]
            j += 1
    return p

