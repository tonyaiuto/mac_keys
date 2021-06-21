# mac_keys

Tips for using other keyboards with macos.

This is mostly tables to map keys to useful behavior.
Then there are simple tools to turn that into the
commands you need to remap your macos device.

## Getting the left hand modifiers into shape

Let's assume you have the typical layout on the side.

```
[capslock]   A
[shift     ] Z
[ctrl] [alt] [space bar ]
```
And you want it to be useful
```
[ctrl]   A
[shift     ] Z
[⌥] [⌘] [space bar ]
```

You can do most of this with System Preferences.
`[System Preferences] > [Keyboard] -> [Modifier Keys...]` brings up the menu.

```
  Caps Lock Key: ^ Control
 Contrl (^) Key: ⌥ Option
 Option (⌥) Key: ⌘ Command
Command (⌘) Key: ⌘ Command
```

Use `Mission Control` to map F4 to Mission Control and F3 to Application Windows.


## How to remap arbitrary keys

I want to fix my keyboard further.
- The key to the left of the '1' should be escape.
- F8, F9, F10 should be mute, volume down, volume up

You can do that with hidutil. 

- Create a list of remaps. See `goldtouch.txt` for an example.
- Use `make_hidutil_command.py` to turn that into hidutil commands.
```
#!/bin/bash
# This script should be executable
# Use Automator to turn this into an action
# Have that action run at startup
# ESC -> `
# ` -> ESC
# F8 -> Mute
# F9 -> vol down
# F10 -> vol up
# caps-lock -> control
# menu key in upper right -> power
hidutil property --set '{"UserKeyMapping":[
{"HIDKeyboardModifierMappingSrc":0x700000029,"HIDKeyboardModifierMappingDst":0x700000035},
{"HIDKeyboardModifierMappingSrc":0x700000035,"HIDKeyboardModifierMappingDst":0x700000029},
{"HIDKeyboardModifierMappingSrc":0x700000041,"HIDKeyboardModifierMappingDst":0x70000007F},
{"HIDKeyboardModifierMappingSrc":0x700000042,"HIDKeyboardModifierMappingDst":0x700000081},
{"HIDKeyboardModifierMappingSrc":0x700000043,"HIDKeyboardModifierMappingDst":0x700000080},
{"HIDKeyboardModifierMappingSrc":0x700000039,"HIDKeyboardModifierMappingDst":0x7000000E0},
{"HIDKeyboardModifierMappingSrc":0x700000065,"HIDKeyboardModifierMappingDst":0x700000066}
]}'
```
- Use automator to create an App to run the script.
- Set up that app to run at login.

## How to discover key codes

- Must reading: [Universal Serial Bus (USB) HID Usage Tables 10/28/2004 Version 1.12](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf)
- Use wireshark
- Use the XHC20 interface
- You might have to bring it up first `sudo ifconfig XHC20 up`
- Filter to the device. For me, that was usb.src == "18.14.1"
- Each key sends 4 events.  The first one has the "usage id'
  in the 2a'th (hex) byte.

## Goldtouch

Most keys are in the right place and deliver the expected keycode.
We only have to remap a few.
