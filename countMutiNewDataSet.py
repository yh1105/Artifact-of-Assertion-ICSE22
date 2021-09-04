record_TypeTot = {"assertEquals": 0, "assertTrue": 0, "assertThat": 0, "assertNotNull": 0
    , "assertFalse": 0, "assertNull": 0, "assertArrayEquals": 0, "assertSame": 0, "other": 0}
recordATLAS = {"assertEquals": 0, "assertTrue": 0, "assertThat": 0, "assertNotNull": 0
    , "assertFalse": 0, "assertNull": 0, "assertArrayEquals": 0, "assertSame": 0, "other": 0}
record_IRac = {"assertEquals": 0, "assertTrue": 0, "assertThat": 0, "assertNotNull": 0
    , "assertFalse": 0, "assertNull": 0, "assertArrayEquals": 0, "assertSame": 0, "other": 0}
record_IRadaptH = {"assertEquals": 0, "assertTrue": 0, "assertThat": 0, "assertNotNull": 0
    , "assertFalse": 0, "assertNull": 0, "assertArrayEquals": 0, "assertSame": 0, "other": 0}
record_IRadaptNN = {"assertEquals": 0, "assertTrue": 0, "assertThat": 0, "assertNotNull": 0
    , "assertFalse": 0, "assertNull": 0, "assertArrayEquals": 0, "assertSame": 0, "other": 0}
record_Combine = {"assertEquals": 0, "assertTrue": 0, "assertThat": 0, "assertNotNull": 0
    , "assertFalse": 0, "assertNull": 0, "assertArrayEquals": 0, "assertSame": 0, "other": 0}

recordIndexAtlasNotNull = []
recordIndexIRNotNull = []
recordIndexAdaptNotNull = []
f = open("./Result/NewDataSet/IRLabel.txt", 'r', encoding="utf-8")
contentList = f.read().rstrip("\n").split("\n")
f.close()
tt = 0
for l in contentList:
    n1 = l.split(" ")[0]
    n2 = l.split(" ")[2]
    if n1 in record_TypeTot.keys():
        record_TypeTot[n1] += 1
    elif n2 in record_TypeTot.keys():
        record_TypeTot[n2] += 1
    else:
        record_TypeTot['other'] += 1

f = open("./Result/NewDataSet/ATLASLabel.txt", 'r', encoding="utf-8")
contentAssertLabel = f.read().rstrip("\n").split("\n")
f.close()

f = open("./Result/NewDataSet/ATLASPre.txt", 'r', encoding="utf-8")
contentAssertAtlasPre = f.read().rstrip("\n").split("\n")
f.close()
for i in range(0, len(contentAssertLabel)):
    n1 = contentAssertLabel[i].split(" ")[0]
    n2 = contentAssertLabel[i].split(" ")[2]
    a = contentAssertLabel[i].strip().split()
    b = contentAssertAtlasPre[i].strip().split()
    if " ".join(a) == " ".join(b):
        if n1 in recordATLAS.keys():
            recordATLAS[n1] += 1
        elif n2 in recordATLAS.keys():
            recordATLAS[n2] += 1
        else:
            recordATLAS['other'] += 1

f = open("./Result/NewDataSet/IRLabel.txt", 'r', encoding="utf-8")
contentAssertLabelIRac = f.read().rstrip("\n").split("\n")
f.close()

f = open("./Result/NewDataSet/IR.txt", 'r', encoding="utf-8")
contentAssertIRacPre = f.read().rstrip("\n").split("\n")
f.close()
for i in range(0, len(contentAssertLabelIRac)):
    n1 = contentAssertLabelIRac[i].split(" ")[0]
    n2 = contentAssertLabelIRac[i].split(" ")[2]
    a = contentAssertLabelIRac[i].strip().split()
    b = contentAssertIRacPre[i].strip().split()
    if "".join(a) == "".join(b):
        if n1 in record_IRac.keys():
            record_IRac[n1] += 1
        elif n2 in record_IRac.keys():
            record_IRac[n2] += 1
        else:
            record_IRac['other'] += 1

f = open("./Result/NewDataSet/RAadapt-H.txt", 'r', encoding="utf-8")
contentAssertRAadaptHPre = f.read().rstrip("\n").split("\n")
f.close()
for i in range(0, len(contentAssertLabelIRac)):
    n1 = contentAssertLabelIRac[i].split(" ")[0]
    n2 = contentAssertLabelIRac[i].split(" ")[2]
    a = contentAssertLabelIRac[i].strip().split()
    b = contentAssertRAadaptHPre[i].strip().split()
    if " ".join(a) == " ".join(b):
        if n1 in record_IRadaptH.keys():
            record_IRadaptH[n1] += 1
        elif n2 in record_IRadaptH.keys():
            record_IRadaptH[n2] += 1
        else:
            record_IRadaptH['other'] += 1

f = open("./Result/NewDataSet/IRadapt-NN.txt", 'r', encoding="utf-8")
contentAssertRAadaptNNPre = f.read().rstrip("\n").split("\n")
f.close()
for i in range(0, len(contentAssertLabelIRac)):
    n1 = contentAssertLabelIRac[i].split(" ")[0]
    n2 = contentAssertLabelIRac[i].split(" ")[2]
    a = contentAssertLabelIRac[i].strip().split()
    b = contentAssertRAadaptNNPre[i].strip().split()
    if " ".join(a) == " ".join(b):
        if n1 in record_IRadaptNN.keys():
            record_IRadaptNN[n1] += 1
        elif n2 in record_IRadaptNN.keys():
            record_IRadaptNN[n2] += 1
        else:
            record_IRadaptNN['other'] += 1

