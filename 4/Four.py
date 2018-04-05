
def readFile(fileName):
    #Open file, read its content and return it.
    with open(fileName, 'r') as file:

        content = file.read()
        return content

def checkPassphrases(passphrases):

    # Go through the list of passphrases an cont how many are valid
    # Define lambda function for visibility
    listPassphrase = lambda passphrase : len(passphrase.split(' '))
    setPassphrases =  lambda passphrase : len(set(passphrase.split(' ')))

    return sum(1 for passphrase in passphrases if listPassphrase(passphrase) == setPassphrases(passphrase))


def checkAnagrams(wordSet):
    # if one word is present more then one time in a list return false, otherwise return True
    for word in wordSet:
        if wordSet.count(word) > 1:
            return False
    return True


def checkPassphrasesSeccondPart(passphrases):

    # Go through the list of passphrases an cont how many are valid
    # Define lambda function for visibility
    listPassphrase = lambda passphrase : len(passphrase.split(' '))
    setPassphrases =  lambda passphrase : len(set(passphrase.split(' ')))
    setWords = lambda passphrase : [set(word) for word in passphrase.split(' ')]

    return  sum(1  for passphrase in passphrases if listPassphrase(passphrase) == setPassphrases(passphrase) and checkAnagrams(setWords(passphrase)))

if __name__ == "__main__":

    fileName = 'input'

    passphrases = readFile(fileName)

    print(checkPassphrases(passphrases.split('\n')))
    print(checkPassphrasesSeccondPart(passphrases.split('\n')))