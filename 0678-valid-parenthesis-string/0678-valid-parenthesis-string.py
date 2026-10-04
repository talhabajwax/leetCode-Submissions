class Solution:
    def checkValidString(self, s: str) -> bool:
        openstack=[]
        star=[]
        for i,ch in enumerate(s):
            if ch=='(':
                openstack.append(i)
            if ch== '*':
                star.append(i)
            if ch==')':
                if openstack:
                    openstack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while openstack and star:
            if star[-1] > openstack[-1]:
                openstack.pop()
                star.pop()
            else:
                return False

        return not openstack