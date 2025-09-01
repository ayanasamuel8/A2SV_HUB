# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain=defaultdict(int)
        for cpdomain in cpdomains:
            count,domain_address=cpdomain.split()
            domains=domain_address.split('.')
            for i in range(len(domains)):
                domain['.'.join(domains[i:])]+=int(count)
        return [str(value)+' '+key for key,value in domain.items()]