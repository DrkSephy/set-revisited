# set-revisited
SET protocol revisited: http://en.wikipedia.org/wiki/Secure_Electronic_Transaction

Overview
--------

When trying to purchase items through a non-trusted third party vendor, it is unfavorable to 
give all of your credit card information to ensure a transaction. A new approach is outlined 
below:

* Client encrypts their data using the banks Public Key, and sends this blob of data 
  to the vendor.

* Vendor then sends this blob of data to the bank, which then decrypts it and returns a 
  boolean regarding whether or not the client does contain the right amount of money.

* The bank then sends the funds to the vendor.

* Vendor gets confirmation that they received the payment.


Implementation
--------------

* Implement a simple client that "purchases items".