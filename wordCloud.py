import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys

# def _upload():

    # _upload_widget = fileupload.FileUploadWidget()

    # def _cb(change):
    #     global file_contents
    #     decoded = io.StringIO(change['owner'].data.decode('utf-8'))
    #     filename = change['owner'].filename
    #     print('Uploaded `{}` ({:.2f} kB)'.format(
    #         filename, len(decoded.read()) / 2 **10))
    #     file_contents = decoded.getvalue()

    # _upload_widget.observe(_cb, names='data')
    # display(_upload_widget)
# Upload File

# _upload()   

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    
#    print(file_contents)
     
    iteration_dict = {}
    word_list = []
    
    word_list = file_contents.split()
    
    for word in word_list:
        
        if word in uninteresting_words or not word.isalpha() :
            continue
        elif word not in iteration_dict:
            iteration_dict[word.lower()] = 0
            
        iteration_dict[word.lower()] += 1
    
#     print(iteration_dict)
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(iteration_dict)
    return cloud.to_array()

file = open("C:\\Users\\steenkaj\\googleAutomation\\pycrash\\CRM Roadmap.txt")
file_contents = file.read()
file.close()

# print(file_contents)
# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()