f = open("./Result/NewDataSet/ComineLearningIndex.txt", 'r', encoding="utf-8")
contentIndex = f.read().rstrip("\n").split("\n")
f.close()

f = open("./Result/NewDataSet/Combine.txt", 'r', encoding="utf-8")
contentAssertCombinePre = f.read().rstrip("\n").split("\n")
f.close()

for i in range(0, len(contentAssertLabel)):
    n1 = contentAssertLabel[i].split(" ")[0]
    n2 = contentAssertLabel[i].split(" ")[2]
    a = contentAssertLabel[i].strip().split()
    c = contentAssertRAadaptNNPre[i].strip().split()
    b = contentAssertCombinePre[i].strip().split()
    if str(i) in contentIndex:
        if "".join(a) == "".join(b):
            if n1 in record_Combine.keys():
                record_Combine[n1] += 1
            elif n2 in record_Combine.keys():
                record_Combine[n2] += 1
            else:
                record_Combine['other'] += 1
    else:
        if "".join(c) == "".join(b):
            if n1 in record_Combine.keys():
                record_Combine[n1] += 1
            elif n2 in record_Combine.keys():
                record_Combine[n2] += 1
            else:
                record_Combine['other'] += 1

listN = ["assertEquals", "assertTrue", "assertThat", "assertNotNull", "assertFalse", "assertNull", "assertArrayEquals",
         "assertSame", "other"]

tot1 = 0
tot2 = 0
tot3 = 0
tot4 = 0
tot5 = 0
tot6 = 0
tot7 = 0
for l in record_TypeTot:
    tot1 += record_TypeTot[l]
for l in recordATLAS:
    tot2 += recordATLAS[l]
for l in record_IRac:
    tot3 += record_IRac[l]
for l in record_IRadaptH:
    tot4 += record_IRadaptH[l]
for l in record_IRadaptNN:
    tot6 += record_IRadaptNN[l]
for l in record_Combine:
    tot7 += record_Combine[l]
print("tot" + "  & " + str(tot1) + "  & " + str(tot2) + "  & " + str(tot3) + "  & " + str(tot4) + "  & " + str(
    tot5) + "  & " + str(tot6) + "  & " + str(tot7) + "\\\\")

print("tot" + "  & " + str(round(tot1 / 26542, 2)) + "  & " + str(round(tot2 / 26542, 2)) + "  & " + str(
    round(tot3 / 26542, 2)) + "  & " + str(round(tot4 / 26542, 2)) + "  & " + str(
    round(tot5 / 26542, 2)) + "  & " + str(round(tot6 / 26542, 2)) + "  & " + str(round(tot7 / 26542, 2)) + "\\\\")

for keyt in record_TypeTot.keys():
    print(keyt, end="")
    print(" &", end="")
print()
print("total&", end="")
for l in record_TypeTot.keys():
    print(str(record_TypeTot[l]) + "(" + str(round(record_TypeTot[l] / record_TypeTot[l], 2)) + ")", end="")
    print(" &", end="")
    tot1 += record_TypeTot[l]
print()
print("ATLAS &" + str(tot2) + "(" + str(round(tot2 / 26542, 2)) + ") &", end="")
for l in recordATLAS.keys():
    print(str(recordATLAS[l]) + "(" + str(round(recordATLAS[l] / record_TypeTot[l], 2)) + ")", end="")
    print(" &", end="")
    tot2 += recordATLAS[l]
print()
print("IRac &" + str(tot3) + "(" + str(round(tot3 / 26542, 2)) + ") &", end="")
for l in record_IRac.keys():
    print(str(record_IRac[l]) + "(" + str(round(record_IRac[l] / record_TypeTot[l], 2)) + ")", end="")
    print(" &", end="")
    tot3 += record_IRac[l]
print()
print("RAadaptH &" + str(tot4) + "(" + str(round(tot4 / 26542, 2)) + ") &", end="")
for l in record_IRadaptH.keys():
    print(str(record_IRadaptH[l]) + "(" + str(round(record_IRadaptH[l] / record_TypeTot[l], 2)) + ")", end="")
    print(" &", end="")
    tot4 += record_IRadaptH[l]
print()
print("RAadaptNN &" + str(tot6) + "(" + str(round(tot6 / 26542, 2)) + ") &", end="")
for l in record_IRadaptNN.keys():
    print(str(record_IRadaptNN[l]) + "(" + str(round(record_IRadaptNN[l] / record_TypeTot[l], 2)) + ")", end="")
    print(" &", end="")
    tot6 += record_IRadaptNN[l]
print()
print("Combine &" + str(tot7) + "(" + str(round(tot7 / 26542, 4)) + ") &", end="")
for l in record_Combine.keys():
    print(str(record_Combine[l]) + "(" + str(round(record_Combine[l] / record_TypeTot[l], 2)) + ")", end="")
    print(" &", end="")
    tot7 += record_Combine[l]
print()

for l in record_TypeTot.keys():
    print(str(record_TypeTot[l]) + "(" + str(round(record_TypeTot[l] / 26542, 2)) + ")", end="")
    print(" &", end="")

print()
for l in record_TypeTot.keys():
    print(str(l) + " ", end="")
