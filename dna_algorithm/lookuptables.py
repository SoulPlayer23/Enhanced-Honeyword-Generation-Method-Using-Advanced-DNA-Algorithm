lookup1 = {
"A" : "AAA" , "B" : "ACA" , "C" : "AGA" , "D" : "ATA" , "E" : "GAA" , "F" : "GCA" , "G" : "GGA" , "H" : "GTA" ,

"I" : "AAC" , "J" : "ACC" , "K" : "AGC" , "L" : "ATC" , "M" : "GAC" , "N" : "GCC" , "O" : "GGC" , "P" : "GTC" ,

"Q" : "AAG" , "R" : "ACG" , "S" : "AGG" , "T" : "ATG" , "U" : "GAG" , "V" : "GCG" , "W" : "GGG" , "X" : "GTG" ,

"Y" : "AAT" , "Z" : "ACT" , "1" : "AGT" , "2" : "ATT" , "3" : "GAT" , "4" : "GCT" , "5" : "GGT" , "6" : "GTT" ,

"7" : "CAA" , "8" : "CCA" , "9" : "CGA" , "0" : "CTA" , "!" : "TAA" , "@" : "TCA" , "#" : "TGA" , "$" : "TTA" ,

"*" : "CAC" , "?" : "CCC" , "/" : "CGC" , ">" : "CTC" , "<" : "TAC" , "~" : "TCC" , " " : "TGC" , "|" : "TTC" ,

"\\" : "CAG" , "_" : "CCG" , "=" : "CGG" , "+" : "CTG" , "-" : "TAG" , "," : "TCG" , "." : "TGG" , ":" : "TTG" ,

";" : "CAT" , "%" : "CCT" , "&" : "CGT" , "ˆ" : "CTT" , "(" : "TAT" , ")" : "TCT" , "[" : "TGT" , "]" : "TTT"
}

lookup2 = {
";" : "AAA" , "%" : "ACA" , "&" : "AGA" , "ˆ" : "ATA" , "(" : "GAA" , ")" : "GCA" , "[" : "GGA" , "]" : "GTA" ,

"\\" : "AAC" , "_": "ACC" , "=" : "AGC" , "+" : "ATC" , "-" : "GAC" , "," : "GCC" , "." : "GGC" , ":" : "GTC" ,

"*" : "AAG" , "?" : "ACG" , "/" : "AGG" , ">" : "ATG" , "<" : "GAG" , "~" : "GCG" , " " : "GGG" , "|" : "GTG" ,

"7" : "AAT" , "8" : "ACT" , "9" : "AGT" , "0" : "ATT" , "!" : "GAT" , "@" : "GCT" , "#" : "GGT" , "$" : "GTT" ,

"Y" : "CAA" , "Z" : "CCA" , "1" : "CGA" , "2" : "CTA" , "3" : "TAA" , "4" : "TCA" , "5" : "TGA" , "6" : "TTA" ,

"Q" : "CAC" , "R" : "CCC" , "S" : "CGC" , "T" : "CTC" , "U" : "TAC" , "V" : "TCC" , "W" : "TGC" , "X" : "TTC" ,
 
"I" : "CAG" , "J" : "CCG" , "K" : "CGG" , "L" : "CTG" , "M" : "TAG" , "N" : "TCG" , "O" : "TGG" , "P" : "TTG" ,

"A" : "CAT" , "B" : "CCT" , "C" : "CGT" , "D" : "CTT" , "E" : "TAT" , "F" : "TCT" , "G" : "TGT" , "H" : "TTT" ,
}

