# import re
# from kmp import KMPSearch

# root_file=input("Enter The Name of root file ")
# plagiarised_file=input("Enter The Name of plagiarised file ")
  
# Text = open(root_file,"r")
# text = Text.read()

# pattern_file = open(plagiarised_file,"r").read()
# sentences = re.split(r'[\.\?!\r\n]', pattern_file)
# counter_matched = 0
# counter_total = 0
# p=0
# for pattern in sentences:
#   pattern = pattern.strip()

#   if len(pattern) > 0:
#     counter_total +=1
#     counter_matched += KMPSearch(pattern, text,p)
          
# print ("Match percentage = %s%%" % (counter_matched*100/counter_total))

# if(counter_matched*100/counter_total) >= 70 :
#   print ("The input file appears to be plagiarised. %s%% of its content matches with the file %s." % ((counter_matched*100/counter_total), root_file))  

import re
from kmp import KMPSearch

def highlight_plagiarised(text, plagiarised_text):
    highlighted_text = ""
    for word in text.split():
        if word in plagiarised_text.split():
            highlighted_text += "<span style='color:red'>" + word + "</span> "
        else:
            highlighted_text += word + " "
    return highlighted_text

root_file = input("Enter The Name of root file: ")
plagiarised_file = input("Enter The Name of plagiarised file: ")

with open(root_file, "r") as root:
    text = root.read()

with open(plagiarised_file, "r") as plagiarised:
    plagiarised_text = plagiarised.read()

sentences = re.split(r'[\.\?!\r\n]', plagiarised_text)

counter_matched = 0
counter_total = 0
p = 0
plagiarised_content = ""

for pattern in sentences:
    pattern = pattern.strip()

    if len(pattern) > 0:
        counter_total += 1
        counter_matched += KMPSearch(pattern, text, p)

        if KMPSearch(pattern, text, p) > 0:
            highlighted = highlight_plagiarised(text, pattern)
            plagiarised_content += highlighted + "<br>"

match_percentage = (counter_matched * 100) / counter_total

print("\nMatch percentage = %s%%" % match_percentage)

if match_percentage >= 30:
    print("The input file appears to be plagiarised. %s%% of its content matches with the file %s." % (
        match_percentage, root_file))

    # Generate Word document
    report_filename = "plagiarised_report.doc"
    try:
        with open(report_filename, "w") as report_file:
            report_file.write("<html><body>")
            report_file.write("<p>Plagiarised Text (Highlighted in Red):</p>")
            report_file.write("<p>" + plagiarised_content + "</p>")
            report_file.write("<p>Match percentage: %s%%</p>" % match_percentage)
            report_file.write("</body></html>")
        print("Word document report generated:", report_filename)
    except Exception as e:
        print("Error occurred while creating the Word document:", e)
