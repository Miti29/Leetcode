class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # l1 = []
        # for i in strs:
        #     x = ''.join(sorted(i))
        #     a=[]
        #     for idx, j in enumerate(l1):
        #         print(j)
        #         if x in j:
        #             l1[idx].append((a.append(i)))
        #     l1.append(i)
        
        # return l1
        d, li = {}, []
        for i in strs:
            x = "".join(sorted(i))
            li = []
            if x in d:
                d[x].append(i)
                # continue
            else:
                li.append(i)
                d[x] = li

        
        li = []
        # print(d)

        for a,b in d.items():
            print(b)
            li.append(b)

        return li


                
