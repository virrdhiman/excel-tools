import pandas as pd

# 1. Define Sheet1 Data (Login & Webmail Credentials)
login_data = {
    "Identifier": ["virender.demo@yourdomain.com"],
    "EmailPassword": ["SecureWebmailPass123!"]
}

# 2. Define Sheet2 Data (Gift Cards & PINs Layout)
gift_card_data = {
    "CardNumber": ["6000123456789012", "6000123456789013", "6000123456789014"],
    "Pin": ["112233", "445566", "778899"]
}

# Convert dictionary structures to Pandas DataFrames
df_login = pd.DataFrame(login_data)
df_gift = pd.DataFrame(gift_card_data)

# Write to a single Excel workbook with multiple tabs
with pd.ExcelWriter("flipkart_data.xlsx", engine="openpyxl") as writer:
    df_login.to_excel(writer, sheet_name="Sheet1", index=False)
    df_gift.to_excel(writer, sheet_name="Sheet2", index=False)

print("[+] 'flipkart_data.xlsx' created successfully with Sheet1 and Sheet2!l sheet)
      
      