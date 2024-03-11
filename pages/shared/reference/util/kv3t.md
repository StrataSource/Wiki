---
title: kv3t
---

# kv3t

kv3t is a command line utility that converts KeyValues3 files to and from any format or encoding. The utility can also convert KeyValues1 files into KeyValues3. It is available for Windows and Linux.

Supported formats:
* `generic`

Supported encodings:
* `text`
* `binary`
* `binary_bc` (block-compressed binary)

Supported input files:
* Any KV3 file
* text KeyValues1

## Help Text

```
------------------------------------------------------------------
KV3T - A tool for dealing with KeyValues3 files
KeyValues3 - Copyright (c) Valve Corporation, All rights reserved.
Tool developed by the Strata Source Team
------------------------------------------------------------------
SYNOPSIS
kv3t <input> [options] [-o output]

DESCRIPTION
        Read and convert KeyValues3 ("KV3") files from and to any format. If no output is specified, print to stdout as text.
        KV3 input formats and encoding will be automatically detected.

COMMAND-LINE OPTIONS
        -inh | --input-no-header
                Specify that your input file doesn't have a header. Interpret as 'generic' and 'text', which is not guaranteed to work.
        -ikv1 | --input-is-kv1
                Specify that the input file is in the original KeyValues format ("KV1") and try to convert it.
                Doesn't support advanced conversion rules for now.
        -ikv1es | --input-kv1-escape-sequences
                Enable escape sequence support for KV1 input files.
        --kv1-multiroot
                Enable support for multiple root keys. Needed for sound scripts, VMF, etc.
        -of <FORMAT> | --output-format <FORMAT>
                Request a special KV3 output format. Only 'generic' (default) is supported for now.
        -oe <ENCODING> | --output-encoding <ENCODING>
                Request a special KV3 output encoding when writing to a file. Supports 'text' for plain text (default),
                'binary' for simple binary encoding and 'binary_bc' for block-compressed binary encoding
```

## Usage Examples

Example 1: Convert binary KeyValues3 to text
```
kv3t myfile.kv3 -oe text myfile_text.kv3
```

Example 2: Convert text KeyValues3 to binary compressed
```
kv3t myfile_text.kv3 -oe binary_bc myfile.kv3
```