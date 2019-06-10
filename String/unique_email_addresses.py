def numUniqueEmails(self, emails):
        """
        https://leetcode.com/problems/unique-email-addresses/submissions/
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            print local
            print domain
            if '+' in local:
                local = local[:local.index('+')]
            unique_emails.add(local.replace('.','') + '@' + domain)
        return len(unique_emails)
