class StealthConfiguration:
    def __init__(self,
                 languages = ["en-US","en"],
                 vendor = "Google Inc",
                 platform = "Win32",
                 webgl_vendor = "Intel Inc",
                 renderer = "Intel Iris OpenGL Engine",
                 fix_hairline = True
                 ):
        
        self.languages = languages
        self.vendor = vendor
        self.platform = platform
        self.webgl_vendor = webgl_vendor
        self.renderer = renderer
        self.fix_hairline = fix_hairline
        