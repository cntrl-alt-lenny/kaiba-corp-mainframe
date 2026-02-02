# YGOProDeck API Documentation (v7)

You can support our free Yu-Gi-Oh! API by purchasing a subscription to YGOPRODeck Premium.

This is currently the latest API version (v7).

**CRITICAL NOTE ON IMAGES:** Do not continually hotlink images directly from this site. Please download and re-host the images yourself. Failure to do so will result in an IP blacklist. Please read this guide on where to download images.

Upgrade Note: Please read through the documentation before upgrading to v7. Your code will not work if you simply change the endpoint to v7.

Older Versions: All older versions of the API are now deprecated.

## API Changelog v7 (last update 7th December 2023)

ygoprodeck_url is now returned for all cards.

## General Usage Info

Our Yu-Gi-Oh! API is now available for public consumption. Below are the details on how to use the API and what kind of response is to be expected from the API.

Please download and store all data pulled from this API locally to keep the amount of API calls used to a minimum. Failure to do so may result in either your IP address being blacklisted or the API being rolled back.

### Rate Limiting

Rate Limiting on the API is enabled.

Limit: 20 requests per 1 second.

Penalty: If you exceed this, you are blocked from accessing the API for 1 hour. We will monitor this rate limit for now and adjust accordingly.

### Caching

Our API responses are cached on our side. The cache timings will be given below. These are subject to change.

### 1. Get Card Information

The Card Information endpoint is available at:

`https://db.ygoprodeck.com/api/v7/cardinfo.php`

This is the only endpoint that is now needed. You can pass multiple parameters to this endpoint to filter the information retrieved.

The specific results from this endpoint are cached for 2 days (172800 seconds) but will be manually cleared upon new card entry.

#### Parameters

- `name`: The exact name of the card. You can pass multiple `|` separated names to this parameter (e.g., `Baby Dragon|Time Wizard`).
- `fname`: A fuzzy search using a string. For example `&fname=Magician` to search by all cards with "Magician" in the name.
- `id`: The 8-digit passcode of the card. You cannot pass this alongside `name`. You can pass multiple comma separated IDs.
- `konami_id`: The Konami ID of the card. This is not the passcode.
- `type`: The type of card you want to filter by. See "Card Types Returned" section. Multiple comma separated Types allowed.
- `atk`: Filter by atk value.
- `def`: Filter by def value.
- `level`: Filter by card level/RANK.
- `race`: Filter by the card race (officially called type: Spellcaster, Warrior, Insect, etc). Also used for Spell/Trap cards. Multiple comma separated Races allowed.
- `attribute`: Filter by the card attribute. Multiple comma separated Attributes allowed.
- `link`: Filter the cards by Link value.
- `linkmarker`: Filter the cards by Link Marker value (Top, Bottom, Left, Right, Bottom-Left, Bottom-Right, Top-Left, Top-Right). Multiple comma separated values allowed.
- `scale`: Filter the cards by Pendulum Scale value.
- `cardset`: Filter the cards by card set (Metal Raiders, Soul Fusion, etc).
- `archetype`: Filter the cards by archetype (Dark Magician, Prank-Kids, Blue-Eyes, etc).
- `banlist`: Filter the cards by banlist (TCG, OCG, Goat).
- `sort`: Sort the order of the cards (atk, def, name, type, level, id, new).
- `format`: Sort the format of the cards (tcg, goat, ocg goat, speed duel, master duel, rush duel, duel links). Note: Duel Links is not 100% accurate. Using tcg results in all cards with a set TCG Release Date and excludes Speed Duel/Rush Duel cards.
- `misc`: Pass yes to show additional response info.
- `staple`: Check if card is a staple.
- `has_effect`: Check if a card actually has an effect or not by passing a boolean true/false. (e.g., Black Skull Dragon has no effect).
- `startdate`, `enddate`, and `dateregion`: Filter based on cards' release date. Format dates as YYYY-mm-dd. Pass `dateregion` as tcg (default) or ocg.

#### Equation Symbols

You can also use the following equation symbols for `atk`, `def`, and `level`:

