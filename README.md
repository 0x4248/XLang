# XLang

XLang is a format for storing language strings in XML files. It is designed to be easy to read and write, and easy to parse.

XLang allows you to speed up the process of localising your application by providing a simple, easy-to-use format for storing language strings.

## Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<XLang version="1.0">
    <meta>
        <name>Demo</name>
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