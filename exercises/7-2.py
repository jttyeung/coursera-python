# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = raw_input("Enter file name: ")
fh = open(fname)
spamLines = 0
spamTotal = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else :
        position = line.find("0.")
        spamLines = spamLines + 1
        spamConf = float(line[position:])
        spamTotal = spamConf + spamTotal
        spamAvg = spamTotal/spamLines
print "Average spam confidence:", spamAvg



# Desired Output:
# Average spam confidence: 0.750718518519