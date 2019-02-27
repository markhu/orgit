# orgit
organize items by taxonomy (logical hierarchy)

This command-line script `orgit.py` accepts the following commands:

1. CREATE obj
2. LIST (no args)
3. MOVE obj
4. DELETE obj

The object argument might be categories, or items.

Data cached in `data.json` file, and re-written after every operation.

The sample input shown here is also in the `input.txt` file:

```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST
```

## bulk data

Crude-but-effective bulk executions:

```
$ while read line ; do ./orgit.py $line ; done < input.txt 
```

Alternate way to list data (if you have `jq` tool installed, i.e. via `brew install jq`)
```
$ jq . data.json 
```