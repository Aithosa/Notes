# 我的代码
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        jud = []
        for ele in s:
            jud.append(ele)
            if len(jud) >= 2:
                if ele in "()" and (ord(jud[-1]) == ord(jud[-2])+1):
                    jud.pop()
                    jud.pop()
                elif ord(jud[-1]) == ord(jud[-2])+2:
                    jud.pop()
                    jud.pop()
        if len(jud) == 0:
            return True
        else:
            return False

# 同时间的其他代码
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        # 去掉字符串中的空格
        s.replace(' ','')
        # 括号是奇数 false
        if len(s)%2 != 0:
            return False
        flag = False
        r_list = [')', ']', '}']
        ret = [0]
        for i in s:
            # 如果i是右括号 且 和左括号匹配
            if i in r_list:
                if (i == ')' and ret[-1] == '(') or (i == ']' and ret[-1] == '[') or (i == '}' and ret[-1] == '{'):
                    ret.pop()
            # 如果i是左括号 放进ret中
            else:
                ret.append(i)
        if len(ret) == 1:
            flag = True
        return flag


# 高一级的代码
class Solution:
    def isValid(self, s):
        if not s:
            return True
        st = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
                st.append(s[i])
            elif (s[i] == ')'):
                if not st:
                    return False
                if (st[len(st)-1] != '('):
                    return False;
                st.pop()
            elif (s[i] == ']'):
                if not st:
                    return False
                if (st[len(st)-1] != '['):
                    return False
                st.pop()
            elif (s[i] == '}'):
                if not st:
                    return False
                if (st[len(st)-1] != '{'):
                    return False
                st.pop()


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        stack = []
        for i in range(len(s)):
            if s[i] in ["}","]",")"]:
                if len(stack) <= 0: return False
                if s[i] == "}" and stack[-1] != "{": return False
                if s[i] == ")" and stack[-1] != "(": return False
                if s[i] == "]" and stack[-1] != "[": return False
                stack.pop(-1)
            else:
                stack.append(s[i])
        if len(stack) <= 0:  return True
        else: return False


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(s is None or len(s) == 0):
            return True
        if len(s) % 2 == 1:
            return False
        stack = []
        dictionary = {'(':')','[':']','{':'}'}
        for each in s:
            if each in dictionary:
                stack.append(each)
            else:
                if not stack or dictionary[stack.pop()] != each:
                    return False
                
        return stack == []