"""Birch is an HTML rendering library
"""

# Import os library for filepath management
import os
# Typing for better predictive typings
import typing
# Regex for string matching
import re

class RePattern:
    BIRCH_ENTRIES = re.compile("{% *[A-z|0-9| |_]* *%}")

class BirchRenderer(object):
    def __init__(self, html_directory:str="pages") -> None:
        self.html_directory = html_directory
        self.global_scope = {}
    
    def set_global_scope_entry(self, key:str, value:typing.Any) -> None:
        """Sets a global scope value.

        Args:
            key (str): The key for this value.
            value (typing.Any): The value.
        """
        self.global_scope[key] = value
    
    def render(self, filepath:str, **scope) -> str:
        """Renders an HTML file.
        Raises OSError if file cannot be read.

        Args:
            filepath (str): The path of the HTML file.

        Returns:
            str: The rendererd HTML
        """

        # Get the full filepath and read the content
        full_path = os.path.join(self.html_directory, filepath)
        with open(full_path) as buffer:
            file_content = buffer.read()
        
        # Modify file content as required here
        
        # Find {%% ... %%} regex matches
        r = re.finditer(RePattern.BIRCH_ENTRIES, file_content)

        matches = reversed([m.span() for m in r])

        # TODO: Separate matches into
        # arguments, "space delimited".
        for span in matches:
            match = file_content[span[0]:span[1]]
            match_content = match[2:-2].strip()

            scope_value = scope.get(match_content, self.global_scope.get(match_content, "Undefined"))
            match_result = str(scope_value)

            # Replace the portion of the string
            file_content = file_content[:span[0]] + match_result + file_content[span[1]:]

        # Return the modified file content
        return file_content