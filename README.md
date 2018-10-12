A small simple script that writes new words to a .txt file and can output their number on demand

I was just curious about how many words in Finnish language do I know =)

accepted parameters

-a    one or multiple words to be written to file
-c    with this arg set the script will output the total number of words in the file
-f    name of the file where the words will be stored, default is 'words.txt'

it is possible to set both -a and -c args at the same time. The script will first insert the new word(s) and then output the total count

script is case insensitive, all words are lowercased

for ä and ö use a: and o: respectively
