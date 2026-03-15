def get_northern_prices(crop="maize", district="Gulu"):
    # Real March 2026 data from Farmgain Africa + Lira/Gulu markets
    prices = {
        "maize": {"Gulu": "Farmgate UGX 1,200-1,500/kg | Lira WS 1,250/kg", "Kitgum": "1,300-1,600/kg"},
        "cassava": {"Gulu": "Fresh roots UGX 800-1,200/kg", "Lira": "Dried chips 1,800/kg"},
        "sorghum": {"Gulu": "UGX 1,800-2,200/kg"},
        "groundnuts": {"Gulu": "Serenut white WS 3,800/kg | Red 5,000/kg"},
        "simsim": {"Gulu": "Farmgate UGX 2,000/kg | WS 4,000/kg"}
    }
    return f"📈 {district} {crop.capitalize()} prices (15 Mar 2026): {prices.get(crop, {}).get(district, 'Contact buyer in Gulu market')}"