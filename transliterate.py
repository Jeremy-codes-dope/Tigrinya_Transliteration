import pandas as pd

# Mapping of Ge'ez (Tigrinya) script to Latin equivalents
transliteration_map = {
    'ሀ': 'he', 'ሁ': 'hu', 'ሂ': 'hi', 'ሃ': 'ha', 'ሄ': 'he', 'ህ': 'hə', 'ሆ': 'ho',
    'ለ': 'le', 'ሉ': 'lu', 'ሊ': 'li', 'ላ': 'la', 'ሌ': 'le', 'ል': 'lə', 'ሎ': 'lo',
    'ሐ': 'ḥe', 'ሑ': 'ḥu', 'ሒ': 'ḥi', 'ሓ': 'ḥa', 'ሔ': 'ḥe', 'ሕ': 'ḥə', 'ሖ': 'ḥo',
    'መ': 'me', 'ሙ': 'mu', 'ሚ': 'mi', 'ማ': 'ma', 'ሜ': 'me', 'ም': 'mə', 'ሞ': 'mo',
    'ሠ': 'se', 'ሡ': 'su', 'ሢ': 'si', 'ሣ': 'sa', 'ሤ': 'se', 'ሥ': 'sə', 'ሦ': 'so',
    'ረ': 're', 'ሩ': 'ru', 'ሪ': 'ri', 'ራ': 'ra', 'ሬ': 're', 'ር': 'rə', 'ሮ': 'ro',
    'ሰ': 'se', 'ሱ': 'su', 'ሲ': 'si', 'ሳ': 'sa', 'ሴ': 'se', 'ስ': 'sə', 'ሶ': 'so',
    'ሸ': 'she', 'ሹ': 'shu', 'ሺ': 'shi', 'ሻ': 'sha', 'ሼ': 'she', 'ሽ': 'shə', 'ሾ': 'sho',
    'ቀ': 'qe', 'ቁ': 'qu', 'ቂ': 'qi', 'ቃ': 'qa', 'ቄ': 'qe', 'ቅ': 'qə', 'ቆ': 'qo',
    'በ': 'be', 'ቡ': 'bu', 'ቢ': 'bi', 'ባ': 'ba', 'ቤ': 'be', 'ብ': 'bə', 'ቦ': 'bo',
    'ቨ': 've', 'ቩ': 'vu', 'ቪ': 'vi', 'ቫ': 'va', 'ቬ': 've', 'ቭ': 'və', 'ቮ': 'vo',
    'ተ': 'te', 'ቱ': 'tu', 'ቲ': 'ti', 'ታ': 'ta', 'ቴ': 'te', 'ት': 'tə', 'ቶ': 'to',
    'ቸ': 'che', 'ቹ': 'chu', 'ቺ': 'chi', 'ቻ': 'cha', 'ቼ': 'che', 'ች': 'cə', 'ቾ': 'cho',
    'ኀ': 'ḫe', 'ኁ': 'ḫu', 'ኂ': 'ḫi', 'ኃ': 'ḫa', 'ኄ': 'ḫe', 'ኅ': 'ḫə', 'ኆ': 'ḫo',
    'ነ': 'ne', 'ኑ': 'nu', 'ኒ': 'ni', 'ና': 'na', 'ኔ': 'ne', 'ን': 'nə', 'ኖ': 'no',
    'ኘ': 'ñe', 'ኙ': 'ñu', 'ኚ': 'ñi', 'ኛ': 'ña', 'ኜ': 'ñe', 'ኝ': 'ñə', 'ኞ': 'ño',
    'አ': 'e', 'ኡ': 'u', 'ኢ': 'i', 'ኣ': 'a', 'ኤ': 'e', 'እ': 'ə', 'ኦ': 'o',
    'ከ': 'ke', 'ኩ': 'ku', 'ኪ': 'ki', 'ካ': 'ka', 'ኬ': 'ke', 'ክ': 'kə', 'ኮ': 'ko',
    'ኸ': 'ḫe', 'ኹ': 'ḫu', 'ኺ': 'ḫi', 'ኻ': 'ḫa', 'ኼ': 'ḫe', 'ኽ': 'ḫə', 'ኾ': 'ḫo',
    'ወ': 'we', 'ዉ': 'wu', 'ዊ': 'wi', 'ዋ': 'wa', 'ዌ': 'we', 'ው': 'wə', 'ዎ': 'wo',
    'ዐ': 'a', 'ዑ': 'u', 'ዒ': 'i', 'ዓ': 'a', 'ዔ': 'e', 'ዕ': 'ə', 'ዖ': 'o',
    'ዘ': 'ze', 'ዙ': 'zu', 'ዚ': 'zi', 'ዛ': 'za', 'ዜ': 'ze', 'ዝ': 'zə', 'ዞ': 'zo',
    'ዠ': 'že', 'ዡ': 'žu', 'ዢ': 'ži', 'ዣ': 'ža', 'ዤ': 'že', 'ዥ': 'žə', 'ዦ': 'žo',
    'የ': 'ye', 'ዩ': 'yu', 'ዪ': 'yi', 'ያ': 'ya', 'ዬ': 'ye', 'ይ': 'yə', 'ዮ': 'yo',
    'ደ': 'de', 'ዱ': 'du', 'ዲ': 'di', 'ዳ': 'da', 'ዴ': 'de', 'ድ': 'də', 'ዶ': 'do',
    'ጀ': 'je', 'ጁ': 'ju', 'ጂ': 'ji', 'ጃ': 'ja', 'ጄ': 'je', 'ጅ': 'jə', 'ጆ': 'jo',
    'ገ': 'ge', 'ጉ': 'gu', 'ጊ': 'gi', 'ጋ': 'ga', 'ጌ': 'ge', 'ግ': 'gə', 'ጎ': 'go',
    'ጠ': 'ṭe', 'ጡ': 'ṭu', 'ጢ': 'ṭi', 'ጣ': 'ṭa', 'ጤ': 'ṭe', 'ጥ': 'ṭə', 'ጦ': 'ṭo',
    'ጨ': 'č̣e', 'ጩ': 'č̣u', 'ጪ': 'č̣i', 'ጫ': 'č̣a', 'ጬ': 'č̣e', 'ጭ': 'č̣ə', 'ጮ': 'č̣o',
    'ጰ': 'p̣e', 'ጱ': 'p̣u', 'ጲ': 'p̣i', 'ጳ': 'p̣a', 'ጴ': 'p̣e', 'ጵ': 'p̣ə', 'ጶ': 'p̣o',
    'ጸ': 'ṣe', 'ጹ': 'ṣu', 'ጺ': 'ṣi', 'ጻ': 'ṣa', 'ጼ': 'ṣe', 'ጽ': 'ṣə', 'ጾ': 'ṣo',
    'ፀ': 'tse', 'ፁ': 'tsu', 'ፂ': 'tsi', 'ፃ': 'tsa', 'ፄ': 'tse', 'ፅ': 'tsə', 'ፆ': 'tso',
    'ፈ': 'fe', 'ፉ': 'fu', 'ፊ': 'fi', 'ፋ': 'fa', 'ፌ': 'fe', 'ፍ': 'fə', 'ፎ': 'fo',
    'ፐ': 'pe', 'ፑ': 'pu', 'ፒ': 'pi', 'ፓ': 'pa', 'ፔ': 'pe', 'ፕ': 'pə', 'ፖ': 'po'
    # Add more mappings for all Tigrinya characters here...
}

# Function to transliterate a single name
def transliterate_name(tigrinya_name):
    transliterated_name = ""
    for char in tigrinya_name:
        if char in transliteration_map:
            transliterated_name += transliteration_map[char]
        else:
            transliterated_name += char  # Keep character as-is if no mapping found
    return transliterated_name

# Function to transliterate a column of names in an Excel file
def transliterate_excel(file_path, sheet_name='Sheet1', name_column='Names'):
    # Read Excel file
    df = pd.read_excel(C:\Users\Jeremiah\Documents\Prog Projects\Tigrinya_Transliteration, sheet_name=sheet1)
    
    # Transliterate names in the specified column
    df['Transliterated_Names'] = df[B377].apply(transliterate_name)
    
    # Save the result to a new Excel file
    output_file = C:\Users\Jeremiah\Documents\Prog Projects\Tigrinya_Transliteration.replace('.xlsx', '_transliterated.xlsx')
    df.to_excel(output_file, index=False)
    
    print(f"Transliterated names saved to: {output_file}")

# Example usage
if __name__ == "__main__":
    # Path to your Excel file
    excel_file = 'names_list.xlsx'
    
    # Transliterate the names and save to a new file
    transliterate_excel(excel_file)
