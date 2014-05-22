import xml.etree.ElementTree as Tree

# Get filename and name from user
filename = input("Enter in the filename you want to parse (example.xml): ")
user = input("Enter in a name for yourself, used for replies: ")

# Set up ElementTree XML using the file provided by user
Tree = Tree.parse(filename)
root = Tree.getroot()

def main():

    # Create new file and set encoding to utf-8 as texts may contain improperly formatted emojis
    with open("parsed_{}.txt".format(filename), 'w', encoding='utf-8') as out:

        # Loop through each text
        for sms in root.findall('sms'):
            type = sms.get('type')
            message = sms.get('body')
            date = sms.get('readable_date')
            name = sms.get('contact_name')

            # Used to see if text is the sender, aka YOU.
            if type == "2":
                name = user

            # Print contents to file
            out.write('{}\n{}\n{}\n\n'.format(date, name, message))

        out.close()


main()