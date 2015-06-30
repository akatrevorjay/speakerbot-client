from pymarkovchain import MarkovChain
import os


mc = MarkovChain('./markovdb')
data = ''

base_path = './resources/'
try:
    sources = os.listdir(base_path)
    for source in sources:
        with open(''.join([base_path, '/',source])) as f:
            sourceData = f.read()
        data = data + sourceData
except OSError as e:
    print 'Please create ./resources/ and populate with training materials'
mc.generateDatabase(data)



def generateSingle(keyword=None):
    '''
    Generates a single [almost] sentence from the given sources.
    You can pass in a keyword to ensure the given word exists in the output.

    e.x.
        generateSingle(keyword='jizz')
        > "kyle jizz the jizzer"

    '''
    results = generateALot(keyword=keyword, max=1)
    if len(results) > 0:
        return results[0]
    else:
        return ''

def generateALot(keyword=None, max=50, max_tries=5000):
    results = []
    current = 0
    while len(results) < max and current < max_tries:
        current += 1
        s = mc.generateString()
        if len(s.split(' ')) > 2:
            if keyword and keyword.lower() in s.lower():
                results.append(s)
            elif not keyword:
                results.append(s)
    return results

def main():
    pass

if __name__ == '__main__':
    main()
