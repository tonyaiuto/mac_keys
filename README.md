# mac_keys

Using other keyboards with macos.

This is mostly tables to map keys to useful behavior.
Then there are simple tools to turn that into the
commands you need to remap your macos device.

Must reading:
```
Universal Serial Bus (USB)
HID Usage Tables
10/28/2004
Version 1.12
https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
```

## How to use this on a mac

- create a script of the hidutil commands
- use automator to create an App to run the script
- Set up that app to run at login.

## How to discover key codes

- Use wireshark
- Use the XHC20 interface
- You might have to bring it up first `sudo ifconfig XHC20 up`
- Filter to the device. For me, that was usb.src == "18.14.1"
- Each key sends 4 events.  The first one has the "usage id'
  in the 2a'th (hex) byte.

## Goldtouch

Most keys are in the right place and deliver the expected keycode.
We only have to remap a few
