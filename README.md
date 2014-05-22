# Android SMS Backup Reader - 0.0.1
Simple Python terminal program that takes the XML file generated by SMS backup apps and translates it to a readable text file.

You will need at minimum `Python 3` possibly `Python 3.4` to use. Have not yet tested on other versions other than `3.4` ... :(

## Usage

-----

Say we have the following backup XML file:

`sms-11-10-12.xml`
```
<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<?xml-stylesheet type="text/xsl" href="sms.xsl"?>
<smses count="2">
  <sms protocol="0" address="0000000000" date="1352597621411" type="1" subject="null" body="Hello" toa="null" sc_toa="null" service_center="null" read="1" status="-1" locked="0" date_sent="0" readable_date="Nov 10, 2012 7:33:41 PM" contact_name="John Doe" />
  <sms protocol="0" address="0000000000" date="1352598118191" type="2" subject="null" body="World" toa="null" sc_toa="null" service_center="000000000000" read="1" status="-1" locked="0" date_sent="1352598119000" readable_date="Nov 10, 2012 7:41:58 PM" contact_name="John Doe" />
 </smses>
```

Now we can easily pick through and read it, but why would you? Run it through `Reader.py` and we get the following output as a text file:

`parsed_sms-11-10-12.xml.txt`
```
Nov 10, 2012 7:33:41 PM
John Doe
Hello

Nov 10, 2012 7:41:58 PM
John Doe
World

```