def analyze(codebook):
   codebook = codebook.upper()
   s=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
   sortList = []
   for i in range(26):
      sortList.append((s[i], codebook.count(s[i])))
   sortList = sorted(sortList, key=lambda x:x[1], reverse = True)
   return sortList

def assign(freq):
   s=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
   common = []
   encode = []
   decode = []
   for i in range(len(freq)):
      common.append((s[i],freq[i][0]))
   print(common)
   for j in range(26):
      encode.append(common[j][1])
      decode.append(common[[x[1] for x in common].index(s[j])][0])
   return encode, decode   
   
def printFreq(freq):
   print(str(freq)[1:-1])

def codeme(encode, enc):
   val = ""
   enc = enc.upper()
   s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   for i in range(len(enc)):
      if enc[i] in s:
         val += encode[s.index(enc[i])]
      else:
         val += enc[i]
   return val

def decodeme(decode, dec):
   val = ""
   dec = dec.upper()
   s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   for i in range(len(dec)):
      if dec[i] in s:
         val += decode[s.index(dec[i])]
      else:
         val += dec[i]
   return val
                  
                    
def main():
    # read the code from input
    codebook = input("Please enter the codebook: ")
    print(codebook)
    freq = analyze(codebook)
    printFreq(freq)
    encode, decode = assign(freq)
    print("Encode:")
    print(encode)
    print("Decode:")
    print(decode)
    while (True):
        enc = input("Please enter a message to encode: ")
        print(enc)
        if enc == "EXIT":
            break
        if enc != "SKIP":
            coded = codeme(encode, enc)
            print(coded)
        dec = input("Please enter a message to decode: ")
        print(dec)
        if dec == "EXIT":
            break
        if dec != "SKIP":
            coded = decodeme(decode, dec)
            print(coded)
    print("This program will self destruct in 10 seconds...")
main()