- `lt` (less than)
- `lte` (less than equals to)
- `gt` (greater than)
- `gte` (greater than equals to)

Examples: `atk=lt2500` (atk < 2500), `def=gte2000` (def >= 2000), `level=lte8` (level <= 8).

### Response Information

#### All Cards

- `id`: ID or Passcode of the card.
- `name`: Name of the card.
- `type`: The type of the card (Normal Monster, Effect Monster, Synchro Monster, Spell Card, Trap Card, etc.).
- `frameType`: The backdrop type that this card uses.
- `desc`: Card description/effect.
- `ygoprodeck_url`: Link to YGOPRODeck card page.

#### Monster Cards

- `atk`: ATK value.
- `def`: DEF value.
- `level`: Level/RANK.
- `race`: Official type (Spellcaster, Warrior, etc).
- `attribute`: Card attribute.

#### Spell/Trap Cards

- `race`: Official type (Field, Equip, Counter, etc).

#### Card Archetype

- `archetype`: The Archetype the card belongs to.

#### Pendulum Monsters

- `scale`: Pendulum Scale Value.

#### Link Monsters

- `linkval`: Link Value.
- `linkmarkers`: Array of Link Markers.

#### Card Sets

A Card Sets array is returned (`card_sets`). Contains: `set_name`, `set_code`, `set_rarity`, `set_price`.

Optionally use `tcgplayer_data` parameter to replace internal data with TCGplayer data (adds `set_edition`, `set_url`).

Note: TCGplayer data may have incorrect names/rarities.

#### Card Images

A Card Images array is returned (`card_images`). Contains: `id`, `image_url`, `image_url_small`, `image_url_cropped`.

Includes default and alternative artwork.

#### Card Prices

A Card Prices array is returned (`card_prices`).

Shows lowest price found across versions from: Cardmarket, CoolStuffInc, Tcgplayer, eBay, Amazon.

#### Banlist Info

Returned in `banlist_info` array.

- `ban_tcg`, `ban_ocg`, `ban_goat`.

#### Misc Info (if `misc=yes`)

- `beta_name`: Old/Temporary/Translated name.
- `views`, `viewsweek`: View counts.
- `upvotes`, `downvotes`.
- `formats`: Available formats.
- `treated_as`: If treated as another card (e.g., Harpie Lady 1).
- `tcg_date`, `ocg_date`: Release dates.
- `konami_id`.
- `md_rarity`.
- `has_effect`.

### Example JSON Response

```json
{
  "data": [
    {
      "id": 6983839,
      "name": "Tornado Dragon",
      "type": "XYZ Monster",
      "frameType": "xyz",
      "desc": "2 Level 4 monsters\nOnce per turn (Quick Effect): You can detach 1 material from this card, then target 1 Spell/Trap on the field; destroy it.",
      "atk": 2100,
      "def": 2000,
      "level": 4,
      "race": "Wyrm",
      "attribute": "WIND",
      "card_sets": [
        {
          "set_name": "Battles of Legend: Relentless Revenge",
          "set_code": "BLRR-EN084",
          "set_rarity": "Secret Rare",
          "set_rarity_code": "(ScR)",
          "set_price": "4.08"
        }
      ],
      "card_images": [
        {
          "id": 6983839,
          "image_url": "https://images.ygoprodeck.com/images/cards/6983839.jpg",
          "image_url_small": "https://images.ygoprodeck.com/images/cards_small/6983839.jpg",
          "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/6983839.jpg"
        }
      ],
      "card_prices": [
        {
          "cardmarket_price": "0.42",
          "tcgplayer_price": "0.48",
          "ebay_price": "2.99",
          "amazon_price": "0.77",
          "coolstuffinc_price": "0.99"
        }
      ]
    }
  ]
}
```

### Example Usage URLs

