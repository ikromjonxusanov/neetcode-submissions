class Solution:
    def get_key(self, value):
        return tuple(sorted([ord(x) for x in value]))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = {}

        for word in strs:
            key = self.get_key(word)
            if key not in outputs:
                outputs[key] = [word]
                continue
            
            outputs[key].append(word)
        array = []
        for output in outputs.values():
            array.append(output)
        return array
