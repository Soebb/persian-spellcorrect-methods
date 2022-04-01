import re


class PersianEditor:
    """
    A class for Persian Text Sanitization
    """
    def __init__(self, text):
        """
        This is the base part of the class
        """

        self.text = text
        self._cleanup_zwnj = False
        self._fix_dashes = True
        self._fix_three_dots = True
        self._fix_hamzeh = True
        self._hamzeh_with_yeh = True
        self._fix_prefix_spacing = True
        self._fix_prefix_separate = True
        self._fix_suffix_spacing = True
        self._fix_suffix_separate = True
        self._aggresive = True
        self._cleanup_kashidas = True
        self._fix_english_quotes = True
        self._cleanup_extra_marks = True
        self._cleanup_spacing = True
        self._fix_spacing_for_braces_and_quotes = True
        self._fix_arabic_numbers = True
        self._fix_english_numbers = True
        self._fix_misc_non_persian_chars = True

        UnTouchable() # to generate the untouchable words
        # self.dont_touch_list_gen()
        self.cleanup()





    def fix_prefix_separate_func(self):
        """
        """
        # I removed punctioations here but I dont know why its work :D
        regex = re.compile(r"\A(ن?می)(\S+)") #  \A for words like سهمیه

        # This is a little parser that split whole string from spaces
        # and put it to list
        # all lists words will be test one by one and space if need
        wlist = self.text.split(" ")
        for word in wlist:
            p = regex.search(word)
            if p:
                # Here I'll check the word wasn't something like میلاد
                if p.group() not in UnTouchable.words:
                    # This little one was really tricky!
                    # regex grouping is really awesome ;-)
                    self.text = re.sub(
                        p.group(),
                        p.group(1) + r"‌" + p.group(2) ,
                        self.text
                    )

    def fix_suffix_separate_func(self):
        """
        to add virtual space in words with suffix (haye, ...)
        that are not spaced correctly ;-)
        """
        regex = re.compile(
            r"""(\S+)
            (تر(ی(ن)?)?
            |ها(ی(ی)?)?|
            [تمش]ان)\b""",
            re.VERBOSE
        )
        # This is a little parser that split whole string from spaces
        # and put it to list all lists words will be test
        # one by one and space if need
        wlist = self.text.split(" ")
        for word in wlist:
            p = regex.search(word)
            if p:
                # Here I'll check the word wasn't something like بهتر
                if p.group() not in UnTouchable.words:
                    self.text = re.sub(
                        p.group(),
                        p.group(1) + r"‌" + p.group(2) ,
                        self.text
                    )


class UnTouchable:
    DATAFILE = "untouchable.dat"
    words = set() # a set storing all untouchable words

    @classmethod
    def __init__(cls):
        cls.generate()

    @classmethod
    def get(cls):
        return cls.words

    @classmethod
    def add(cls, word_list):
        # TODO: What da fuck? No write access to file-system
        # Should be changed to another way
        with open(cls.DATAFILE, "a", encoding="utf8") as f:
            for word in word_list:
                if word not in cls.words:
                    f.write(word+"\n")
                    cls.words.add(word)

    @classmethod
    def generate(cls):
        """
        This method generates a Unicode list from 'data/untouchable.dat'
        containing such words like 'بهتر' or 'میلاد' which suffixes/prefixes functions
        should not have to touch them
        """
        with open(cls.DATAFILE, encoding='utf8') as f:
            for line in f:
                # I had to strip the f.readline() to prevent white spaces
                cls.words.add(line.strip())
