from base64 import b64encode


def hex_to_b64(hexed: hex) -> bytes:
	some_bytes = bytes.fromhex(hexed)
	return b64encode(some_bytes)

assert hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
