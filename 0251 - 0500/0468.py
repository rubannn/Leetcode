class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def tryconvert(n, base):
            try:
                int(n, base)
                return True
            except Exception as e:
                return False

        ip = queryIP.split('.')
        if len(ip) == 4:
            for x in ip:
                if not tryconvert(x, 10):
                    return "Neither"
                num = int(x)
                if not (0<= num <= 255) or len(str(num)) != len(x):
                    return "Neither"
            return "IPv4"

        ip = queryIP.split(':')
        if len(ip) == 8:
            for x in ip:
                if not tryconvert(x, 16):
                    return "Neither"
                num = int(x, 16)
                if not (0<= num <= int('ffff', 16)) or len(x) > 4:
                    return "Neither"
            return "IPv6"
        return "Neither"
