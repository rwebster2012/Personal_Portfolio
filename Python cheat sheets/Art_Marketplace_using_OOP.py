class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  def remove_listing(self, listing_to_remove):
    self.listings.remove(listing_to_remove)
    
  def show_listings(self):
    for listing in self.listings:
      print(listing)

veneer = Marketplace()

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      listing = Listing(artwork, price, artwork.owner)
      veneer.add_listing(listing)
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          artwork.owner = self
          veneer.remove_listing(art_listing)
    
edytta = Client('Edytta Halpirt', 'Private Collection', False)
moma = Client('The MOMA', 'New York', True)
  
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return '{name}. "{painting_title}". {year_created}, {built_on}. {owner}, {owners_location}.'.format( name = self.artist, painting_title = self.title, year_created = self.year, built_on = self.medium, owner = self.owner.name, owners_location = self.owner.location)
  
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin', 1910, 'oil on canvas', edytta)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "{art_name}, ${art_price} .".format(art_name = self.art.title, art_price = self.price)

#below print statement shows that the artwork is assigned to edytta
print(girl_with_mandolin)

#veneer.show_listings()
#below should add the girl with mandolin to the art listings 
edytta.sell_artwork(girl_with_mandolin, '6M (USD)')

#shows the current art listing
print(veneer.show_listings())

#below should buy the specified art from the art listings
moma.buy_artwork(girl_with_mandolin)

#below should show an owner change on the piece of art and there should be no more current art listings
print(girl_with_mandolin)
print(veneer.show_listings())