lookup3 = {
"A" : "AAA" , "I" : "ACA" , "Q" : "AGA" , "Y" : "ATA" , "7" : "GAA" , "*" : "GCA" , "\\" : "GGA" , ";" : "GTA" ,

"B" : "AAC" , "J" : "ACC" , "R" : "AGC" , "Z" : "ATC" , "8" : "GAC" , "?" : "GCC" , "_" : "GGC" , "%" : "GTC" ,

"C" : "AAG" , "K" : "ACG" , "S" : "AGG" , "1" : "ATG" , "9" : "GAG" , "/" : "GCG" , "=" : "GGG" , "&" : "GTG" ,

"D" : "AAT" , "L" : "ACT" , "T" : "AGT" , "2" : "ATT" , "0" : "GAT" , ">" : "GCT" , "+" : "GGT" , "ˆ" : "GTT" ,

"E" : "CAA" , "M" : "CCA" , "U" : "CGA" , "3" : "CTA" , "!" : "TAA" , "<" : "TCA" , "-" : "TGA" , "(" : "TTA" ,

"F" : "CAC" , "N" : "CCC" , "V" : "CGC" , "4" : "CTC" , "@" : "TAC" , "~" : "TCC" , "," : "TGC" , ")" : "TTC" ,

"G" : "CAG" , "O" : "CCG" , "W" : "CGG" , "5" : "CTG" , "#" : "TAG" , " " : "TCG" , "." : "TGG" , "[" : "TTG" ,

"H" : "CAT" , "P" : "CCT" , "X" : "CGT" , "6" : "CTT" , "$" : "TAT" , "|" : "TCT" , ":" : "TGT" , "]" : "TTT"
}

lookup4 = {
";" : "AAA" , "\\" : "ACA" , "*" : "AGA" , "7" : "ATA" , "Y" : "GAA" , "Q" : "GCA" , "I" : "GGA" , "A" : "GTA" ,

"%" : "AAC" , "_" : "ACC" , "?" : "AGC" , "8" : "ATC" , "Z" : "GAC" , "R" : "GCC" , "J" : "GGC" , "B" : "GTC" ,

"&" : "AAG" , "=" : "ACG" , "/" : "AGG" , "9" : "ATG" , "1" : "GAG" , "S" : "GCG" , "K" : "GGG" , "C" : "GTG" ,

"ˆ" : "AAT" , "+" : "ACT" , ">" : "AGT" , "0" : "ATT" , "2" : "GAT" , "T" : "GCT" , "L" : "GGT" , "D" : "GTT" ,

"(" : "CAA" , "-" : "CCA" , "<" : "CGA" , "!" : "CTA" , "3" : "TAA" , "U" : "TCA" , "M" : "TGA" , "E" : "TTA" ,

")" : "CAC" , "," : "CCC" , "~" : "CGC" , "@" : "CTC" , "4" : "TAC" , "V" : "TCC" , "N" : "TGC" , "F" : "TTC" ,

"[" : "CAG" , "." : "CCG" , " " : "CGG" , "#" : "CTG" , "5" : "TAG" , "W" : "TCG" , "O" : "TGG" , "G" : "TTG" ,

"]" : "CAT" , ":" : "CCT" , "|" : "CGT" , "$" : "CTT" , "6" : "TAT" , "X" : "TCT" , "P" : "TGT" , "H" : "TTT" ,

}

lookup5 = {
"A" : "AAA" , "!" : "ACA" , ">" : "AGA" , "_" : "ATA" , "." : "GAA" , "&" : "GCA" , "[" : "GGA" , "]" : "GTA" ,

"I" : "AAC" , "B" : "ACC" , "@" : "AGC" , "<" : "ATC" , "=" : "GAC" , ":" : "GCC" , "ˆ" : "GGC" , "[" : "GTC" ,

"P" : "AAG" , "J" : "ACG" , "C" : "AGG" , "#" : "ATG" , "~" : "GAG" , "+" : "GCG" , ";" : "GGG" , "(" : "GTG" ,

"V" : "AAT" , "Q" : "ACT" , "K" : "AGT" , "D" : "ATT" , "$" : "GAT" , " " : "GCT" , "-" : "GGT" , "%" : "GTT" ,

"1" : "CAA" , "W" : "CCA" , "R" : "CGA" , "L" : "CTA" , "E" : "TAA" , "*" : "TCA" , "|" : "TGA" , "," : "TTA" ,

"5" : "CAC" , "2" : "CCC" , "X" : "CGC" , "S" : "CTC" , "M" : "TAC" , "F" : "TCC" , "?" : "TGC" , "\\" : "TTC" ,

"8" : "CAG" , "6" : "CCG" , "3" : "CGG" , "Y" : "CTG" , "T" : "TAG" , "N" : "TCG" , "G" : "TGG" , "/" : "TTG" ,

"0" : "CAT" , "9" : "CCT" , "7" : "CGT" , "4" : "CTT" , "Z" : "TAT" , "U" : "TCT" , "O" : "TGT" , "H" : "TTT" ,
}

lookup = {1: lookup1, 2: lookup2, 3: lookup3, 4: lookup4, 5: lookup5}