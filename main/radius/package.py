import hashlib
import hmac

import six


def calculate_HMAC_MD5(pkt):

    origin_ma = pkt["Message-Authenticator"]

    # the last element of the request package is a Message-Authenticator
    # replace the original raw Message-Authenticator with the default value to re-calculate the hash
    pkt["Message-Authenticator"] = 16 * six.b("\x00")

    raw_packet = pkt.RequestPacket()

    #reset old data
    pkt["Message-Authenticator"] = origin_ma[0]

    digest = hmac.new(pkt.secret, raw_packet, hashlib.md5)

    dig = digest.digest()

    return dig
