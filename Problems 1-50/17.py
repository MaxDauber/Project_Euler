'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''

numbersDict = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety"
}


def numberLetters(num):
    num_len = ''
    
    if 0 < num <= 20:
        num_len += numbersDict[num]

    if 21 <= num <= 99:
        a,b = divmod(num, 10)
        if b == 0:
            num_len += numbersDict[a*10]
        else:
            num_len += numbersDict[a*10] + numbersDict[b]

    if 100 <= num <= 999:
        if num % 100 == 0:
            num_len += numbersDict[int(num / 100)] + "hundred"
        else:
            digit = int(num / 100)
            num = num - digit * 100
            if 0 < num <= 20:
                num_len += numbersDict[digit] + "hundredand" + numbersDict[num]
            if 21 <= num <= 99:
                a,b = divmod(num, 10)
                if b == 0:
                    num_len += numbersDict[digit] + "hundredand" + numbersDict[a*10]
                else:
                    num_len += numbersDict[digit] + "hundredand" + numbersDict[a*10] + numbersDict[b]
    if num == 1000:
        num_len += "onethousand"

    return len(num_len)

sum = 0
for i in range(1,1001):
    sum += numberLetters(i)
print(sum)
