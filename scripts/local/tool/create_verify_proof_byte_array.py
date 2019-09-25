def get_byte_array_string(input):
    split_to_2 = ["0x" + input[i:i+2] for i in range(0, len(input), 2)]
    return ', '.join(split_to_2) + ', '

l = [
6548240722676184311,
15981990255983598837,
4271084634524553022,
16099447255209036814,
17988598413050183269,
16929176871347718508,
6300229255366500887,
8613131833402875905,
11347925642258876918,
4558997298459442589,
8863663967133787059,
14356437779847216171,
6831914406606665822,
2016228809022734684,
10079427714015461727,
2185464558742164936,
4361719364940252452,
13020089061524665557,
6665506512250681052,
5690075570418549767,
644005173095260504,
10826353151531705695,
3861910526311831281,
10736526242564263141,
8959848315720915094,
5017360562788239081,
8699848958128346014,
12237422200133871867,
17647416271569930190,
678531036792986875,
331659326383269018,
16388739233441686814,
16943180183801414177,
10661750740031014987,
17786511659862514183,
15759876780486814339,
7129941987814594086,
2195679622922895926,
13608914646152514919,
2894841317249443502,
16426646093855773122,
887944944269177406,
11298754551943214098,
12703112664033280835,
15685601136233012725,
9935920996234260495,
2338779294532949310,
9743620975716563718,
9897573720350170676,
12245192298801992530]

#as_string = [str(hex(i)).replace('0x', '').replace('L', '').rjust(8 * 2, '0') for i in l]
as_string = [str(hex(i)).replace('0x', '').replace('L', '').rjust(8 * 2, '0') for i in l]
as_array = [get_byte_array_string(i) for i in as_string]
#print(as_array)
#joined = "".join(as_array)
#c = 0;

for x in as_array:
    print(x)
