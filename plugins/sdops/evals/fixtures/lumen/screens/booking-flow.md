# Flow: Book a stay (iOS), frames "Book / 1" to "Book / 4"

1. Hotel detail: photos, rating, amenities, sticky footer with price and "Choose room" (`Button/Primary`).
2. Choose room: list of rooms with "Select" buttons; a sold-out room is greyed with a "Sold out" chip.
3. Guest details and payment: form with name, email, card (via payment provider sheet); "Pay" button.
4. Confirmation: success illustration, booking reference, "Add to calendar", "View trip".

Branches seen: 3a payment declined → inline error above "Pay", stays on step 3.
Entry points: Home search results, Saved list. Exit: Confirmation → Trips tab.
