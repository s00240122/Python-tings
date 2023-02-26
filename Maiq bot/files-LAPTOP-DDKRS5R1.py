import discord

gibbal_id = 698905167629647882

maiq_quotes = [
    "M'aiq's father was also called M'aiq. As was M'aiq's father's father. At least, that is what his father said. But then again, you can never trust a liar.",
    "M'aiq wishes you well.",
    "M'aiq knows much, tells some. M'aiq knows many things others do not.",
    "M'aiq carries two weapons, to be safe. What if one breaks? That would be most unlucky.",
    "M'aiq is always in search of calipers, yet he finds none. Where could they have gone?",
    "How does anyone know there was a city of Winterhold? M'aiq did not see it with his eyes. Did you?",
    "Too much magic can be dangerous. M'aiq once had two spells and burned his sweetroll.",
    "What does this mean, to combine magic? Magic plus magic is still magic.",
    "Some say Alduin is Akatosh, some say M'aiq is a Liar. Don't you believe either of those things.",
    "It does not matter to M'aiq how strong or smart one is. It only matters what one can do.",
    "Dragons were never gone. They were just invisible and very, very quiet.",
    "Werebears? Where? Bears? Men that are bears?",
    "Much snow in Skyrim. Enough snow. M'aiq does not want it anymore.",
    "Snow falls. Why worry where it goes? M'aiq thinks the snowflakes are pretty.",
    "M'aiq once walked to High Hrothgar. So many steps, he lost count.",
    "Once M'aiq got into trouble in Riften, and fled to Windhelm. It is good that nobody there cared.",
    "M'aiq can travel fast across the land. Some lazy types take carriages. It is all the same to M'aiq.",
    "M'aiq saw a mudcrab the other day. Horrible creatures.",
    "M'aiq loves the people of Skyrim. Many interesting things they say to each other.",
    "Nords are so serious about beards. So many beards. M'aiq thinks they wish they had glorious manes like Khajiit.",
    "M'aiq does not remember his childhood. Perhaps he never had one.",
    "M'aiq is very practical. He has no need for mysticism.",
    "M'aiq was soul trapped once. Not very pleasant. You should think about that once in a while.",
    "Something strange happens to Khajiit when they arrive in Skyrim.",
    "M'aiq has heard the people in Skyrim are better-looking than the ones in Cyrodiil. He has no opinion on the matter. All people are beautiful to him.",
    "Why do soldiers bother with target practice? One learns best by hitting real people.",
    "M'aiq knows why Falmer are blind. It has nothing to do with the Dwemer disappearing. Really.",
    "M'aiq has heard it is dangerous to be your friend.",
    "The people of Skyrim are more open-minded about certain things than people in other places.",
    "Some like taking friends on adventures. M'aiq thinks being alone is better. Less arguing about splitting treasure.",
    "Don't try blocking if you have two weapons. You will only get confused. Much better to hit twice anyway.",
    "M'aiq knows many things, no?",
    "M'aiq is tired now. Go bother somebody else.",
    "M'aiq is done talking.",
]

art_channel_list = [1072264994508525609]

activity_list = [
    ("Mudcrabs", discord.ActivityType.watching),
    (discord.ActivityType.playing, "Finding Uranium Ore", ),
    (discord.ActivityType.playing, "Extracting Uranium", ),
    (discord.ActivityType.playing, "Collecting Materials", ),
    (discord.ActivityType.watching, "How to make Nuclear Weapons", ),
    (discord.ActivityType.playing, "Crafting Nuclear Weapons", ),
    (discord.ActivityType.playing, "DEFCON", ),
    (discord.ActivityType.watching, "Nuclear War", ),
]  # add better activities

