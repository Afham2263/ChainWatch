import pandas as pd
from extract import extract_coin_data

def transform_data(json_data):
    df = pd.DataFrame(json_data)

    # Optional: only keep the columns we care about
    df = df[[
        'name',
        'symbol',
        'current_price',
        'market_cap',
        'total_volume',
        'price_change_percentage_24h'
    ]]

    # Rename for clarity
    df.columns = [
        'Coin',
        'Symbol',
        'Price (USD)',
        'Market Cap',
        '24h Volume',
        '24h Change (%)'
    ]

    # Add derived columns
    df['Price (INR)'] = df['Price (USD)'] * 83.15  # Approx. USD→INR

    # Round for clean display
    df = df.round(2)

    return df
if __name__ == "__main__":
    raw_data = extract_coin_data()
    transformed_df = transform_data(raw_data)
    
    output_file = "top_10_cryptos.xlsx"
    transformed_df.to_excel(output_file, index=False)

    print(f"Data successfully saved to {output_file}")