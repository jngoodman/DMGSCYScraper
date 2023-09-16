"""Flask application should automatically:
    > Create storage directories.
    > Instantiate collections table.
    > Requests collections .html from DMGSCY.co.uk.
    > Populate the bands table with this .html data.
    Users should have a button for each band that lets them:
    > Request HTML, instantiate merch table, populate merch table and select (i.e, show in Flask) table in a single click.
    Once a table already exists, users should:
    > Have a tickbox for 'use existing data' to prevent making new requests.
    > If ticked, just select table. Otherwise, do as before.
    Users should also have a button for each band that lets them:
    > Add to a favourites list.
    Finally, users should be able to:
    > Delete data from database (i.e., drop table). <issues warning>
    > Delete database itself. <issues warning>

    Effective way to do this: When user first loads the app, they're prompted to pick their favourite bands from the
    list. These are then saved. On future loads, user can select existing bands or 'add new favourites.'

    So first goal for tomorrow - get a flask application going that displays:
    > All band names from DMGSCY.
    > Lets the user add them to a list called 'favourites'.
    > Displays 'favourites list' after clicking 'submit'.
    > On all future loads, displays favourites list with 'modify' at the bottom."""
