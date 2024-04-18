from kmp import KMPSearch
import re

def highlight_plagiarised(text, plagiarised_text):
    highlighted_text = ""
    text_words = re.findall(r'\w+', text.lower())
    plagiarised_words = re.findall(r'\w+', plagiarised_text.lower())
    
    for word in text_words:
        if word in plagiarised_words:
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

counter_matched = 0
counter_total = 0

root_words = re.findall(r'\w+', text.lower())  # Split root text into words
plagiarised_words = re.findall(r'\w+', plagiarised_text.lower())  # Split plagiarised text into words

for word in plagiarised_words:
    counter_total += 1
    if word in root_words:
        counter_matched += 1

match_percentage = (counter_matched * 100) / counter_total

print("\nMatch percentage = %s%%" % match_percentage)

if match_percentage >= 0:
    print("The input file appears to be plagiarised. %s%% of its content matches with the file %s." % (
        match_percentage, root_file))

    # Generate Word document
    report_filename = "plagiarised_report.doc"
    try:
        with open(report_filename, "w") as report_file:
            report_file.write("<html><body>")
            report_file.write("<p>Plagiarised Text (Highlighted in Red):</p>")
            report_file.write("<p>" + highlight_plagiarised(text, plagiarised_text) + "</p>")
            report_file.write("<p>Match percentage: %s%%</p>" % match_percentage)
            report_file.write("</body></html>")
        print("Word document report generated:", report_filename)
    except Exception as e:
        print("Error occurred while creating the Word document:", e)