lang_codes = {
    'afar': 'aa',
    'bangla': 'bn',
    'abkhazian': 'ab',
    'bambara': 'bm',
    'belarusian': 'be',
    'bashkir': 'ba',
    'azerbaijani': 'az',
    'aymara': 'ay',
    'avaric': 'av',
    'assamese': 'as',
    'arabic': 'ar',
    'aragonese': 'an',
    'amharic': 'am',
    'akan': 'ak',
    'afrikaans': 'af',
    'avestan': 'ae',
    'bulgarian': 'bg',
    'tibetan': 'bo',
    'bislama': 'bi',
    'breton': 'br',
    'bosnian': 'bs',
    'catalan': 'ca',
    'wolof': 'wo',
    'walloon': 'wa',
    'volapük': 'vo',
    'vietnamese': 'vi',
    'venda': 've',
    'uzbek': 'uz',
    'urdu': 'ur',
    'ukrainian': 'uk',
    'uyghur': 'ug',
    'tahitian': 'ty',
    'twi': 'tw',
    'tatar': 'tt',
    'tsonga': 'ts',
    'turkish': 'tr',
    'tongan': 'to',
    'tswana': 'tn',
    'tagalog': 'tl',
    'turkmen': 'tk',
    'tigrinya': 'ti',
    'thai': 'th',
    'tajik': 'tg',
    'telugu': 'te',
    'tamil': 'ta',
    'swahili': 'sw',
    'swedish': 'sv',
    'sundanese': 'su',
    'southern sotho': 'st',
    'swati': 'ss',
    'serbian': 'sr',
    'albanian': 'sq',
    'somali': 'so',
    'shona': 'sn',
    'samoan': 'sm',
    'slovenian': 'sl',
    'slovak': 'sk',
    'sinhala': 'si',
    'serbo-croatian': 'sh',
    'sango': 'sg',
    'northern sami': 'se',
    'sindhi': 'sd',
    'sardinian': 'sc',
    'sanskrit': 'sa',
    'kinyarwanda': 'rw',
    'russian': 'ru',
    'romanian': 'ro',
    'rundi': 'rn',
    'romansh': 'rm',
    'quechua': 'qu',
    'portuguese': 'pt',
    'pashto': 'ps',
    'polish': 'pl',
    'pali': 'pi',
    'punjabi': 'pa',
    'ossetic': 'os',
    'odia': 'or',
    'oromo': 'om',
    'ojibwa': 'oj',
    'occitan': 'oc',
    'nyanja': 'ny',
    'navajo': 'nv',
    'south ndebele': 'nr',
    'norwegian': 'no',
    'norwegian nynorsk': 'nn',
    'dutch': 'nl',
    'ndonga': 'ng',
    'nepali': 'ne',
    'north ndebele': 'nd',
    'norwegian bokmål': 'nb',
    'nauru': 'na',
    'burmese': 'my',
    'maltese': 'mt',
    'malay': 'ms',
    'marathi': 'mr',
    'mongolian': 'mn',
    'malayalam': 'ml',
    'macedonian': 'mk',
    'maori': 'mi',
    'marshallese': 'mh',
    'malagasy': 'mg',
    'latvian': 'lv',
    'luba-katanga': 'lu',
    'lithuanian': 'lt',
    'lao': 'lo',
    'lingala': 'ln',
    'limburgish': 'li',
    'ganda': 'lg',
    'luxembourgish': 'lb',
    'latin': 'la',
    'kyrgyz': 'ky',
    'cornish': 'kw',
    'komi': 'kv',
    'kurdish': 'ku',
    'kashmiri': 'ks',
    'kanuri': 'kr',
    'korean': 'ko',
    'kannada': 'kn',
    'khmer': 'km',
    'kalaallisut': 'kl',
    'kazakh': 'kk',
    'kuanyama': 'kj',
    'kikuyu': 'ki',
    'kongo': 'kg',
    'georgian': 'ka',
    'javanese': 'jv',
    'japanese': 'ja',
    'inuktitut': 'iu',
    'italian': 'it',
    'icelandic': 'is',
    'ido': 'io',
    'inupiaq': 'ik',
    'sichuan yi': 'ii',
    'igbo': 'ig',
    'interlingue': 'ie',
    'indonesian': 'id',
    'interlingua': 'ia',
    'herero': 'hz',
    'armenian': 'hy',
    'hungarian': 'hu',
    'haitian creole': 'ht',
    'croatian': 'hr',
    'hiri motu': 'ho',
    'hindi': 'hi',
    'hebrew': 'he',
    'hausa': 'ha',
    'manx': 'gv',
    'gujarati': 'gu',
    'guarani': 'gn',
    'galician': 'gl',
    'scottish gaelic': 'gd',
    'irish': 'ga',
    'western frisian': 'fy',
    'french': 'fr',
    'faroese': 'fo',
    'fijian': 'fj',
    'finnish': 'fi',
    'fulah': 'ff',
    'persian': 'fa',
    'basque': 'eu',
    'estonian': 'et',
    'spanish': 'es',
    'esperanto': 'eo',
    'english': 'en',
    'greek': 'el',
    'ewe': 'ee',
    'dzongkha': 'dz',
    'divehi': 'dv',
    'german': 'de',
    'danish': 'da',
    'welsh': 'cy',
    'chuvash': 'cv',
    'church slavic': 'cu',
    'czech': 'cs',
    'cree': 'cr',
    'corsican': 'co',
    'chamorro': 'ch',
    'chechen': 'ce',
    'zulu': 'zu',
    'zhuang': 'za',
    'xhosa': 'xh',
    'yoruba': 'yo',
    'yiddish': 'yi',
    'chinese': 'zh'
}