- Get all cards: `https://db.ygoprodeck.com/api/v7/cardinfo.php`
- "Dark Magician" info: `https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Dark Magician`
- "Blue-Eyes" archetype: `https://db.ygoprodeck.com/api/v7/cardinfo.php?archetype=Blue-Eyes`
- Lvl 4 Water, sort by ATK: `https://db.ygoprodeck.com/api/v7/cardinfo.php?level=4&attribute=water&sort=atk`
- TCG Banlist Lvl 4 sorted A-Z: `https://db.ygoprodeck.com/api/v7/cardinfo.php?banlist=tcg&level=4&sort=name`
- Metal Raiders Dark Monsters: `https://db.ygoprodeck.com/api/v7/cardinfo.php?cardset=metal%20raiders&attribute=dark`
- Equip Spells: `https://db.ygoprodeck.com/api/v7/cardinfo.php?type=spell%20card&race=equip`
- Speed Duel cards: `https://db.ygoprodeck.com/api/v7/cardinfo.php?format=Speed Duel`
- Staples: `https://db.ygoprodeck.com/api/v7/cardinfo.php?staple=yes`

## 2. Endpoint Values Reference

### Parameter race values

Monster Cards: Aqua, Beast, Beast-Warrior, Creator-God, Cyberse, Dinosaur, Divine-Beast, Dragon, Fairy, Fiend, Fish, Insect, Machine, Plant, Psychic, Pyro, Reptile, Rock, Sea Serpent, Spellcaster, Thunder, Warrior, Winged Beast, Wyrm, Zombie.

Spell Cards: Normal, Field, Equip, Continuous, Quick-Play, Ritual.

Trap Cards: Normal, Continuous, Counter.

### Parameter type values

Main Deck: Effect Monster, Flip Effect Monster, Flip Tuner Effect Monster, Gemini Monster, Normal Monster, Normal Tuner Monster, Pendulum Effect Monster, Pendulum Effect Ritual Monster, Pendulum Flip Effect Monster, Pendulum Normal Monster, Pendulum Tuner Effect Monster, Ritual Effect Monster, Ritual Monster, Spell Card, Spirit Monster, Toon Monster, Trap Card, Tuner Monster, Union Effect Monster.

Extra Deck: Fusion Monster, Link Monster, Pendulum Effect Fusion Monster, Synchro Monster, Synchro Pendulum Effect Monster, Synchro Tuner Monster, XYZ Monster, XYZ Pendulum Effect Monster.

Other: Skill Card, Token.

## 3. Endpoint Languages

We offer the API in: English, French (fr), German (de), Portuguese (pt), and Italian (it).

Pass `&language=` along with the code.

Card images are only stored in English.

Newly revealed cards are English only until official translation.

## 4. Card Images (IMPORTANT)

Images are pulled from our image server images.ygoprodeck.com. You must download and store these images yourself!

Please only pull an image once and then store it locally. If we find you are pulling a very high volume of images per second then your IP will be blacklisted and blocked.

URLs:

- Full size: `https://images.ygoprodeck.com/images/cards/`
- Small: `https://images.ygoprodeck.com/images/cards_small/`
- Cropped: `https://images.ygoprodeck.com/images/cards_cropped/`

Pass the ID of the card to retrieve the image. Example (Limit Reverse): `https://images.ygoprodeck.com/images/cards/27551.jpg`

## 5. Other Endpoints

### Random Card

`https://db.ygoprodeck.com/api/v7/randomcard.php`

Cache Control is disabled.

Returns an error if parameters are passed.

### All Card Sets

`https://db.ygoprodeck.com/api/v7/cardsets.php`

Returns all Card Set Names, Codes, Card Counts, and TCG Dates.

### Card Set Information

`https://db.ygoprodeck.com/api/v7/cardsetsinfo.php`

Requires setcode parameter (e.g., `?setcode=SDY-046`).

Returns id, name, set_name, set_code, set_rarity, set_price.

### All Card Archetypes

`https://db.ygoprodeck.com/api/v7/archetypes.php`

Returns all Archetype names sorted A-Z.

### Check Database Version

`https://db.ygoprodeck.com/api/v7/checkDBVer.php`

Not cached. Incremented when new cards are added or info is modified.

## Error Checking

All error codes return a 400 response header.

Invalid parameters will return an error JSON explaining valid values.

The only way to return all cards is to pass 0 parameters.
