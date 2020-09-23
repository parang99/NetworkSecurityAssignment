#!/usr/bin/env python
# coding: utf-8

# In[2]:


substituteTable = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76], 
                  [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0], 
                  [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15], 
                  [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75], 
                  [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84], 
                  [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF], 
                  [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8], 
                  [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2], 
                  [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73], 
                  [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB], 
                  [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79], 
                  [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08], 
                  [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A], 
                  [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E], 
                  [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF], 
                  [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

mixColumnMatrix = [[0x02, 0x03, 0x01, 0x01], 
                   [0x01, 0x02, 0x03, 0x01], 
                   [0x01, 0x01, 0x02, 0x03], 
                   [0x03, 0x01, 0x01, 0x02]]

def substitute(beforeList):
    afterList = []
    for byte in beforeList:
        row = byte // 16
        col = byte % 16
        afterList.append(substituteTable[row][col])
    return afterList

def makeKey(studentId):
    return studentId + studentId + studentId[:2]

def xorList(listA, listB):
    result = []
    for index in range(len(listA)):
        result.append(listA[index] ^ listB[index])
    return result

def xorPolynomial(poly1, poly2):
    xorList = [0] * 9
    if len(poly1) == 8:
        poly1.insert(0, 0)
    if len(poly2) == 8:
        poly2.insert(0, 0)
    for bit in range(9):
        xorList[bit] = poly1[bit] ^ poly2[bit]
    return xorList

def hexToPolynomial(hexnum):
    binaryStrNo0b = format(hexnum, '08b')
    return list(map(int, binaryStrNo0b))

def polynomialToHex(polynomialList):
    binaryStringNo0b = ''.join(map(str, polynomialList))
    return int(binaryStringNo0b, 2)

def checkMixColumn():
    aesTest = AES('a', 'b')
    aesTest.listAfterShiftRows = [0x87, 0xF2, 0x4D, 0X97, 
                                  0X6E, 0X4C, 0X90, 0XEC, 
                                  0X46, 0XE7, 0X4A, 0XC3, 
                                  0XA6, 0X8C, 0XD8, 0X95]
    aesTest.mixColumn()
    answer = [0x47, 0x40, 0xA3, 0x4C, 0x37, 0xD4, 0x70, 0x9F, 0x94, 0xE4, 0x3A, 0x42, 0xED, 0xA5, 0xA6, 0xBC]

    print('Mix Column', end = ' : ')
    showNumListToHexNo0x(aesTest.listAfterMixColumn)
    print('\nMix Column', end = ' : ')
    showNumListToHexNo0x(answer)

class AES:
    def __init__(self, plainText, keyText):
        self.plainText = plainText
        self.keyText = keyText

    def plainTextAndKeyTextToNumList(self):
        self.plainList = self.textToNumList(self.plainText)
        self.keyList = self.textToNumList(self.keyText)
        
    def textToNumList(self, text):
        listAfter = []
        for char in text:
            listAfter.append(ord(char))
        return listAfter
    
    def addRoundKey(self, listAfter, keyList):
        return xorList(listAfter, keyList)

    def substituteBytes(self):
        listAfter = []
        for byte in self.listAfterAddRoundKey:
            row = byte // 16
            col = byte % 16
            listAfter.append(substituteTable[row][col])
        self.listAfterSubstituteBytes = listAfter

    def shiftRows(self):
        listAfter = []
        listAfter[:4] = self.listAfterSubstituteBytes[:4]
        listAfter[4:7] = self.listAfterSubstituteBytes[5:8]
        listAfter.append(self.listAfterSubstituteBytes[4])
        listAfter[8:10] = self.listAfterSubstituteBytes[10:12]
        listAfter[10:12] = self.listAfterSubstituteBytes[8:10]
        listAfter.append(self.listAfterSubstituteBytes[15])
        listAfter[13:16] = self.listAfterSubstituteBytes[12:15]
        self.listAfterShiftRows = listAfter
        
    def mixColumn(self):
        listAfter = [0] * 16
        for row in range(4):
            for col in range(4):
                self.row = row
                self.col = col
                listAfter[row * 4 + col] = self.calculateU()
        self.listAfterMixColumn = listAfter

    def calculateU(self):
        self.get2Matrix()
        self.multipleAndXOR()
        self.divisionX84310()
        return polynomialToHex(self.polynomialSum)

    def get2Matrix(self):
        self.getConstantMatrix()
        self.getTextMatrix()

    def getConstantMatrix(self):
        self.constantMatrix = mixColumnMatrix[self.row]

    def getTextMatrix(self):
        textMatrix = []
        for index in range(4):
            textMatrix.append(self.listAfterShiftRows[index * 4 + self.col])
        self.textMatrix = textMatrix

    def multipleAndXOR(self):
        polynomialSum = [0] * 9
        for index in range(4):
            self.constantHex = self.constantMatrix[index]
            self.textHex = self.textMatrix[index]
            multiple = self.multiplePolynomial()
            polynomialSum = xorPolynomial(multiple, polynomialSum)
        self.polynomialSum = polynomialSum

    def multiplePolynomial(self):
        textPolynomial = hexToPolynomial(self.textHex)
        if self.constantHex == 0x01:
            return textPolynomial
        elif self.constantHex == 0x02:
            return textPolynomial + [0]
        else:
            return xorPolynomial(textPolynomial, textPolynomial + [0])

    def divisionX84310(self):
        if self.polynomialSum[0] == 1:
            X84310 = [1, 0, 0, 0, 1, 1, 0, 1, 1]
            self.polynomialSum = xorPolynomial(self.polynomialSum, X84310)
        
    def keyExpansion(self):
        RCon = [0, 0, 0, 0]
        self.rotateWord()
        self.w3SubstituteWord = substitute(self.w3RotateWord)
        self.w3XORWord = xorList(RCon, self.w3SubstituteWord)
        self.do4XOR()
    
    def rotateWord(self):
        w3RotateWord = []
        w3RotateWord[0:3] = self.keyList[13:16]
        w3RotateWord.append(self.keyList[12])
        self.w3RotateWord = w3RotateWord
    
    def do4XOR(self):
        keyPart1 = self.keyList[0:4]
        newKeyPart1 = xorList(self.w3XORWord, keyPart1)
        keyPart2 = self.keyList[4:8]
        newKeyPart2 = xorList(newKeyPart1, keyPart2)
        keyPart3 = self.keyList[8:12]
        newKeyPart3 = xorList(newKeyPart2, keyPart3)
        keyPart4 = self.keyList[12:16]
        newKeyPart4 = xorList(newKeyPart3, keyPart4)
        self.newKeyList = newKeyPart1 + newKeyPart2 + newKeyPart3 + newKeyPart4
        
    def print_process(self):
        print('%-16s' % 'Plain List', end = ' : ')
        showNumListToHexNo0x(self.plainList)
        print('\n')
        print('%-16s' % 'Add Round Key', end = ' : ')
        showNumListToHexNo0x(self.listAfterAddRoundKey)
        print('\n')
        print('%-16s' % 'Substitute Bytes', end = ' : ')
        showNumListToHexNo0x(self.listAfterSubstituteBytes)
        print('\n')
        print('%-16s' % 'Shift Rows', end = ' : ')
        showNumListToHexNo0x(self.listAfterShiftRows)
        print('\n')
        print('%-16s' % 'Mix Column', end = ' : ')
        showNumListToHexNo0x(self.listAfterMixColumn)
        print('\n')
        print('%-16s' % 'Add Round Key', end = ' : ')
        showNumListToHexNo0x(self.cipherList)
        print('\n')
        
        print('-' * 65, '\n')
        
        print('%-16s' % 'Key List', end = ' : ')
        showNumListToHexNo0x(self.keyList)
        print('\n')
        print('%-16s' % 'Key Expansion', end = ' : ')
        showNumListToHexNo0x(self.newKeyList)
        print('\n')
        
        print('-' * 65, '\n')
        
        print('%-16s' % 'Plain Text', end = ' : ')
        showNumListToAscii(self.plainList)
        print('\n')
        print('%-16s' % 'Add Round Key', end = ' : ')
        showNumListToAscii(self.listAfterAddRoundKey)
        print('\n')
        print('%-16s' % 'Substitute Bytes', end = ' : ')
        showNumListToAscii(self.listAfterSubstituteBytes)
        print('\n')
        print('%-16s' % 'Shift Rows', end = ' : ')
        showNumListToAscii(self.listAfterShiftRows)
        print('\n')
        print('%-16s' % 'Mix Column', end = ' : ')
        showNumListToAscii(self.listAfterMixColumn)
        print('\n')
        print('%-16s' % 'Add Round Key', end = ' : ')
        showNumListToAscii(self.cipherList)


def run_function(plainText, studentId):
    keyText = makeKey(studentId)

    aes = AES(plainText, keyText)

    aes.plainTextAndKeyTextToNumList()

    aes.listAfterAddRoundKey = aes.addRoundKey(aes.plainList, aes.keyList)
    aes.listAfterSubstituteBytes = substitute(aes.listAfterAddRoundKey)
    aes.shiftRows()
    aes.mixColumn()
    aes.keyExpansion()
    aes.cipherList = aes.addRoundKey(aes.listAfterMixColumn, aes.newKeyList)
    
    aes.print_process()

def showNumListToHexNo0x(numList):
    for num in numList:
        print(format(num, '02X'), end = ' ')
def showNumListToAscii(numList):
    for num in numList:
        print(chr(num), end = '')
        
# checkMixColumn()

plainText = 'I love Sookmyung'
studentId = '1713523'
run_function(plainText, studentId)


# In[ ]:




