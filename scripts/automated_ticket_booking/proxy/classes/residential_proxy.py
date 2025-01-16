from proxy.interfaces.i_residential_proxy_options import IResidentialProxyOptions

class ResidentialProxy(IResidentialProxyOptions):
    def __init__(self):
        self.proxy = None

    def get_residential_proxy(self):
        options = {
             'proxy': {
                'http': "http://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2334",
                'https': "https://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2334",
                'http': "socks5://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2333",
                'https': "socks5://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2333"
            }
        }
        self.proxy = options
        return self.proxy