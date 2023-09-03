A web scraper to recover bands and collection URLS from https://damagedsociety.co.uk/pages/band-a-z.


Currently only the scraper which returns band names and URLs as a dictionary. Interace with via cmd line.


Goals:

1) Store all bands and URLs in a SQL .db.
2) Allow users to add valid dimension tables to schema to store the collections of band merchandise for their bands of interest. Dimension tables will contain names, image URLs and page URLs for each entry in the collection.
3) Create flask interface.
