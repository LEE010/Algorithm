class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.mem = {}
        self.s = s
        self.left, self.right = 0, 0
        self.maxLen = 0

        self.palindrome(0, len(s)-1)

        return s[self.left, self.right+1] 

    def palindrome(self, left: int, right: int) -> None:
        if left > right:
            return 0
        
        if left == right:
            return 1

        pos = (left, right)

        if pos in self.mem:
            return self.mem[pos]

        if self.s[left] == self.s[right]:
            self.mem[pos] = self.palindrome(left+1, right-1) + 2
        else:
            self.mem[pos] = max(self.palindrome(left, right+1), self.palindrome(left-1, right))

        if self.maxLen < self.mem[pos]:
            self.maxLen = self.mem[pos]
            self.left, self.right = pos

        return self.mem[pos]

"babad"
"cbbd"
"ccc"
"asdfgaasdfga"
"vthbaypbzzfrgeqkfsazhvocumiiblrrcxprqhpdkifncwazfrhmimewubfxmgehebepiuhkvghnbtvyckioxavjcezgbpztkimjmugprtwhsbthytmznfdihgtiuogiixshdqhczbkhswgfqfeaxajozaazczvfbnhzgazmcvplwutfdoatytwxpoxyzggjysobgdkurqdocpakcaxzvfcpagipbqfdfwhzitlezfpdhayrroztwgfqmcfkrphzehxbyioqxxvusvhqktmdovrwlijwjdxccylqqhbfbsmmjpgknxpivysnvedjmnasjtaufzdopjmzfubyxcrfqwaulbqnhezmtaygstdtldkqeeeeqkdltdtsgyatmzehnqbluawqfrcxybufzmjpodzfuatjsanmjdevnsyvipxnkgpjmmsbfbhqqlyccxdjwjilwrvodmtkqhvsuvxxqoiybxhezhprkfcmqfgwtzorryahdpfzeltizhwfdfqbpigapcfvzxackapcodqrukdgbosyjggzyxopxwtytaodftuwlpvcmzagzhnbfvzczaazojaxaefqfgwshkbzchqdhsxiigouitghidfnzmtyhtbshwtrpgumjmiktzpbgzecjvaxoikcyvtbnhgvkhuipebehegmxfbuwemimhrfzawcnfikdphqrpxcrrlbiimucovhzasfkqegrfzzbpyabhtv"
"mqizdjrfqtmcsruvvlhdgzfrmxgmmbguroxcbhalzggxhzwfznfkrdwsvzhieqvsrbyedqxwmnvovvnesphgddoikfwuujrhxwcrbttfbmlayrlmpromlzwzrkjkzdvdkpqtbzszrngczvgspzpfnvwuifzjdrmwfadophxscxtbavrhfkadhxrmvlmofbzqshqxazzwjextdpuszwgrxirmmlqitjjpijptmqfbggkwaolpbdglmsvlwdummsrdyjhmgrasrblpjsrpkkgknsucsshjuxunqiouzrdwwooxclutkrujpfebjpoodvhknayilcxjrvnykfjhvsikjabsdnvgguoiyldshbsmsrrlwmkfmyjbbsylhrusubcglaemnurpuvlyyknbqelmkkyamrcmjbncpafchacckhymtasylyfjuribqxsekbjkgzrvzjmjkquxfwopsbjudggnfbuyyfizefgxamocxjgkwxidkgursrcsjwwyeiymoafgyjlhtcdkgrikzzlenqgtdukivvdsalepyvehaklejxxmmoycrtsvzugudwirgywvsxqapxyjedbdhvkkvrxxsgifcldkspgdnjnnzfalaslwqfylmzvbxuscatomnmgarkvuccblpoktlpnazyeazhfucmfpalbujhzbykdgcirnqivdwxnnuznrwdjslwdwgpvjehqcbtjljnxsebtqujhmteknbinrloregnphwhnfidfsqdtaexencwzszlpmxjicoduejjomqzsmrgdgvlrfcrbyfutidkryspmoyzlgfltclmhaeebfbunrwqytzhuxghxkfwtjrfyxavcjwnvbaydjnarrhiyjavlmfsstewtxrcifcllnugldnfyswnsewqwnvbgtatccfeqyjgqbnufwttaokibyrldhoniwqsflvlwnjmffoirzmoxqxunkuepj"
"abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
"zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

"abcdefghijklmnop"[0:3]