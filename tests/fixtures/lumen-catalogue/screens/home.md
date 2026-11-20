# Screen: Home (iOS, 390 × 844), frame "Home / default"

Top to bottom:
1. Top bar: avatar left, "Lumen" wordmark centre, bell icon right (component `NavBar/Top`).
2. Search card: destination field, dates field, guests field, primary button "Search" (`Card/Search`, `Input/Field`, `Button/Primary`).
3. "Recently viewed": horizontal carousel of hotel cards with photo, name, price per night (`Card/Hotel`).
4. "Deals for you": list of 3 rows, each a thumbnail, title, discount chip (`List/Row`, `Chip/Discount`).
5. Tab bar: Home, Trips, Saved, Profile (`TabBar`).

States seen in the file: default, loading (skeleton cards), empty "Recently viewed" (section hidden).
