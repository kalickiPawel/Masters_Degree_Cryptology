from Crypto.Hash import SHA256
from rsa_modules import Plain
import logging

logger = logging.getLogger(__name__)


class Fdh(Plain):
    """
    Improved PlainRSA scheme to the version with attachment (RSA-FDH),
    i.e. this algorithm uses a hash function (signed (encrypted) the
    private key is the message shortcut, not the message itself.)
    """

    def __init__(self, size):
        super().__init__(size)

    @staticmethod
    def generate_hash(m):
        h = SHA256.new()
        h.update(bytes(m, 'ascii'))
        logger.info('Message with hash: {}'.format(int(h.hexdigest(), 16)))
        return int(h.hexdigest(), 16)

    def encrypt_message(self, m):
        m = self.generate_hash(m)
        return super().encrypt_message(m)

    def decrypt_message(self, c):
        return super().decrypt_message(c)

    def validation(self, c, m):
        logger.warning("Start validation")
        decrypt = self.decrypt_message(c)
        return m == decrypt
