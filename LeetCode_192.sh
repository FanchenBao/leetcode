# I have to use a lot of stackoverflow for this.
# For using sed to remove consecutive what spaces: https://stackoverflow.com/a/1271270/9723036
# For the general idea: https://stackoverflow.com/a/10552948/9723036
# For using awk: https://www.howtogeek.com/562941/how-to-use-the-awk-command-on-linux/

# The script first strips all the leading and trailing white spaces.
# Then it repaces the remaining white spaces with newline.
# Then sort, count, sort reverse, and awk for output.

cat words.txt | sed -E 's/^\s+|\s+$//g' | sed -E 's/\s+/\n/g' | sort | uniq -c | sort -r | awk '{print $2,$1}'