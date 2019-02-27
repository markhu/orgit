# orgt
organize items by taxonomy (logical hierarchy)

This command-line script accepts the following commands:

1. CREATE obj
2. LIST (no args)
3. MOVE obj
4. DELETE obj

The objects might be categories, or items.

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
