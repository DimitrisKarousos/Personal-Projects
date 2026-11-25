def LFSR(startState, tapLength, streamLength, printMsg = False):
    state = startState
    startStateLength = int.bit_length(startState)
    #printformat = '{:#0' + str(startStateLength + 2) + 'b}' #+2 refers to 0b at the start of the format
    outStream = []
    for i in range(streamLength):
        #print(i)
        #print(printformat.format(state)[2:]) #[2:] trims the 0b at the start of the values
        #XOR the state with itself shifted taplength bits to the right and only keep last bit
        feedbackBit = (state ^ (state >> tapLength)) & 1
        #shift state to the right and add the feedback bit at the start
        state = (state >> tapLength) | (feedbackBit << startStateLength - 1)
        outStream.append(state & 1) #append the last state bit to the output stream
    if printMsg == True:
        print(''.join(map(str, outStream))) #print bitstring of list
    return  outStream

print(LFSR(9, 1, 20))
