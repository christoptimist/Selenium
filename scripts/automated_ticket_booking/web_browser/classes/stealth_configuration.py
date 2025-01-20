import random

class StealthConfiguration:
    def __init__(self,
                 languages = ["en-US", "en-GB", "es", "fr"], 
                 vendor_list = ["Google Inc.", "Mozilla", "Apple Inc."],
                 platform_list = ["Win32", "MacIntel", "Linux x86_64"],
                 webgl_vendor_list = ["Intel Inc.", "AMD", "NVIDIA"],
                 renderer_list = ["Intel Iris OpenGL Engine", "AMD Radeon (TM) Graphics", "NVIDIA GeForce GTX 1060/PCIe/SSE2"],
                 fix_hairline = True,
                 canvas_method = {
                     "getText": lambda: f"random_text_num_{random.randint(1, 10)}",
                     "isOffscreenCanvasSupported": lambda: random.choice([True, False])
                 }
                 ):
        
        self.languages = random.choice(languages)
        self.vendor = random.choice(vendor_list)
        self.platform = random.choice(platform_list)
        self.webgl_vendor = random.choice(webgl_vendor_list)
        self.renderer = random.choice(renderer_list)
        self.fix_hairline = fix_hairline
        self.canvas_method = canvas_method
        