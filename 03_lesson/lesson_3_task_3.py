from address import Address
from mail import Mailing


sender_address = Address(101000, 'Москва', 'Арбат', 25, 12)
recipient_address = Address(630099, 'Новосибирск', 'Красный проспект', 45, 78)


mail = Mailing(recipient_address, sender_address, 5220, 45876525895147)

r = mail.format_mailing()
print(r)
