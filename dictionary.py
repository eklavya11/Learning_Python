#dictionary->key-value

monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April"
}

print(monthConversions)
print(monthConversions["Jan"])#prints value
print(monthConversions.get("Nov","Not a valid key"))#prints value if key is present otherwise default value