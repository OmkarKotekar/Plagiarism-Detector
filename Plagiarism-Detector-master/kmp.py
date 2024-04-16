# from lps import computeLPSArray

# def KMPSearch(pat, text, p):

#     M = len(pat)
#     N = len(text)
#     lps = [0]*M
#     j = 0 
#     computeLPSArray(pat, M, lps)
 
#     i = 0 
#     while i < N:
#         if pat[j].lower() == text[i].lower():
#             i += 1
#             j += 1
 
#         if j == M:
#             p +=1
#             j = lps[j-1]
#             break

#         elif i < N and pat[j].lower() != text[i].lower():
#             if j != 0:
#                 j = lps[j-1]
#             else:
#                 i += 1      
#     return p
 
# from lps import computeLPSArray
# import re

# def KMPSearch(pat, text, p):
#     pat_words = re.sub(r'[^\w\s]', '', pat.lower()).split()  # Remove punctuation and split into words
#     text_words = re.sub(r'[^\w\s]', '', text.lower()).split()  # Remove punctuation and split into words
    
#     M = len(pat_words)
#     N = len(text_words)
#     lps = [0] * M
#     computeLPSArray(pat_words, M, lps)
#     j = 0 
#     i = 0 
#     while i < N:
#         if pat_words[j] == text_words[i]:
#             i += 1
#             j += 1
#             if j == M:
#                 p += 1
#                 j = lps[j-1]
#         else:
#             if j != 0:
#                 j = lps[j-1]
#             else:
#                 i += 1      
#     return p


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

