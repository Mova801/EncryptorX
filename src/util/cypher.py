from __future__ import annotations
from base64 import b64encode, b64decode, b32encode, b32decode
from re import sub
from dataclasses import dataclass
from string import ascii_lowercase, ascii_uppercase
from typing import Self


@dataclass
class Cypher:
    """
    Class used to modify strings with different methods:
    - hex (Mova801 method)
    - caes (Caesar)
    - xor
    """
    __cyphers_registry: dict
    _lowercase_alphabet: str = ascii_lowercase
    _uppercase_alphabet: str = ascii_uppercase
    __chars_to_ignore: tuple = ('+', '*', '[', ']', '?', '.', '(', ')', '^', '$', '!', '/', '%')

    def __init__(self, encryption_method: str = None, string: str = None, key: int | str = None) -> None:
        self._string = string
        self._key = key
        self.__invalid_data = False

        # Contains every encryption method
        self.__cyphers_registry = {
            "hex": self.__hex_string__,
            "dhex": self.__dhex_string__,
            "caes": self.__caesar_string__,
            "xor": self.__xor_string__
        }

        # Contains every encryption method input check function
        check_registry = {
            "hex": self._check_hex,
            "caes": self._check_caes_xor,
            "xor": self._check_caes_xor
        }
        check = check_registry.get(encryption_method, False)
        if not check:
            self.__invalid_data = True
            raise ValueError(
                f'Invalid encryption_method: {encryption_method}!')

        valid_str, valid_key = check(string, key)
        self._method = encryption_method
        if not valid_str:
            self.__invalid_data = True
            raise ValueError(f"Invalid string : {string}!")
        if not valid_key:
            self.__invalid_data = True
            raise ValueError(f"Invalid key : {key}!")

    def __str__(self) -> str:
        return f"Cypher({self._method})" + "{" + f"string: {self._string} | key: {self._key} | valid data: {self.__invalid_data}" + "}"

    def _combination(self) -> tuple:
        return self._string, self._key

    def _check_hex(self, string, key) -> tuple[bool, bool]:
        """ Checks if the given string and key can be used without causing problems for the HEX cyphers. """
        valid_str: bool = bool(isinstance(string, str) and string)
        if isinstance(key, str):
            valid_key: bool = len(key) > 3 and key[3] == "#"
            if valid_key:
                self.__locked = True
        else:
            valid_key: bool = isinstance(key, int)
        return valid_str, valid_key

    def _check_caes_xor(self, string, key) -> tuple[bool, bool]:
        """
        Checks if the given string and key can be used without causing problems 
        for the CAES and the XOR cyphers.
        """
        valid_str: bool = isinstance(string, str) and string
        valid_key: bool = isinstance(key, int)
        return valid_str, valid_key

    def encoding(self, encoding: str = None, **kwargs: dict) -> Self | tuple[int, int]:
        """
        Returns the given string encoded with the specified encoding type.
        """
        string = self._string
        match encoding:
            case "hex":
                if string.startswith("0x"):
                    raise ValueError(
                        f"Cannot convert base 16 to base 16: {string}")
                self._string = hex(int(self._combination()[0]))
            case "base32":
                string_bytes = string.encode("utf-8")
                base64_bytes = b32encode(string_bytes)
                self._string = base64_bytes.decode("utf-8")
            case "base64":
                string_bytes = string.encode("utf-8")
                base64_bytes = b64encode(string_bytes)
                self._string = base64_bytes.decode("utf-8")

        if kwargs.get("get_tuple"):
            return self._combination()
        return self

    def decoding(self, encoding: str = None, **kwargs: dict) -> Self | tuple[int, int]:
        """
        Returns the given string decoded with the specified encoding type.
        """
        string = self._string
        match encoding:
            case "base32":
                string_bytes = string.encode("utf-8")
                base32_bytes = b32decode(string_bytes)
                self._string = base32_bytes.decode("utf-8")

            case "base64":
                string_bytes = string.encode("utf-8")
                base64_bytes = b64decode(string_bytes)
                self._string = base64_bytes.decode("utf-8")
        if kwargs.get("get_tuple"):
            return self._combination()
        return self

    def generate_key(self):
        """ Generate a random key. """
        pass

    def _substitute(self, letter: str) -> str:
        """
        Given a letter and a string, substitute every occurrence of the given letter
        with its unicode value, plus a key value in the string. 
        Returns the number of digits of the unicode value as a string. 
        """
        proto_string = self._string
        shifted_letter = ord(letter) + self._key
        if letter not in self.ignore_letters:
            self.ignore_letters.append(letter)
            if letter in self.__chars_to_ignore:
                letter = rf"\{letter}"
            self._string = sub(letter, str(shifted_letter), proto_string)
        return str(len(str(shifted_letter)))

    def _build_hex_key(self, proto_keybody: str) -> str:
        """
        Build the HEX cypher final key (encrypted).
        Return: hex(key)#hex(key_body)
        """
        return f"{hex(self._key)}#{hex(int(proto_keybody))}"

    def __hex_string__(self) -> tuple[int, int]:
        self.ignore_letters = []

        proto_keybody = "".join(self._substitute(letter) for letter in self._string)
        # scambio ogni lettera con il suo intero unicode e ne salvo il numero di cifre in una lista
        # genera la hex stringa
        self._string = hex(int(self._string))
        # genera la hex chiave
        self._key = self._build_hex_key(proto_keybody)
        del self.ignore_letters
        return self._combination()

    def refined_unshift_letter(self, letter_len) -> str:
        proto_string = self._string
        unshifted_letter = int(proto_string[:int(letter_len)])
        self._string = proto_string[int(letter_len):]
        return chr(unshifted_letter - self._key)

    def __dhex_string__(self) -> tuple[int, int]:
        # passo da base 16 a base 10
        try:
            self._string = str(int(self._string, 16))
            key, proto_keybody = self._key.split("#", 1)
            proto_keybody = str(int(proto_keybody, 16))
            self._key = int(key, 16)
        except ValueError:
            return tuple((self._string, self._key))
        self._string = "".join(self.refined_unshift_letter(letter_len) for letter_len in proto_keybody)
        # self._string = "".join(map(self.refined_unshift_letter, proto_keybody))
        return self._combination()

    @property
    def low_alphabet(self) -> str:
        return self._lowercase_alphabet

    @property
    def upp_alphabet(self) -> str:
        return self._uppercase_alphabet

    def _shift(self, letter: str) -> str:
        """
        Shifts a letter of the alphabet by a certain value (key) and returns the shifted letter.
        If the maximum len of the alphabet is reached, the shifted letter is equal to the
        initial shifted letter minus the len of the alphabet.
        """
        low_alphabet = self.low_alphabet
        upp_alphabet = self.upp_alphabet
        if letter in low_alphabet:
            alphabet = low_alphabet
        elif letter in upp_alphabet:
            alphabet = upp_alphabet
        else:
            return letter
        shifted_pos = ord(letter) + self._key
        if shifted_pos <= ord(alphabet[-1]):
            return chr(shifted_pos)
        else:
            return chr(shifted_pos - len(alphabet))

    def __caesar_string__(self) -> tuple[int, int]:
        # scambio ogni lettera con il suo intero unicode e ne salvo il numero di cifre in una lista
        self._string = "".join(self._shift(letter) for letter in self._string)
        # self._string  = "".join(map(self._shift, self._string))
        return self._combination()

    def __xor_string__(self) -> tuple[int, int]:
        self._string: str = "".join([chr(ord(char) ^ self._key) for char in self._string])
        return self._combination()

    def _start_cyphers(self, method: str, get_tuple: bool) -> Self | tuple[int, int]:
        cyphers = self.__cyphers_registry.get(method)
        data = cyphers()
        if get_tuple:
            return data
        return self

    def lock(self, **kwargs: dict) -> Self | tuple[int, int]:
        """
        Use the chosen cyphers (hex, caes, xor) to encrypt the given string using the given key.
        If the string has already been locked, the operation is aborted.
        Returns the Cypher object; to get the tuple(string, key) the flag (get_tuple=True) must the True.
        """
        get_tuple: bool = kwargs.get("get_tuple", False)
        if self.__invalid_data:
            if get_tuple:
                return self._combination()
            return self
        return self._start_cyphers(self._method, get_tuple)

    def unlock(self, **kwargs: dict) -> Self | tuple[int, int]:
        """
        Use the chosen cyphers (hex, caes, xor) to decrypt the given string using the given key.
        If the string has already been unlocked, the operation is aborted and 
        a tuple(string, key) is returned.
        Returns the Cypher object; to get the tuple(string, key) the flag (get_tuple=True) must the True.
        """
        get_tuple: bool = kwargs.get("get_tuple", False)
        if self.__invalid_data:
            if get_tuple:
                return self._combination()
            return self
        method: str = self._method if self._method != "hex" else "dhex"
        return self._start_cyphers(method, get_tuple)
