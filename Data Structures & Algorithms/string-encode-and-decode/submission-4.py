class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f'{len(str)}#{str}' for str in strs])


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):

            j = i
            while s[j] != '#':
                j+= 1
            
            word_length = int(s[i:j])
            word = s[j+1:j+word_length+1]
            result.append(word)

            i = j+word_length+1
            
        return result
