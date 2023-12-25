# XLang

XLang is a format for storing language strings in XML files. It is designed to be easy to read and write, and easy to parse.

## Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<XLang>
    <meta>
        <name>Demo</name>
        <version>1.0</version>
        <author>John Doe</author>
        <description>This is a demo file.</description>
    </meta>
    <strings>
        <string name="welcome">
            <en>Welcome to XLang!</en>
            <de>Willkommen bei XLang!</de>
            <fr>Bienvenue à XLang!</fr>
        </string>
    </strings>
</XLang>
```

## Licence

This project is licenced under the GNU Public Licence v3.0. See [LICENCE](LICENCE) for more information.