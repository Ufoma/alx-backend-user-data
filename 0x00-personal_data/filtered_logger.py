#!/usr/bin/env python3

import re

def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specific fields in a log message.

    Args:
        fields (list): A list of field names (strings) to obfuscate.
        redaction (str): The string to replace field values with.
        message (str): The log line containing fields to be filtered.
        separator (str): The character that separates fields in the log line.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    # Create a regex pattern to match each specified field and its value
    # This pattern finds fields formatted as "field=value" up to the separator.
    pattern = r'(' + '|'.join(f"{field}=[^{separator}]*" for field in fields) + ')'
    
    # Use re.sub to replace matched field values with the redaction string
    # Lambda ensures only the value after '=' is replaced, keeping field names intact
    return re.sub(pattern, lambda x: f"{x.group(0).split('=')[0]}={redaction}", message)
