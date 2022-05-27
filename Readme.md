
# Template Autometa

## Example template file
```
To,
$0

Subject: Application to be a part of your organization.

Respected Sir/Ma'am,
Hello, This is $1, from $2. I found about your organization the other day and is eager to join you.

I am a $3 and have good experience in $4. Kindly let me know if there is any vacancy.

Thanking you,
$1
```


## Example Info.json File

```json
{
    "treemail.txt":["Head of The Tree Cap","Sujal Choudhari","India","Software Developer","Environmental Studies"],
    "oceanmail.md":["Head of CleanOcean","Sujal","Canada","Marine Biologist","Oceans and Biodiversity"],
    "child.rst":["Dr. Stranger","Sujal Choudhari","Europe","Psycologist","Child Psychology"]
}
```

## Expected Output (child.rst)
```
To,
Dr. Stranger

Subject: Application to be a part of your organization.

Respected Sir/Ma'am,
Hello, This is Sujal Choudhari, from Europe. I found about your organization the other day and is eager to join you.

I am a Psycologist and have good experience in Child Psychology. Kindly let me know if there is any vacancy.

Thanking you,
Sujal Choudhari
```